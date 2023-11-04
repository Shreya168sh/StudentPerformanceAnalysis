import sys
import os
import pandas as pd
from src.exceptions import CustomException
from src.utils import load_object
from config import DataIngestionConfig


class PredictPipeline:
    def __init__(self):
        self.base_path = DataIngestionConfig.base_path

    def predict(self, features):
        try:
            model_path = os.path.join(self.base_path, 'artifacts/model.pkl')
            preprocessor_path = os.path.join(self.base_path, 'artifacts/proprocessor.pkl')

            print(f"model path: {model_path}")
            print(f"preprocessor path: {preprocessor_path}")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            scaled_data = preprocessor.transform(features)
            preds = model.predict(scaled_data)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, gender: str,
                race_ethnicity: str,
                parental_level_of_education: str,
                lunch: str,
                test_preparation_course: str,
                reading_score: int,
                writing_score: int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        try:
            input_data_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score]
            }

            return pd.DataFrame(input_data_dict)
            
        except Exception as e:
            raise CustomException(e, sys)
