import os
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "data.csv")


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "proprocessor.pkl")


@dataclass
class ModelTrainerConfig: 
    trained_model_path = os.path.join("artifacts", "model.pkl")
