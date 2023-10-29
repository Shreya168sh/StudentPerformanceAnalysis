from fastapi import FastAPI, HTTPException, status, Response
import uvicorn
from pydantic import BaseModel
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


app = FastAPI()


class InputData(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: int
    writing_score: int


@app.get('/')
def index():
    return {'detail': 'Not found'}


@app.post('/prediction')
def predict(request: InputData):
    data = CustomData(
        gender = request.gender,
        race_ethnicity= request.race_ethnicity,
        parental_level_of_education = request.parental_level_of_education,
        lunch = request.lunch,
        test_preparation_course = request.test_preparation_course,
        reading_score = request.reading_score,
        writing_score = request.writing_score
    )

    preds_df = data.get_data_as_dataframe()
    print(f"preds_df: {preds_df}")

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(preds_df)
    return {"Predicted Maths Score": results[0]}


if __name__ == "__main__":
    uvicorn.run("application:app", host='127.0.0.1', port=8084)
