import streamlit as st
import base64
import pickle
import numpy as np
import pandas as pd
import json

# Load the dataset
dataset = pd.read_csv('Crop and fertilizer dataset.csv')

# Load the trained model
model = pickle.load(open('crop_fertilizer_model1.pkl', 'rb'))

# Placeholder function for crop and fertilizer prediction
def predict_crop_and_fertilizer(city, soil_type):
    # Filter the dataset to get the relevant rows based on city and soil type
    selected_rows = dataset[(dataset['District_Name'] == city) & (dataset['Soil_color'] == soil_type)]
    
    if len(selected_rows) == 0:
        return {
            'crop': 'No Data',
            'fertilizer': 'No Data',
            'nitrogen': 'No Data',
            'phosphorus': 'No Data',
            'potassium': 'No Data',
            'rainfall': 'No Data',
            'pH': 'No Data',
            'link': 'No Link'
        }
    
    # Extract the first row from the filtered dataset
    selected_row = selected_rows.iloc[0]
    
    # Extract the predicted crop, fertilizer, and link
    crop = selected_row['Crop']
    fertilizer = selected_row['Fertilizer']
    link = selected_row['Link']
    
    # Extract the nutrient values, rainfall, and pH from the dataset
    nitrogen = selected_row['Nitrogen']
    phosphorus = selected_row['Phosphorus']
    potassium = selected_row['Potassium']
    rainfall = selected_row['Rainfall']
    pH = selected_row['pH']
    
    return {
        'crop': crop,
        'fertilizer': fertilizer,
        'nitrogen': nitrogen,
        'phosphorus': phosphorus,
        'potassium': potassium,
        'rainfall': rainfall,
        'pH': pH,
        'link': link
    }

def main():
    # Load background image
    def load_background_image(image_file):
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{encoded_string}"

    st.title("City and Soil Selection")

    # Set background image
    background_image = load_background_image("images/back.jpg")
    st.markdown(
        f"""
        <style>
            .reportview-container {{
                background: url("{background_image}");
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Get city and soil type from the frontend
    city = st.selectbox("Select a City:", dataset['District_Name'].unique())
    soil_type = st.selectbox("Select Soil Type:", dataset['Soil_color'].unique())
    
    # Predict crop and fertilizer
    prediction = predict_crop_and_fertilizer(city, soil_type)
    
    # Display prediction result
    st.write("Predicted Crop:", prediction['crop'])
    st.write("Predicted Fertilizer:", prediction['fertilizer'])
    st.write("Nitrogen:", prediction['nitrogen'])
    st.write("Phosphorus:", prediction['phosphorus'])
    st.write("Potassium:", prediction['potassium'])
    st.write("Rainfall:", prediction['rainfall'])
    st.write("pH:", prediction['pH'])
    st.write("Link:", prediction['link'])

if __name__ == '__main__':
    main()
