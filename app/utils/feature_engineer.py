import numpy as np
import pandas as pd



def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df["WaterCementRatio"] = df["Water"] / df["Cement"]
    df["TotalBinder"] = df["Cement"] + df["BlastFurnaceSlag"] + df["FlyAsh"]
    df["WaterBinderRatio"] = df["Water"] / df["TotalBinder"]
    df["TotalAggregate"] = df["CoarseAggregate"] + df["FineAggregate"]
    df["FineAggregateRatio"] = df["FineAggregate"] / df["TotalAggregate"]
    df["CoarseAggregateRatio"] = df["CoarseAggregate"] / df["TotalAggregate"]
    df["CementRatio"] = df["Cement"] / df["TotalBinder"]
    df["SCM"] = df["BlastFurnaceSlag"] + df["FlyAsh"]
    df["SCMPercentage"] = df["SCM"] / df["TotalBinder"]
    df["LogAge"] = np.log1p(df["Age"])
    return df


