import numpy as np
import pandas as pd
from typing import Union, List, Optional

def create_time_features(
    df: pd.DataFrame,
    date_column: str
) -> pd.DataFrame:
    """Create time-based features from datetime column."""
    df = df.copy()
    df['hour'] = df[date_column].dt.hour
    df['dayofweek'] = df[date_column].dt.dayofweek
    df['quarter'] = df[date_column].dt.quarter
    df['month'] = df[date_column].dt.month
    df['year'] = df[date_column].dt.year
    df['dayofyear'] = df[date_column].dt.dayofyear
    return df

def create_lag_features(
    series: Union[pd.Series, pd.DataFrame],
    lags: List[int]
) -> pd.DataFrame:
    """Create lag features from time series data."""
    df = pd.DataFrame(series.copy())
    for lag in lags:
        df[f'lag_{lag}'] = df.shift(lag)
    return df

def create_rolling_features(
    series: Union[pd.Series, pd.DataFrame],
    windows: List[int],
    functions: List[str] = ['mean', 'std']
) -> pd.DataFrame:
    """Create rolling window features."""
    df = pd.DataFrame(series.copy())
    for window in windows:
        for func in functions:
            df[f'rolling_{window}_{func}'] = df.rolling(
                window=window
            ).agg(func)
    return df