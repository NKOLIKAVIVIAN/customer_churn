# Step 1: Load your libraries
import streamlit as st
import pandas as pd
import joblib 
from PIL import Image
print('Libraries Imported Successfully')

# Step 2: Load Model
model = joblib.load('gb_model.pkl')
print('Model Loaded Successfully')

# Step 3: Set Streamlit Title and Header
st.title('Telecom Customer Churn Prediction')
image = Image.open('telecom_image.jpg') 
st.image(image, use_container_width=True)
st.write('This Application predicts whether a telecom customer is likely to churn based on some attributes')
st.header('Kindly Provide the Following Information')
print('Streamlit Title and Header Set Successfully')

# Step 4: Define Input Paramters
account_weeks = st.number_input('Account Weeks', min_value=1, max_value=243, value=10)
contract_renewal = st.selectbox('Contract Renewal', options=[0,1], format_func=lambda x: "Yes" if x== 1 else "No")
data_plan = st.selectbox('Data Plan', options=[0,1], format_func=lambda x: "Yes" if x== 1 else "No")
data_usage = st.number_input('Data Usage', min_value=0.0, max_value=5.4, value=2.0, step=0.1)
cust_serv_calls = st.number_input('Customer Service Calls', min_value=0, max_value=9, value=2)
day_mins = st.number_input('Day Minutes', min_value=0.0, max_value=350.8, value=150.0, step=0.1)
day_calls = st.number_input('Day Calls', min_value=0, max_value=165, value=80)
monthly_charge = st.number_input('Monthly Charge', min_value=14.0, max_value=111.3, value=70.0, step=0.1)
overage_fee = st.number_input('Overage Fee', min_value=0.0, max_value=18.2, value=5.0, step=0.1)
roam_mins = st.number_input('Roaming Minutes', min_value=0.0, max_value=20.0, value=5.0, step=0.1)
print('Input Parameters Created Successfully')

# Step 5: Create a dictionary from the input parameter
input_data = {
'AccountWeeks': account_weeks,
'ContractRenewal': contract_renewal,
'DataPlan': data_plan,
'DataUsage': data_usage,
'CustServCalls': cust_serv_calls,
'DayMins': day_mins,
'DayCalls': day_calls,
'MonthlyCharge': monthly_charge,
'OverageFee': overage_fee,
'RoamMins': roam_mins
} 
print('Dictionary Created Successfully')

# Step 6: Convert the Dictionary to a Pandas DataFrame
input_df = pd.DataFrame([input_data])
print('DataFrame Created Successfully')

# Step 7: Make Predictions
if st.button('Predict Churn'):
    try:
        prediction = model.predict(input_df)
        st.subheader('Prediction Result')
        if prediction[0] == 1:
            st.error(f'This Customer is likely to CHURN')
        else:
            st.success(f' This Customer is likely to STAY')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
print('Model Deployed Successfully')