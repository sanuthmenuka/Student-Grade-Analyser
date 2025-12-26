import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('student_performance_model.pkl')

model = load_model()

# App title
st.title("🎓 Student Academic Performance Predictor")
st.write("Enter student information to predict academic performance score")

# Create input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.number_input("Age", min_value=15, max_value=25, value=19)
        study_hours = st.slider("Study Hours per Day", 0.0, 12.0, 5.0, 0.5)
        social_media = st.slider("Social Media Hours", 0.0, 12.0, 3.0, 0.5)
    
    with col2:
        sleep_hours = st.slider("Sleep Hours", 4.0, 12.0, 7.0, 0.5)
        attendance = st.slider("Attendance %", 0, 100, 85)
        part_time = st.selectbox("Part-time Job", ["Yes", "No"])

    submitted = st.form_submit_button("Predict Performance")

if submitted:
    # Create input dataframe
    input_data = pd.DataFrame([{
        "gender": gender,
        "age": age,
        "study_hours_per_day": study_hours,
        "social_media_hours": social_media,
        "sleep_hours": sleep_hours,
        "attendance_percentage": attendance,
        "part_time_job": part_time
    }])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"### Predicted Academic Performance: **{prediction:.2f}**")
    
    # Performance interpretation
    if prediction >= 85:
        st.balloons()
        st.info("🌟 Excellent performance predicted!")
    elif prediction >= 70:
        st.info("✅ Good performance predicted!")
    elif prediction >= 60:
        st.warning("⚠️ Average performance predicted!")
    else:
        st.error("📚 Below average - consider increasing study time!")