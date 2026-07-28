import joblib
from utils.validation import validate_input
from utils.feature_engineer import create_features
import pandas as pd
import numpy as np


model = joblib.load("models/concrete_strength_model.pkl")

def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = [
        "Cement",
        "BlastFurnaceSlag",
        "FlyAsh",
        "Water",
        "Superplasticizer",
        "CoarseAggregate",
        "FineAggregate",
        "Age",
    ]
    return df[required_columns]

def predict_strength(df: pd.DataFrame) -> np.ndarray:
    df = drop_columns(df)
    validate_input(df)
    df = create_features(df)
    prediction = model.predict(df)
    return prediction