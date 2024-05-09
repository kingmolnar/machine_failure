from typing import List, Set, Dict, Union
import os
jp = os.path.join
import datetime
T_now = datetime.datetime.now
import pandas as pd
from pandas import DataFrame, Series

THIS_DIR = os.path.dirname(__file__)

DATAFILE = '/data/IFI8410/equipment_failure/raw_data.csv'
IMG_DIR = jp(THIS_DIR, '..', 'imgs')
FIG_DIR = jp(THIS_DIR, '..', 'figs')

for d in [IMG_DIR, FIG_DIR]:
    os.makedirs(d, exist_ok=True)

def load_data() -> DataFrame:
    """Load dataset

    Returns:
        DataFrame: Pandas DataFrame of format:
            ID                      int64
            DATE                   object
            REGION_CLUSTER         object
            MAINTENANCE_VENDOR     object
            MANUFACTURER           object
            WELL_GROUP              int64
            AGE_OF_EQUIPMENT        int64
            S5                    float64
            S8                    float64
            S13                   float64
            S15                   float64
            S17                   float64
            S16                   float64
            S19                   float64
            S18                   float64
            EQUIPMENT_FAILURE       int64
    """
    print(f"Load: {DATAFILE}")
    df = pd.read_csv(DATAFILE)
    df['DATE'] = pd.to_datetime(df['DATE'], format="%m/%d/%y")
    print(f"Number of rows: {df.shape[0]:,}")
    print(f"Number of columns: {df.shape[1]:,}")
    ## print(df.dtypes)
    return df

