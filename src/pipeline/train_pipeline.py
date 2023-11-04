import pandas as pd
from sklearn.model_selection import train_test_split
import os
import sys
from src.exceptions import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from config import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig


class TrainPipeline:
    def __init__(self):
        self.ingestion_obj = DataIngestion()
        self.transformation_obj = DataTransformation()
        self.model_trainer = ModelTrainer()

    def train_model(self, dataset_path):
        try:
            train_data, test_data = self.ingestion_obj.initiate_data_ingestion(dataset_path=dataset_path)
            train_arr, test_arr, _ = self.transformation_obj.initiate_data_transformation(train_path=train_data, test_path=test_data)
            print(self.model_trainer.initiate_model_trainer(train_array=train_arr, test_array=test_arr))

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    # dataset_path = os.path.join(DataIngestionConfig.base_path, "notebooks/data/StudentsPerformance.csv")
    train_pipeline.train_model(dataset_path="/home/shreya/work/mlproject/StudentPerformanceAnalysis/notebooks/data/StudentsPerformance.csv")
