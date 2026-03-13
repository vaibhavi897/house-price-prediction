import streamlit as st
import pickle
import pandas as pd

# Load trained model


model = pickle.load(open("../models/house_price_model.pkl", "rb"))

st.title("House Price Prediction")

st.write("Enter house details to predict price")

# User inputs
overall_qual = st.slider("Overall Quality", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sq ft)", 500, 5000, 1500)
garage_cars = st.slider("Garage Capacity", 0, 4, 1)
total_bsmt_sf = st.number_input("Basement Area", 0, 3000, 800)
year_built = st.number_input("Year Built", 1900, 2024, 2000)

# Create dataframe from inputs
input_data = pd.DataFrame({
    "OverallQual":[overall_qual],
    "GrLivArea":[gr_liv_area],
    "GarageCars":[garage_cars],
    "TotalBsmtSF":[total_bsmt_sf],
    "YearBuilt":[year_built]
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")