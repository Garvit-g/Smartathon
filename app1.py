import streamlit as st
import pandas as pd
from PIL import Image 
import tempfile
import cv2 as cv

def main():
    st.title("Smartathon")
    st.subheader("Detection and evaluation of the following elements on street imagery taken from a moving vehicle")
    video_file = st.file_uploader("Upload Video",type=['mp4','mp3'])
    if video_file is not None:
        file_details = {"Filename":video_file.name,"FileType":video_file.type,"FileSize":video_file.size}
        st.write(file_details)
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(video_file.read())
        vf = cv.VideoCapture(tfile.name)
        stframe = st.empty()

        while vf.isOpened():
            ret, frame = vf.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            stframe.image(frame)
if __name__ == '__main__':
    main()