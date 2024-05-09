#!/usr/bin/env python3
import os
import pandas as pd
DATA_FILE = "data/machine_failure_data.csv"
DATA_URL_1 = "https://raw.githubusercontent.com/shadgriffin/machine_failure/master/equipment_failure_data_1.csv"
DATA_URL_2 = "https://raw.githubusercontent.com/shadgriffin/machine_failure/master/equipment_failure_data_2.csv"

def download_data():
    if os.path.isfile(DATA_FILE):
        print(f"""
        The file `{DATA_FILE}` already exists!
        Please remove this file if you need to download
        the data again.
        """)
        return

    # Make sure directory for data exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # Download raw data
    pd_data_1 = pd.read_csv(DATA_URL_1, sep=",", header=0)
    pd_data_2 = pd.read_csv(DATA_URL_2, sep=",", header=0)
    pd_data=pd.concat([pd_data_1, pd_data_2])
    print(f"Number of rows: {pd_data.shape[0]:,}")
    print(f"Number of columns: {pd_data.shape[1]:,}")
    cols = ['ID', 'DATE', 'REGION_CLUSTER', 'MAINTENANCE_VENDOR', 'MANUFACTURER',
           'WELL_GROUP', 'AGE_OF_EQUIPMENT', 'S5', 'S8', 'S13',
            'S15', 'S17',  'S16', 'S19', 'S18', 'EQUIPMENT_FAILURE']

    # One data entry per day for each device. Ensure there are not duplicate entries
    pd_data.drop_duplicates(subset=['ID','DATE'], inplace=True)
    
    # Save combined data to single file
    pd_data[cols].to_csv(DATA_FILE, index=None)
    print(f"Data saved to: {DATA_FILE}")
        


if __name__ == '__main__':
    download_data()

