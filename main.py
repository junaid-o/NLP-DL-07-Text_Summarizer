from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
#from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
#from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
#from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from TextSummarizer.logger import logging
from TextSummarizer.exception import TextSummarizerException
import sys



STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise TextSummarizerException(e, sys) from e


