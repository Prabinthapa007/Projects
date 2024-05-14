import pickle
import streamlit as st
import pandas as pd
import numpy as np

def get_save_file(file_path:str):
    with open(file_path, "rb") as file:
        output = pickle.load(file)
    
    return output

# Load the pre-trained scaler and model
best_scaler = get_save_file("best_model/standard_scaler.pkl")
best_model = get_save_file("best_model/Random_forest.pkl")


def prediction(user_input):
    model_output = best_model.predict(
        best_scaler.transform(
            user_input
        )
    )[0]
    return model_output

if __name__ == "__main__":
    st.title("Hello Everyone!")

    # Input fields
    age = st.number_input("Enter Age", value=5, min_value=5, max_value=100, step=1)
    cigsPerDay = st.number_input("Enter Cigarettes Per Day", value=0, min_value=0, max_value=100, step=1)
    BPMeds = st.number_input("Enter BP Medicines", value=0, min_value=0, max_value=1, step=1)
    prevalentStroke = st.number_input("Enter Prevalent Strokes", value=0, min_value=0, max_value=1, step=1)
    diabetes = st.number_input("Enter Diabetes Patient or not", value=0, min_value=0, max_value=1, step=1)
    totChol = st.number_input("Enter Cholesterol Level", value=50, min_value=50, max_value=600, step=1)
    sysBP = st.number_input("Enter Systolic Blood Pressure", value=0, min_value=0, max_value=300, step=1)
    BMI = st.number_input("Enter BMI", value=10, min_value=10, max_value=50, step=1)
    heartRate = st.number_input("Enter Heart Rate", value=0, min_value=0, max_value=200, step=1)
    glucose = st.number_input("Enter Glucose Level", value=50, min_value=50, max_value=500, step=1)
    gender = st.selectbox("Select Gender", options=["male", "female"])

    # Combine inputs into a dataframe
    user_input_dict = {
        'age': [age],
        'cigsPerDay': [cigsPerDay],
        'BPMeds': [BPMeds],
        'prevalentStroke': [prevalentStroke],
        'diabetes': [diabetes],
        'totChol': [totChol],
        'sysBP': [sysBP],
        'BMI': [BMI],
        'heartRate': [heartRate],
        'glucose': [glucose],
        'gender': [gender]
    }
    user_input_df = pd.DataFrame(user_input_dict)

    # Applying one-hot encoding to the gender column
    user_input_df = pd.get_dummies(user_input_df, columns=['gender'])

    # Ensuring all necessary columns are present
    required_columns = ['age', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'diabetes', 'totChol', 'sysBP', 'BMI', 'heartRate', 'glucose', 'gender_female', 'gender_male']
    for col in required_columns:
        if col not in user_input_df.columns:
            user_input_df[col] = 0

    # Reordering columns to match the training data
    user_input_df = user_input_df[required_columns]

    # Converting dataframe to numpy array
    user_input = np.array(user_input_df)

    # Displaying the user input before prediction
    st.write("User Input DataFrame:")
    st.write(user_input_df)

    if st.button("Predict"):
        result = prediction(user_input)
        st.write(f"Coronary Disease chance: {result}")
