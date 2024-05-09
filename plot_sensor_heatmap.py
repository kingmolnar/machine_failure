#!/usr/bin/env python3
TITLE = r"""
  ____                              _   _            _     __  __             
 / ___|  ___ _ __  ___  ___  _ __  | | | | ___  __ _| |_  |  \/  | __ _ _ __  
 \___ \ / _ \ '_ \/ __|/ _ \| '__| | |_| |/ _ \/ _` | __| | |\/| |/ _` | '_ \ 
  ___) |  __/ | | \__ \ (_) | |    |  _  |  __/ (_| | |_  | |  | | (_| | |_) |
 |____/ \___|_| |_|___/\___/|_|    |_| |_|\___|\__,_|\__| |_|  |_|\__,_| .__/ 
                                                                       |_|                                                             
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

def main():
    print(TITLE)
    df = load_data()
    for col in ['S5', 'S8', 'S13', 'S15', 'S17', 'S16', 'S19', 'S18']:
        print(f"Plotting Sensor: {col}")
        sensor_matrix = pd.pivot_table(df.sort_values(['DATE', 'ID']),
                                    index='DATE', columns='ID', values=col, aggfunc='max').values
        # print(sensor_matrix.shape)
        fig = plt.figure(figsize=(15, 6))
        plt.imshow(sensor_matrix.T, interpolation=None, cmap='jet')
        plt.xlabel(f'Date [{df.DATE.min()} to {df.DATE.max()}]')
        plt.xticks([])
        plt.ylabel(f'Device ID [{df.ID.min()} to {df.ID.max()}]')
        plt.yticks([])
        plt.colorbar()
        plt.title(f"Sensor {col}")
        fig.savefig(jp(FIG_DIR, f'{FNAME}_{col}.png',), transparent=True)
        plt.close()


if __name__ == '__main__':
    main()