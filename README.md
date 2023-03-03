# DSI Capstone Project : Early Sepsis Prediction
For the fulfillment of requirements of Data Science Immersive Flex Course.

# Executive Summary

# Problem Statement
To identify whether a person has sepsis based on early physiological factors provided such as vital signs (pulse oximetry, systolic/ diastolic blood pressure), lab values and demographics provided

The goal of the analysis is the early detection of sepsis using physiological data. The early prediction of sepsis is potentially life-saving, and we aim to predict sepsis n hours before the clinical prediction. Late prediction of sepsis is potentially life-threatening, and also consumes heavy hospital resources. By predicting sepsis in non-sepsis patients or predicting sepsis very early in sepsis patients consumes limited resources and we can assume the risk of prediction to be minimal.


# EDA and Observations

- Only about 1.8% of raw records indicate sepsis [27916 / 1524294]
- Out of 40,336 unique patients, only about 7.3% patients have onset of sepsis [2932/40336]
![image](https://user-images.githubusercontent.com/110540717/220344215-fe2eb842-d7f2-4aa8-a249-e68871e7bd03.png)

### Demographics
The distribution of Gender and Age groups do not show any particular subgroup of patients being especially prone to sepsis. 
![image](https://user-images.githubusercontent.com/110540717/222811621-dee1ab7f-7153-40c3-baf8-18f1f9fec7b8.png)

![image](https://user-images.githubusercontent.com/110540717/222811589-1928b0d7-7c6f-4063-8e77-48e480781ea4.png)

#### 1. Gender
More patient data was collected for Gender 1 than Gender 0 in the entire dataset. Higher proportion of Gender 1 turned septic (7.7%) compared to Gender 0 (6.7%)
![image](https://user-images.githubusercontent.com/110540717/222811643-8ea79f95-29a2-4c67-b622-4df07d8fd8dd.png)


#### 2. Age Group
Data shows no particular trend that age group by itself relates to incidence rate of sepsis
![image](https://user-images.githubusercontent.com/110540717/222811471-19561235-703f-472d-b9f2-988d95f26605.png)


### Aggregate amount of time spent by patient in hospital

Patients with onset of sepsis have longer stay in the hospital, while all patients without onset of sepsis are discharged within 60 hours of admission to the hospital. This could be because patients with sepsis have serious conditions that might need longer hospitalisation to treat and monitor, instead of an indication that patients with long stay have a higher chance of sepsis onset. 

### Hours of hospitalisation it takes for Sepsis Onset
- Sepsis reported in the first hour for 14.5% of sepsis patients [426/2932]
- Sepsis reported in first 5 hours for 25.0% of sepsis patients [733/2932]
- Sepsis reported in first 10 hours for 32% of sepsis patients [948/2932]
- Median hour of sepsis onset = 28.0
![image](https://user-images.githubusercontent.com/110540717/220344557-9ba0fbe6-ecbd-4e77-b271-151268a862fb.png)


# Data Preparation:

### Steps
1. Impute missing data with nearest front/ back record for same patient
2. For each patient, take an aggregate of 3 hours before the real/pseudo sepsis onset
3. Drop all rows with at least 1 Null value after imputation
4. Drop variables that are highly correlated with corr>0.6
5. Upscale minority data class if imbalanced

### Correlated Values
![image](https://user-images.githubusercontent.com/110540717/222810161-b5ef010d-2335-4b6a-8778-7d4a00729077.png)
Variables to omit from model
- SepsisOnsetHour: Most values are 28h as the median time of onset was applied as pseudo-onset
- Patient: No meaning to include Patient number
- Hgb and Hct highly correlated (drop Hct)
- MAP and DBP are highly correlated (drop MAP)
- Phosphate, Creatinine and BUN are all highly correlated (drop Phosphate and Creatinine)


### Data Dictionary for the final training dataset


|No|Name|Category|Type of Variable|Description|
|---|:---|:---|:---|:---|
|1.|HR|Vital Sign|numerical|Heart Rate (beats per minute) ^ |
|2.|O2Sat|Vital Sign|numerical|Pulse Oximetry (%)^ |
|3.|Temp|Vital Sign|numerical|Temperature (Deg C)^ |
|4.|SBP|Vital Sign|numerical|Systolic BP (mm Hg)^|
|5.|DBP|Vital Sign|numerical|Diastolic BP (mm Hg)^|
|6.|Resp|Vital Sign|numerical|Respiration Rate (breaths per minute)^|
|7.|BUN|Laboratory Values|numerical|Blood Urea Nitrogen (mg/dL)^|
|8.|Calcium|Laboratory Values|numerical|Calcium (mg/dL)^|
|9.|Glucose|Laboratory Values|numerical|Serum Glucose (mg/dL)^|
|10.|Magnesium|Laboratory Values|numerical|Magnesium (mmol/dL)^|
|11.|Potassium|Laboratory Values|numerical|Potassium (mmol/dL)^|
|12.|Hgb|Laboratory Values|numerical|Hemoglobin (g/dL)^|
|13.|WBC|Laboratory Values|numerical|Leukocyte count (count * 10^3/microL)^|
|14.|Platelets|Laboratory Values|numerical|Platelet count (count * 10^3/microL)^|
|15.|SepsisLabel|Target variable|boolean|1 if patient turned septic in hour T0, else 0|
|16.|Gender|Demographics|boolean|Patient's Gender shown as 0 or 1 (not specified male or female)|
|17.|Age|Demographics|numerical|Patient's Age in Years (Reflected as 100 for patients 90 and above)|
|18.|HospAdmTime|Demographics|numerical|Hours between hospital admit and ICU admit|

^ Represents average reading for 3 hour window before sepsis onset/ pseudo-onset of sepsis (i.e. if onset was T0, readings are average of hours T-3 to T-1).

### Distributions of final data for modelling
![image](https://user-images.githubusercontent.com/110540717/222810248-31066bae-cbfa-485f-b0c8-16286520d31e.png)

# Modelling 

### Metrics evaluation on chosen classifier models
![image](https://user-images.githubusercontent.com/110540717/222810976-34f81f75-82f9-4f2e-84b9-f5a82fdcf0a4.png)


### Best Model: Extra Trees Classifier

- Area under the ROC Curve:

![image](https://user-images.githubusercontent.com/110540717/222810427-4595babf-9c1f-43bd-a73f-54b1f367d5a0.png)

- Confusion Matrix
![image](https://user-images.githubusercontent.com/110540717/222810529-0e67de43-d3a8-496a-802c-246316bb36d3.png)

- Top feature importance

![image](https://user-images.githubusercontent.com/110540717/222810564-20b33ae0-602d-4245-b37b-357fec1ed491.png)


# Conclusion:

### Model:
Best model (Extra Trees Classifier) has a high AUC score about 0.91 and Recall of 0.81.

Top 3 most important features for sepsis prediction (1h advance prediction window):
Temperature (deg Celsius)
Respiration rate (breaths per minute)
Blood Urea Nitrogen

*There is a good spread of Vital signs and Laboratory values among the best predictors, hence no conclusion on whether vital signs or laboratory readings are more important

### Recommendations:
Adding the following features for better model performance:
- Changes in vital signs over the past x hours (e.g. Difference in Heart Rates at hours T-1 and T-5)
- Rate of change in vital signs over past x hours
- Text analysis of doctor’s remarks

### Limitations:
- Do not have external test datasets outside of this dataset
- Only have data of sepsis onset; no data on septic shock or eventual death, hence cannot evaluate severity

