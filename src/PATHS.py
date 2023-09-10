from pathlib import Path
import os

SRC_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = SRC_PATH.parents[0]

DATA_PATH = PROJECT_PATH / "data"
RAW_DATA_PATH = DATA_PATH / "raw"
GAN_DATASET_PATH = DATA_PATH / "gan_dataset"

MODELS_PATH = PROJECT_PATH / "models"

MODELS_METRICS_CSV = MODELS_PATH / "intrinsic_metrics.csv"
CLASSIFIERS_EVALUATION_METRICS_CSV = MODELS_PATH / "classifiers_evaluation_metrics.csv"
CLASSIFIER_VALIDATION_METRICS_CSV = MODELS_PATH / "classifier_validation_metrics.csv"
