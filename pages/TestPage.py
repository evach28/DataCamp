import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras_preprocessing import image

st.set_page_config(layout="wide")


st.sidebar.markdown("# Try the solution")

st.title("Try our solution here !")
uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file)
    img = Image.open(uploaded_file)
    img = img.resize((224,224))
    img= img.convert(mode="RGB")
    model=load_model(r"C:\Users\evach\OneDrive\Documents\Semestre 7\DataCamp\dataset_pneumonia\our_model.h5") 

    imagee=image.img_to_array(img) 
    imagee=np.expand_dims(imagee, axis=0)
    img_data=preprocess_input(imagee)
    prediction=model.predict(img_data)

    result = st.checkbox("Click here if you need a result, remeber that this app isn't a medical device")
    if (result == True): 
        if prediction[0][0]>prediction[0][1]: 
            st.write('The result is negative, but contact a doctor the result is not safe at 100%')
        else:
            st.write('The result is positive, contact a doctor')
        st.write(f'Predictions: {prediction}')
    st.markdown("***")
    text7 = '<p style="font-family:Rockwell; color:White; font-size: 25px; width:100%;">Thanks for using DeteX !</p>'
    text8 = '<p style="font-family:Rockwell; color:White; font-size: 25px; width:100%;">Take care of yourself</p>'
    st.write(text7, unsafe_allow_html=True)
    st.write(text8, unsafe_allow_html=True)


text6 = '<p style="font-family:Rockwell; color:White; font-size: 25px; width:100%;">Independently of the result, get the advice of an expert </p>'
st.write(text6, unsafe_allow_html=True)
st.write('[Doctolib](https://www.doctolib.fr/pneumo-allergologue)')

    





