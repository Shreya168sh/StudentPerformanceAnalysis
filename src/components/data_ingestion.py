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

    def initiate_data_ingestion(self, dataset_path):
        '''
        This method is responsible for Data Ingestion.
        '''
        logging.info("Data Ingestion Initialised...")
        try:
            logging.info('Reading the CSV Dataset as Dataframe')

            # Reading csv dataset as a pandas dataframe
            df = pd.read_csv(dataset_path)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            # Splitting dataset into training set and testing set
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
    