# frontend/app.py

import streamlit as st
import requests

API_URL = "http://backend:8000/predict"

st.set_page_config(page_title="Employee Attrition Predictor", layout="centered")
st.title("🔍 Employee Attrition Prediction App")
st.markdown("Fill in the details to predict whether an employee will leave.")

with st.form("prediction_form"):
    Age = st.slider("Age", 18, 65, 30)
    BusinessTravel = st.selectbox("Business Travel", [0, 1, 2])
    DailyRate = st.slider("Daily Rate", 100, 1500, 800)
    Department = st.selectbox("Department", [0, 1, 2])
    DistanceFromHome = st.slider("Distance From Home", 1, 30, 10)
    Education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
    EducationField = st.selectbox("Education Field", list(range(6)))
    EnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
    Gender = st.selectbox("Gender", [0, 1])
    HourlyRate = st.slider("Hourly Rate", 20, 200, 60)
    JobInvolvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
    JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    JobRole = st.selectbox("Job Role", list(range(9)))
    JobSatisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
    MaritalStatus = st.selectbox("Marital Status", [0, 1, 2])
    MonthlyIncome = st.slider("Monthly Income", 1000, 20000, 5000)
    MonthlyRate = st.slider("Monthly Rate", 1000, 30000, 15000)
    NumCompaniesWorked = st.slider("Num Companies Worked", 0, 10, 1)
    OverTime = st.selectbox("OverTime", [0, 1])
    PercentSalaryHike = st.slider("Percent Salary Hike", 0, 100, 15)
    PerformanceRating = st.selectbox("Performance Rating", [1, 2, 3, 4])
    RelationshipSatisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
    StockOptionLevel = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    TotalWorkingYears = st.slider("Total Working Years", 0, 40, 10)
    TrainingTimesLastYear = st.slider("Training Times Last Year", 0, 6, 3)
    WorkLifeBalance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
    YearsAtCompany = st.slider("Years at Company", 0, 40, 5)
    YearsInCurrentRole = st.slider("Years in Current Role", 0, 20, 3)
    YearsSinceLastPromotion = st.slider("Years Since Last Promotion", 0, 15, 2)
    YearsWithCurrManager = st.slider("Years with Current Manager", 0, 20, 3)

    submitted = st.form_submit_button("Predict")

if submitted:
    data = {
        "Age": Age,
        "BusinessTravel": BusinessTravel,
        "DailyRate": DailyRate,
        "Department": Department,
        "DistanceFromHome": DistanceFromHome,
        "Education": Education,
        "EducationField": EducationField,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "Gender": Gender,
        "HourlyRate": HourlyRate,
        "JobInvolvement": JobInvolvement,
        "JobLevel": JobLevel,
        "JobRole": JobRole,
        "JobSatisfaction": JobSatisfaction,
        "MaritalStatus": MaritalStatus,
        "MonthlyIncome": MonthlyIncome,
        "MonthlyRate": MonthlyRate,
        "NumCompaniesWorked": NumCompaniesWorked,
        "OverTime": OverTime,
        "PercentSalaryHike": PercentSalaryHike,
        "PerformanceRating": PerformanceRating,
        "RelationshipSatisfaction": RelationshipSatisfaction,
        "StockOptionLevel": StockOptionLevel,
        "TotalWorkingYears": TotalWorkingYears,
        "TrainingTimesLastYear": TrainingTimesLastYear,
        "WorkLifeBalance": WorkLifeBalance,
        "YearsAtCompany": YearsAtCompany,
        "YearsInCurrentRole": YearsInCurrentRole,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "YearsWithCurrManager": YearsWithCurrManager,
    }

    try:
        res = requests.post(API_URL, json=data)
        res_data = res.json()

        if "prediction" in res_data:
            prediction = res_data["prediction"]
            label = "Yes" if prediction == 1 else "No"
            st.success(f"🎯 Prediction: Employee Attrition = **{label}**")
        else:
            st.error("⚠️ Error: " + str(res_data))
    except Exception as e:
        st.error(f"❌ Could not connect to backend: {e}")
