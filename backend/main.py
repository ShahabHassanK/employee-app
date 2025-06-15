# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

# Load the model and scaler
MODEL_PATH = os.path.join("models", "rf_model.pkl")
SCALER_PATH = os.path.join("models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Define the input schema (30 features only)
class InputData(BaseModel):
    Age: int
    BusinessTravel: int
    DailyRate: float
    Department: int
    DistanceFromHome: float
    Education: int
    EducationField: int
    EnvironmentSatisfaction: int
    Gender: int
    HourlyRate: float
    JobInvolvement: int
    JobLevel: int
    JobRole: int
    JobSatisfaction: int
    MaritalStatus: int
    MonthlyIncome: float
    MonthlyRate: float
    NumCompaniesWorked: int
    OverTime: int
    PercentSalaryHike: float
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: float
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: float
    YearsInCurrentRole: float
    YearsSinceLastPromotion: float
    YearsWithCurrManager: float

@app.get("/health")
def health_check():
    return {"status": "Backend is up and running!"}

@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input to NumPy array
        input_dict = data.dict()
        input_values = list(input_dict.values())
        input_array = np.array(input_values).reshape(1, -1)

        # Scale input
        scaled_input = scaler.transform(input_array)

        # Predict
        prediction = model.predict(scaled_input)[0]

        return {"prediction": int(prediction)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
