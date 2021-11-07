import os
from PIL import Image
import streamlit as st
import time

os.chdir("darknet")

# file_up = st.file_uploader("Upload an image", type="jpg")
# image = Image.open(file_up)
# st.image(image, caption='Uploaded Image.', use_column_width=True)
# image = image.save('inp_img.jpg')

# os.system('./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights inp_img.jpg')
# time.sleep(1)
# out_img = Image.open('predictions.jpg')
# st.image(out_img, caption='Model prediction', use_column_width=True)

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    image = image.save('inp_img.jpg')
    st.write("")
    st.write("Predicting...")
    os.system('./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights inp_img.jpg')
    time.sleep(1)
    out_img = Image.open('predictions.jpg')
    st.image(out_img, caption='Model prediction', use_column_width=True)