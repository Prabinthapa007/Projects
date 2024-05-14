import pickle
import streamlit as st
import numpy as np

def get_save_file(file_path:str):
    with open(file_path, "rb") as file:
        output = pickle.load(file)

    return output

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
    st.title("Hello Everyone !")

    age = st.number_input("Enter Age", value=5, min_value=5, max_value=100, step=1)
    cigsPerDay = st.number_input("Enter Cigarettes Per Day", value=0, min_value=0, max_value=100, step=1)
    BPMeds = st.number_input("Enter BP Medicines", value=0, min_value=0, max_value=1, step=1)
    prevalentStroke = st.number_input("Enter Prevalent Strokes", value=0, min_value=0, max_value=1, step=1)
    diabetes =  st.number_input("Enter Diabetes Patient or not", value=0, min_value=0, max_value=1, step=1)
    totChol = st.number_input("Enter Cholestrol Level", value=50, min_value=50, max_value=600, step=1)
    sysBP = st.number_input("Enter Systolic Blood Pressure", value=0, min_value=0, max_value=300, step=1)
    BMI = st.number_input("Enter BMI", value=10, min_value=10, max_value=50, step=1)  
    heartRate = st.number_input("Enter Heart Rate", value=0, min_value=0, max_value=200, step=1)
    glucose = st.number_input("Enter Glucose Level", value=50, min_value=50, max_value=500, step=1)
    male = st.number_input("Enter 1 if you are male", value=0, min_value=0, max_value=1, step=1)
    female = st.number_input("Enter 1 if you are female", value=0, min_value=0, max_value=1, step=1)

    user_input = np.array([[age, cigsPerDay, BPMeds, prevalentStroke, diabetes, heartRate, totChol, BMI, glucose, sysBP, male, female]])

    if st.button("Predict"):
        st.write(
            f"Coronary Disease chance: {prediction(user_input)}"
        )
