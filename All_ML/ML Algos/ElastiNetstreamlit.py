import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("pickleFiles/ElastiNetmodel.pkl", "rb") as f:
    model = pickle.load(f)

# Set the title of the app
st.title("ML Model Prediction App")

# Provide a brief description
st.write("Enter the features below to get a prediction.")

# Create input widgets for each feature
feature0 = st.number_input("Enter value for feature 0", value=0.0)
feature1 = st.number_input("Enter value for feature 1", value=0.0)
feature2 = st.number_input("Enter value for feature 2", value=0.0)
feature3 = st.number_input("Enter value for feature 3", value=0.0)
feature4 = st.number_input("Enter value for feature 4", value=0.0)
feature5 = st.number_input("Enter value for feature 5", value=0.0)
feature6 = st.number_input("Enter value for feature 6", value=0.0)
feature7 = st.number_input("Enter value for feature 7", value=0.0)
feature8 = st.number_input("Enter value for feature 8", value=0.0)
feature9 = st.number_input("Enter value for feature 9", value=0.0)

# When the button is clicked, run the prediction
if st.button("Predict"):
    # Arrange inputs in the format the model expects
    input_features = np.array([[feature0, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9]])
    
    # Run prediction using your model
    prediction = model.predict(input_features)
    
    # Display the prediction
    st.write("The prediction is:", prediction[0])
