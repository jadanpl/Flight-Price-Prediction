import streamlit as st
import pandas as pd
import pickle

st.header('Flight Price Prediction')
st.write("Let's check out possible flight price for your desired flight.")
st.write('Dataset was provided by [Shubham Bathwal on Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)')
st.image("https://images.pexels.com/photos/723240/pexels-photo-723240.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
st.caption("Photo by [Anugrah Lohiya on Pexels](https://www.pexels.com/photo/photography-of-airplane-during-sunrise-723240/)")

def user_input():
    airline = st.selectbox(label='Which airline do you prefer?',
                           label_visibility='visible',
                           options=['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'])
    source_city = st.selectbox(label='Where you will depart from?',
                               label_visibility='visible',
                               options=['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'],)
    departure_time = st.selectbox(label='What time do you prefer for departure?',
                                  label_visibility='visible',
                                  options=['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'])
    stops = st.selectbox(label='How many stops between the flight?',
                         label_visibility='visible',
                         options=['zero', 'one', 'two_or_more'])
    arrival_time = st.selectbox(label='What time do you wish to arrive?',
                                label_visibility='visible',
                                options=['Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening', 'Late_Night'])
    destination_city = st.selectbox(label='Where is your destination city?',
                                    label_visibility='visible',
                                    options=['Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'])
    flight_class = st.radio(label='Select the class of flight.',
                            label_visibility='visible',
                            options=['Economy', 'Business'])
    duration = st.slider(label="Select the duration of your flight",
                         min_value=0.83, max_value=49.83, value=15.52, step=1e-2, format="%.2f")
    days_left = st.slider(label="Select the number of days before your departure",
                          min_value=1, max_value=49, value=26)

    inputs = pd.DataFrame({'airline': [airline],
                           'source_city': [source_city],
                           'departure_time': [departure_time],
                           'stops': [stops],
                           'arrival_time': [arrival_time],
                           'destination_city': [destination_city],
                           'class': [flight_class],
                           'duration': [duration],
                           'days_left': [days_left]}, index=[0])
    return inputs

input_df = user_input()

st.subheader('Your Selection')
st.dataframe(input_df)

# Load saved regression model
model = pickle.load(open('rf_reg.pkl', 'rb'))

# Apply model to make predictions
prediction = model.predict(input_df)
st.subheader('Prediction')
if prediction<=0:
    st.success("Out of scope. Please select other option. Thank you!")
else:
    st.success(f'The estimated flight price is {"${:,.2f}".format(prediction[0])}. Safe trip! ✈️')
