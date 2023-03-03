import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Will patient turn septic?')
st.markdown('Sample tool for hospitals to decide if patient will turn septic in next hour.')

st.header('Input here')
col1, col2, col3 = st.columns(3)



with col1:
    st.text('Vital Signs')
    HR = st.slider('Heart Rate', 20, 200, 1)
    O2Sat = st.slider('Pulse Oximetry', 20, 200, 1)
    Temp = st.slider('Temperature in Deg C', 35.0, 43.0, 33.0)
    SBP = st.number_input('Systolic bp', 100)
    DBP = st.number_input('Diastolic bp', 70)
    Resp = st.number_input('Breaths per minute (Respiration)', 15)
    
with col2:
    st.text('Lab readings')
    BUN = st.number_input('Blood Urea Nitrogen', 20)
    Calcium = st.number_input('Calcium', 8)
    Glucose = st.number_input('Glucose', 100)
    Magnesium = st.number_input('Magnesium', 2.0)
    Potassium = st.number_input('Potassium', 4.0)
    Hgb = st.number_input('Haemoglobin count', 8.5)
    WBC = st.number_input('White blood cell count', 100)
    Platelets = st.number_input('Platelet count', 100)

with col3:
    st.text('Demographics')
    Age = st.number_input('Age', 100)
    Gender = st.number_input('Gender (1 for Male and 0 for Female)', 1)
    HospAdmTime = st.number_input('Time between hospital and ICU admission', -1.0)

if st.button('Predict if septic'):
    result = predict(np.array([[HR,O2Sat,Temp,SBP,DBP,Resp,BUN,
                                Calcium,Glucose,Magnesium,Potassium,
                                Hgb,WBC,Platelets,Age,Gender,HospAdmTime]]))
    
    st.text('Predicted Sepsis in next hour:')
    st.text(result[0])