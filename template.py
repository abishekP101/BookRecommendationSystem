import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "book_recommendation_system"

list_of_files = [
    # Root files
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "README.md",

    # Package init
    f"{project_name}/__init__.py",

    # Components (stages)
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/stage_00_data_ingestion.py",
    f"{project_name}/components/stage_01_data_validation.py",
    f"{project_name}/components/stage_02_data_transformation.py",
    f"{project_name}/components/stage_03_model_trainer.py",
    f"{project_name}/components/stage_04_model_evaluation.py",
    f"{project_name}/components/stage_05_model_deployment.py",

    # config
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",

    # constants
    f"{project_name}/constant/__init__.py",

    # entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",

    # exception
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception_handler.py",

    # logger
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/log.py",

    # pipeline
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/util.py",

    # recommender
    f"{project_name}/recommender/__init__.py",
    f"{project_name}/recommender/inference.py",
    f"{project_name}/recommender/recbole_config/lightgcn.yaml",

    # data folders
    f"{project_name}/data/raw/.gitkeep",
    f"{project_name}/data/processed/.gitkeep",

    # model saving
    f"{project_name}/recommender/model/.gitkeep",

    # notebooks
    "notebooks/.gitkeep"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass

    logging.info(f"Created: {filepath}")
