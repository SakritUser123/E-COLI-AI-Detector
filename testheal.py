import streamlit as st

# Set up the Streamlit page
st.title('E. coli Risk Prediction Form')

# Initialize the risk variable
risk = 0

# Create the form
with st.form(key='my_form'):
    # Add inputs to the form
    name = st.text_input('Enter your name:')
    age = st.number_input('Enter your age:', min_value=0)
    gender = st.selectbox('Select your gender:', ['Male', 'Female'])
    
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
