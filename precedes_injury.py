import os
import pandas as pd


def precedes_injury(injury, df):
    df10 = df[df['player_name'] == injury['player_name']]

    df10 = df10[df10['game_date'] <= injury['Injury / Surgery Date']]
    max_columns = df10.max()

    close_date = max_columns['game_date']

    max_columns = df10[df10['game_date'] == close_date].max()

    last_pitch = max_columns['pitch_of_game']

    return injury['player_name'], close_date, last_pitch


def injuries_to_df():
    read_directory = "cleaned_csvs"
    statcast = pd.read_csv(os.path.join(read_directory, "statcast_cleaned.csv"))
    fangraphs = pd.read_csv(os.path.join(read_directory, "fangraphs_injuries_cleaned.csv"))

    statcast['game_precedes_injury'] = False
    i = 0
    for row in fangraphs.iterrows():
        print(i)
        i += 1
        injury = row[1]
        name, date, pitch = precedes_injury(injury, statcast)
        condition = (statcast['player_name'] == name) & (statcast['game_date'] == date)

        statcast.loc[condition, 'game_precedes_injury'] = True

    statcast['ID'] = pd.factorize(statcast[['player_name', 'game_date']].apply(tuple, axis=1))[0]

    statcast.to_csv('integrated_data.csv', index=False)

if __name__ == '__main__':
    injuries_to_df()
