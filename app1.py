import streamlit as st
import pandas as pd
from PIL import Image 
import tempfile
import cv2 as cv
from streamlit_option_menu import option_menu
@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

def main():
	st.title("Smartathon")	
	with st.sidebar:
		choose = option_menu("MENU", ["About", "EDA", "Model"])
	if choose == "Model":
			st.subheader("Detection and evaluation of the following elements on street imagery taken from a moving vehicle")
			image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
			if image_file is not None:
				file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
				st.write(file_details)
				img = load_image(image_file)
				st.image(img)

if __name__ == '__main__':
    main()