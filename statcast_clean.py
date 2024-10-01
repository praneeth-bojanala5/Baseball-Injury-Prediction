import os
import pandas as pd


def statcast_clean():
    read_directory = 'raw_csvs'
    read_file = 'statcast_raw.csv'
    write_directory = 'cleaned_csvs'
    write_file = 'statcast_cleaned.csv'

    path = os.path.join(read_directory, read_file)

    relevant_attributes = ['player_name',
                           'pitcher',
                           'game_date',
                           'game_pk',
                           'at_bat_number',
                           'pitch_number',
                           'pitch_type',
                           'pitch_name',
                           'release_speed',
                           'release_pos_x',
                           'release_pos_z',
                           'zone',
                           'p_throws',
                           'type',
                           'pfx_x',
                           'pfx_z',
                           'plate_x',
                           'plate_z',
                           'vx0',
                           'vy0',
                           'vz0',
                           'ax',
                           'ay',
                           'az',
                           'sz_top',
                           'sz_bot',
                           'effective_speed',
                           'release_spin_rate',
                           'release_extension',
                           'release_pos_y',
                           'spin_axis',
                           ]

    df = pd.read_csv(path)

    df = df[relevant_attributes]
    df = df.reindex(index=df.index[::-1])

    df['pitch_of_game'] = df.groupby('game_pk').cumcount() + 1

    col = list(df.columns)
    col.insert(4, col.pop())
    df = df[col]

    df = df[df['release_speed'].notna()]

    to_write = os.path.join(write_directory, write_file)

    df.to_csv(to_write, index=False)


if __name__ == '__main__':
    statcast_clean()
