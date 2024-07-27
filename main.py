from sensor.configuration.mongo_db_connection import MongoDBClient 
from sensor.exception import SensorException 
from sensor.logger import logging
import os,sys 
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig 
"""
def test_exception():
    try: 
        logging.info('We are dividing 1 by zero ')
        x = 1/0 
    except Exception as e:
        raise SensorException(e,sys)
"""
if __name__ == '__main__': 
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    """training_pipeline_config = TrainingPipelineConfig() 
    data_ingestion_config = DataIngestionConfig(training_pipeline_config= training_pipeline_config)
    print(data_ingestion_config.__dict__)"""
    
    
    """mongodb_client = MongoDBClient()
    print("collection name:",mongodb_client.database.list_collection_names()) """
    
""" try:
        test_exception()
    except Exception as e: 
        print(e)"""