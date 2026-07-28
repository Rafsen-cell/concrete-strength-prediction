import pandas as pd

def validate_input(df: pd.DataFrame):
    """"
    Validate the input data before prediction.
    Raises ValueError if the input is invalid
    """

    required_columns = [
        'Cement',
        'BlastFurnaceSlag',
        'FlyAsh',
        'Water',
        'Superplasticizer',
        'CoarseAggregate',
        'FineAggregate',
        'Age'
    ]

    # Check missing columns
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required columns: {','.join(missing)}"
        )

    # Check negative values
    numeric_cols = required_columns
    if (df[numeric_cols] < 0) .any().any():
        raise ValueError(
            "Input contains negative values"
        )

    # Check age
    if (df["Age"] <= 0) .any():
        raise ValueError(
            "Age must be greater than 0 days"
        )
    return True