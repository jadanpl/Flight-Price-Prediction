import os
import pickle
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️",
    layout="wide"
)

# 2. Helper Functions & Model Loading
@st.cache_resource
def load_model(model_filename):
    """Loads the pre-trained standard pickle model."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, model_filename)

    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data


# Load trained pipeline once on startup
model = load_model('rf_reg.pkl')

# 3. Header Section
st.title('✈️ Flight Price Prediction')
st.write("Estimate ticket prices based on departure route, timing, class, and advance booking windows.")
st.caption(
    "Dataset source: [Shubham Bathwal on Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)")

st.image(
    "https://images.pexels.com/photos/723240/pexels-photo-723240.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    use_container_width=True
)
st.caption(
    "Photo by [Anugrah Lohiya on Pexels](https://www.pexels.com/photo/photography-of-airplane-during-sunrise-723240/)")

st.markdown("---")

# 4. User Inputs Section
st.subheader("Enter Flight Details")

with st.form("flight_input_form"):
    col1, col2 = st.columns(2)

    with col1:
        airline = st.selectbox(
            label='Airline Preference',
            options=['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India']
        )
        source_city = st.selectbox(
            label='Departure City',
            options=['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
        )
        departure_time = st.selectbox(
            label='Departure Time',
            options=['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night']
        )
        stops = st.selectbox(
            label='Number of Stops',
            options=['zero', 'one', 'two_or_more']
        )
        flight_class = st.radio(
            label='Flight Class',
            options=['Economy', 'Business'],
            horizontal=True
        )

    with col2:
        destination_city = st.selectbox(
            label='Destination City',
            options=['Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi']
        )
        arrival_time = st.selectbox(
            label='Arrival Time',
            options=['Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening', 'Late_Night']
        )
        duration = st.slider(
            label="Flight Duration (Hours)",
            min_value=0.83,
            max_value=49.83,
            value=15.52,
            step=0.01,
            format="%.2f"
        )
        days_left = st.slider(
            label="Days Before Departure",
            min_value=1,
            max_value=49,
            value=26
        )

    submit_btn = st.form_submit_button("Predict Ticket Price", use_container_width=True)

# 5. Prediction Execution
if submit_btn:
    input_df = pd.DataFrame({
        'airline': [airline],
        'source_city': [source_city],
        'departure_time': [departure_time],
        'stops': [stops],
        'arrival_time': [arrival_time],
        'destination_city': [destination_city],
        'class': [flight_class],
        'duration': [duration],
        'days_left': [days_left]
    })

    st.subheader('Selected Flight Parameters')
    st.dataframe(input_df, use_container_width=True)

    prediction = model.predict(input_df)[0]

    st.subheader('Estimated Price')
    if prediction <= 0:
        st.warning("Selected configuration is out of scope. Please adjust your criteria.")
    else:
        st.success(f"Estimated Fare: **₹{prediction:,.2f}** (or approx **${prediction / 83:,.2f} USD **)")
