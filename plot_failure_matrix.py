#!/usr/bin/env python3
TITLE = r"""
  _____     _ _                  __  __       _        _      
 |  ___|_ _(_) |_   _ _ __ ___  |  \/  | __ _| |_ _ __(_)_  __
 | |_ / _` | | | | | | '__/ _ \ | |\/| |/ _` | __| '__| \ \/ /
 |  _| (_| | | | |_| | | |  __/ | |  | | (_| | |_| |  | |>  < 
 |_|  \__,_|_|_|\__,_|_|  \___| |_|  |_|\__,_|\__|_|  |_/_/\_\
                                                              
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
    failure_matrix = pd.pivot_table(df.sort_values(['DATE', 'ID']),
                                index='DATE', columns='ID', values='EQUIPMENT_FAILURE', aggfunc='max').values
    # print(failure_matrix.shape)
    fig = plt.figure(figsize=(15, 6))
    plt.imshow(failure_matrix.T, interpolation=None, cmap='terrain')
    plt.xlabel(f'Date [{df.DATE.min()} to {df.DATE.max()}]')
    plt.xticks([])
    plt.ylabel(f'Device ID [{df.ID.min()} to {df.ID.max()}]')
    plt.yticks([])
    plt.title("Failure Matrix")
    fig.savefig(jp(FIG_DIR, f'{FNAME}.png',), transparent=True)
    plt.close()


if __name__ == '__main__':
    main()