import pandas as pd
import os 
import tensorflow as tf
import urllib.request
import urllib.request
import streamlit as st
import streamlit as st  
import time
st.sidebar.title("Models")
tabs = ["Home","E.Coli Detection","Cancer Detection","Blood test Analyzer","Info"]
selected_tab = st.sidebar.radio("Select A Model",tabs)

if selected_tab == "Home":
    st.title("Home Page")
    st.write("Use The navigation bar to navigate the various models on the website!")
    

    st.write("Click below to donate with PayPal:")
    if st.button("Donate"):
        st.markdown('[Click here to pay](https://www.paypal.me/KavithaKesavalu)', unsafe_allow_html=True)


    st.write("You can donate to this website it will help out a lot!")
    st.markdown("""
---
Contact: [veerendrasakthi.prabhurajan@gmail.com]  
GitHub: [The repository for this website!](https://github.com/SakritUser123/E-COLI-AI-Detector)
""")
if selected_tab == "Info":
    st.title("Info About This Website")
    st.write("This website is a website for various healthcare models that help with diagnosing various medical conditions.")
if selected_tab == "Blood test analyzer":
    st.title("Broken Bones AI Detection")
if selected_tab == "E.Coli Detection":
    st.title("E-Coli AI Detector")
    with st.form(key='my_form'):
        risk = 0
        # Add inputs to the form
        name = st.text_input('Enter your name:')
        age = st.number_input('Enter your age:', min_value=0)
        gender = st.selectbox('Select your gender:', ['Male', 'Female', 'Other'])
    
    # Additional factors based on age and gender
        if age > 25 and gender == 'Female':
            preg = st.selectbox('Are you pregnant?', ['No', 'Yes'])
        else:
            preg = 'No'
    
    # Factors related to age
        if age <= 5:
            risk += 15
        elif age >= 65:
            risk += 20
        elif 18 <= age <= 30:
            risk += 12.5
        else:
            risk += 0
        
    # Other health conditions
        diabetes = st.selectbox('Do you have diabetes?', ['No', 'Yes'])
        if diabetes == 'Yes':
            risk += 22.5
        
        immune_system = st.checkbox('Do you have a weakened immune system? (e.g., HIV, cancer)')
        if immune_system:
            risk += 30
        
        ulc = st.selectbox('Do you have ulcerative colitis?', ['No', 'Yes'])
        if ulc == 'Yes':
            risk += 15
        
        chro = st.selectbox('Do you have chronic kidney disease?', ['No', 'Yes'])
        if chro == 'Yes':
            risk += 25
        
        surgery = st.selectbox('Did you recently have surgery or were you recently hospitalized?', ['No', 'Yes'])
        if surgery == 'Yes':
            risk += 15
        
        food = st.selectbox('Have you eaten undercooked meat or unpasteurized dairy in the past few days?', ['No', 'Yes'])
        if food == 'Yes':
            risk += 35
    
    # Submit button for the form
        submit_button = st.form_submit_button(label='Submit')

# Placeholder for displaying the result at the bottom of the page
    result_placeholder = st.empty()

# Process the form when the submit button is clicked
    if submit_button:
        # After submit, show the result based on the calculated risk
        result_placeholder.write(f"Hello {name},")
        result_placeholder.write(f"You are {age} years old and identified as {gender}.")
        
        if preg == 'Yes':
            result_placeholder.write("You are pregnant, which increases your risk of E. coli.")
        
    result_placeholder.write(f"Your calculated risk of contracting E. coli is **{risk}%** higher than the average population.")

if selected_tab == 'Cancer Detection':

    import streamlit as st
    import tensorflow as tf
    import cv2
    import numpy as np
    from PIL import Image
    import os

    model = tf.keras.models.load_model('cal.h5')
    st.write("Model loaded successfully!")
    st.title("Cancer Detection Model")
    

# File uploader to upload images
    uploaded_file = st.file_uploader("Choose an image...")
        
    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
    if st.session_state.uploaded_file:     
            
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        st.session_state.image_np = image_np
        st.image(image, caption="Uploaded Image", use_column_width=True)
    if st.session_state.uploaded_file:    
        IMG_SIZE = (150, 150)
        image = np.array(image)

        new = cv2.resize(image,IMG_SIZE)
        print(f"Resized image shape: {new.shape}")  

        img_normalized = new.astype('float32') / 255.0

        img_normalized = np.expand_dims(img_normalized, axis=0)
        prediction = model.predict(img_normalized)
        # Call the prediction function and display result

        st.write(f"Raw Prediction Output: {prediction}")
    
        if prediction >= 0.50:
            
            st.write("It is more  likely to be cancer")
        else:
            st.write("It is less likely to be cancer")

