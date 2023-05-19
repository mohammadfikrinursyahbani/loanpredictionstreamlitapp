import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model_xgb.pkl')

# Define the predict function
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    data = {'Pregnancies': [Pregnancies],
            'Glucose': [Glucose],
            'BloodPressure': [BloodPressure],
            'SkinThickness': [SkinThickness],
            'Insulin': [Insulin],
            'BMI': [BMI],
            'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
            'Age': [Age]}
    
    features = pd.DataFrame(data)
    
    prediction = model.predict(features)
    return prediction[0]

# Create a Streamlit app
def app():
    st.title('Diabetes Prediction')

    st.write('Enter the following details to predict whether you have diabetes or not.')

    # Create input fields for the user to enter the details
    pregnancies = st.slider('Pregnancies', 0, 17, 0)
    glucose = st.slider('Glucose', 0, 199, 70)
    blood_pressure = st.slider('Blood Pressure', 0, 122, 70)
    skin_thickness = st.slider('Skin Thickness', 0, 99, 20)
    insulin = st.slider('Insulin', 0, 846, 79)
    bmi = st.slider('BMI', 0.0, 67.1, 20.0)
    diabetes_pedigree_function = st.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725)
    age = st.slider('Age', 21, 81, 33)

    # Check if any input field is empty
    if glucose == 0 or blood_pressure == 0 or skin_thickness == 0 or insulin == 0 or bmi == 0.0 or diabetes_pedigree_function == 0.0 or age == 0:
        st.write('Not allowed to enter a value of 0 except for pregnancies.')
    else:
        # Call the predict function and display the result
        if st.button('Predict'):
            result = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
            if result == 0:
                st.write('You do not have diabetes.')
            else:
                st.write('You have diabetes.')

if __name__ == '__main__':
    app()
