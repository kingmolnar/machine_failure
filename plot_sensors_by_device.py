#!/usr/bin/env python3
TITLE = r"""
  ____                                  _             ____             _          
 / ___|  ___ _ __  ___  ___  _ __ ___  | |__  _   _  |  _ \  _____   _(_) ___ ___ 
 \___ \ / _ \ '_ \/ __|/ _ \| '__/ __| | '_ \| | | | | | | |/ _ \ \ / / |/ __/ _ \
  ___) |  __/ | | \__ \ (_) | |  \__ \ | |_) | |_| | | |_| |  __/\ V /| | (_|  __/
 |____/ \___|_| |_|___/\___/|_|  |___/ |_.__/ \__, | |____/ \___| \_/ |_|\___\___|
                                              |___/                               
"""
from typing import List, Tuple, Set, Dict, Union, Any


from project_lib import (
    jp,
    DATAFILE,
    FIG_DIR,
    load_data,
)

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

FNAME = os.path.basename(__file__).replace('plot_', '').replace('.py', '')
FIG_PATH = jp(FIG_DIR, FNAME)
os.makedirs(FIG_PATH, exist_ok=True)

def main():
    print(TITLE)
    df = load_data()

    sensor_cols = ['S5', 'S8', 'S13', 'S15', 'S17', 'S16', 'S19', 'S18']
    n_sensor = len(sensor_cols)

    for ID in df.ID.drop_duplicates():
        print(f"Device: {ID}")

        subdf = df[df.ID==ID].sort_values('DATE').copy()
        subdf['row_num'] = range(1, subdf.shape[0]+1)
        faildf = subdf[subdf.EQUIPMENT_FAILURE==1]
        # x = subdf.DATE.values
        x = subdf.row_num.values
        x_f = faildf.row_num.values
        # y = np.ones(len(x_f))
        # z = subdf.EQUIPMENT_FAILURE.values * 1.0
        fig = plt.figure(figsize=(12,10))
        plt.title(f"Device {ID}")
        for j, sc in enumerate(sensor_cols):
            y = subdf[sc].values
            plt.subplot(n_sensor, 1, j+1)
            plt.plot(x, y)
            y_max = y.max()
            y_min = y.min()
            plt.vlines(x_f, y_min, y_max,  color='red')
            if j==0:
                plt.title(f"Device {ID}")
            plt.tick_params(
                axis='x',          # changes apply to the x-axis
                which='both',      # both major and minor ticks are affected
                bottom=False,      # ticks along the bottom edge are off
                top=False,         # ticks along the top edge are off
                labelbottom=False) # labels along the bottom edge are off
            plt.ylabel(sc)
            
        fig.savefig(jp(FIG_PATH, f"device_{ID}.png"), transparent=True)
        plt.close()


if __name__ == '__main__':
    main()
