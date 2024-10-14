import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''


date = st.date_input(
    "When's the date?",
    datetime.date(2019, 7, 6))

# Time input
time = st.time_input(
    "What time?",
    datetime.time(12, 00))

datetime_combined = datetime.datetime.combine(date, time)
st.write('Selected date and time:', datetime_combined)

# - pickup longitude
pickup_longitude = st.number_input('pickup longitude', format="%.6f")
# - pickup latitude
pickup_latitude = st.number_input('pickup latitude', format="%.6f")

# - dropoff longitude
dropoff_longitude = st.number_input('dropoff longitude', format="%.6f")

# - dropoff latitude
dropoff_latitude = st.number_input('dropoff latitude' ,format="%.6f")

#passenfer input
passenger_count = st.number_input('passenger count' )



url = 'https://taxifare-1034799751993.europe-west1.run.app/predict'

params = {
    "pickup_datetime": datetime_combined,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}


response = requests.get(url,params=params)
'''## Finally, we can display the prediction to the user
'''

# Check if the response is successful (status code 201)
if response.status_code == 200:  # Resource created successfully
    st.success('Resource created successfully!')
    data = response.json()
    st.write('Response:', data)
else:
    st.error(f'Failed to create resource. Status code: {response.status_code}')
