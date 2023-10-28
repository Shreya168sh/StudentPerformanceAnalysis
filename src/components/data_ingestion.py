import pandas as pd
from sklearn.model_selection import train_test_split
import os
import sys
from src.exceptions import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from config import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        '''
        This method is responsible for Data Ingestion.
        '''
        logging.info("Data Ingestion Initialised...")
        try:
            logging.info('Reading the CSV Dataset as Dataframe')
            
            df = pd.read_csv("/home/shreya/work/mlproject/notebook/data/StudentsPerformance.csv")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed!")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    ingestion_obj = DataIngestion()
    train_data, test_data = ingestion_obj.initiate_data_ingestion()

    transformation_obj = DataTransformation()
    train_arr, test_arr, _ = transformation_obj.initiate_data_transformation(train_path=train_data, test_path=test_data)

    trainer_obj = ModelTrainer()
    print(trainer_obj.initiate_model_trainer(train_array=train_arr, test_array=test_arr))
