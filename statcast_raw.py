import os
from pybaseball import statcast, cache
import pandas as pd


def statcast_raw():
    cache.enable()

    statcast_raw = statcast(start_dt="2020-01-01", end_dt="2024-12-31")

    cwd = os.getcwd()
    raw_csvs = "raw_csvs"
    path = os.path.join(cwd, raw_csvs)
    os.makedirs(path, exist_ok=True)
    file = os.path.join(path, "statcast_raw.csv")

    statcast_raw.to_csv(file, index=False)


if __name__ == "__main__":
    statcast_raw()
