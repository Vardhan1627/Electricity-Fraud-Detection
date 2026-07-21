from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
MODEL_DIR = BASE_DIR / "models"
DATA_FILE = RAW_DATA_DIR / "client_data.csv"
MODEL_FILE = MODEL_DIR / "fraud_model.pkl"
FEATURE_COLUMNS_FILE = MODEL_DIR / "feature_columns.pkl"
