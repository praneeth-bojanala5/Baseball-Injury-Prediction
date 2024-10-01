import os
import pandas as pd
from datetime import datetime


def not_valid_date(date_str):
    try:
        # Attempt to parse the date with the format
        datetime.strptime(date_str, '%m/%d/%y')
        return False  # Date is valid and in the correct format
    except ValueError:
        return True

def convert_date_format2(date_str):
    # Parse the date from the format "Mar '22"
    dt = datetime.strptime(date_str, "%m/%d/%y")
    # Format the date to "2022-03"
    formatted_date = dt.strftime("%Y-%m-%d")
    return formatted_date

def fangraphs_clean():

    read_directory = 'raw_csvs'
    read_file = 'fangraphs_injuries_raw.csv'
    read_path = os.path.join(read_directory, read_file)
    write_directory = 'cleaned_csvs'
    write_file = 'fangraphs_injuries_cleaned.csv'
    path = os.path.join(write_directory, write_file)

    df = pd.read_csv(read_path)

    df.drop(df[df['Injury / Surgery Date'].apply(not_valid_date)].index, inplace=True)
    single = lambda x: True if x in ['Guerra, Javy', 'Allen, Logan', 'Castillo, Luis', 'Webb, Jacob'] else False
    df.drop(df[df['player_name'].apply(single)].index, inplace=True)

    df['Injury / Surgery Date'] = df['Injury / Surgery Date'].map(convert_date_format2)

    df = df[['player_name', 'Injury / Surgery Date']]

    df.to_csv(path, index=False)



if __name__ == '__main__':
    fangraphs_clean()