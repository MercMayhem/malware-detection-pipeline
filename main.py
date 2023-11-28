from malwareDetection import logger
from malwareDetection.pipeline.model_pusher_pipeline import ModelPusherPipeline
from malwareDetection.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from malwareDetection.pipeline.data_validation_pipeline import DataValidationPipeline
from malwareDetection.pipeline.data_transformation_pipeline import DataTransformationPipeline
from malwareDetection.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
import sys
from malwareDetection.pipeline.model_training_pipeline import ModelTrainingPipeline

logger.info("============ STARTING PIPELINE ===============")

try:
    logger.info("Stage 1 - Data Ingestion starting ")
    ingest = DataIngestionPipeline()
    ingest.run()
    logger.info("Stage 1 - Data Ingestion ended")
except Exception as e:
    logger.exception(f"ERROR: {e}")
    sys.exit(1)

try:
    logger.info("Stage 2 - Data Validation starting ")
    validator = DataValidationPipeline()
    validator.run()
    logger.info("Stage 2 - Data Validation ended")
except Exception as e:
    logger.exception(f"ERROR: {e}")
    sys.exit(1)

try:
    logger.info("Stage 3 - Data Transformation starting ")
    transformer = DataTransformationPipeline()
    transformer.run()
    logger.info("Stage 3 - Data Transformation ended")
except Exception as e:
    logger.exception(f"ERROR: {e}")
    sys.exit(1)

try:
    logger.info("Stage 4 - Model Training starting")
    trainer = ModelTrainingPipeline()
    trainer.run()
    logger.info("Stage 4 - Model Training ended")

except Exception as e:
    logger.exception(f"ERROR: {e}")
    sys.exit(1)

try:
    logger.info("Stage 5 - Model Evaluation starting ")
    obj = ModelEvaluationPipeline()
    obj.run()
    logger.info("Stage 5 - Model Evaluation ended")
except Exception as e:
    logger.info(f"ERROR: {e}")
    sys.exit(1)

try:
    logger.info("Stage 6 - Model Pusher starting ")
    obj = ModelPusherPipeline()
    obj.run()
    logger.info("Stage 6 - Model Pusher ended")
except Exception as e:
    logger.info(f"ERROR: {e}")
    sys.exit(1)

logger.info("============ ENDING PIPELINE ===============")
