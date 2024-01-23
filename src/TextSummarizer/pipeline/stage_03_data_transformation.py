from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.stage_03_data_transformation import DataTransformation
from TextSummarizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()

'''
data_transformation = DataTransformationTrainingPipeline()
data_transformation.main()
'''