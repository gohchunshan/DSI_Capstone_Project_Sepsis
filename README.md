# DSI_Capstone_Project_Sepsis
Capstone Final Project for Data Science Immersive Flex course

# Early Sepsis Prediction
For the fulfillment of requirements of Data Science Immersive Flex Course.


# Problem Statement:
To identify whether a person has sepsis based on early physiological factors provided such as vital signs (pulse oximetry, systolic/ diastolic blood pressure), lab values and demographics provided

The goal of the analysis is the early detection of sepsis using physiological data. The early prediction of sepsis is potentially life-saving, and we aim to predict sepsis n hours before the clinical prediction. Late prediction of sepsis is potentially life-threatening, and also consumes heavy hospital resources. By predicting sepsis in non-sepsis patients or predicting sepsis very early in sepsis patients consumes limited resources and we can assume the risk of prediction to be minimal.

Secondarily, we also wish to find the optimal window (number of hours in advcance) to predict sepsis based on the dataset.

# EDA and Observations:

- Only about 1.8% of raw records indicate sepsis [27916 / 1524294]
- Out of 40,336 unique patients, only about 7.3% patients have onset of sepsis [2932/40336]
![image](https://user-images.githubusercontent.com/110540717/220344215-fe2eb842-d7f2-4aa8-a249-e68871e7bd03.png)

### Aggregate amount of time spent by patient in hospital

Patients with onset of sepsis have longer stay in the hospital, while all patients without onset of sepsis are discharged within 60 hours of admission to the hospital. This could be because patients with sepsis have serious conditions that might need longer hospitalisation to treat and monitor, instead of an indication that patients with long stay have a higher chance of sepsis onset. 

### Hours of hospitalisation it takes for Sepsis Onset
- Sepsis reported in the first hour for 14.5% of sepsis patients [426/2932]
- Sepsis reported in first 5 hours for 25.0% of sepsis patients [733/2932]
- Sepsis reported in first 10 hours for 32% of sepsis patients [948/2932]
- Median hour of sepsis onset = 28.0
![image](https://user-images.githubusercontent.com/110540717/220344557-9ba0fbe6-ecbd-4e77-b271-151268a862fb.png)


# Data Preparation:


### Impute missing values


# Preliminary Modelling:

### Model 1:
![image](https://user-images.githubusercontent.com/110540717/220348039-d784994b-9b44-443b-939d-d16114dffffd.png)

![image](https://user-images.githubusercontent.com/110540717/220347874-6bf5afef-ae83-4ed1-b15b-a46b9513d4e0.png)


### Model 2:
![image](https://user-images.githubusercontent.com/110540717/220348231-f7f84f04-1a3b-4184-8140-509d583e33eb.png)


Conclusion:

Recommendations:
