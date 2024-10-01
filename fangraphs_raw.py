import os
import pandas as pd

def fangraphs_raw():
    read_directory = 'fangraphs_htmls'
    write_directory = 'raw_csvs'
    write_file = os.path.join(write_directory, 'fangraphs_injuries_raw.csv')

    file_list = sorted(os.listdir(read_directory))

    REMOVE_UNDISCLOSED = True
    if REMOVE_UNDISCLOSED:
        file_list = [name for name in file_list if 'undisclosed' not in name]

    first = True
    for file in file_list:
        filename = os.fsdecode(file)

        to_read = os.path.join(read_directory, filename)

        raw_list_of_df = pd.read_html(to_read)

        list_of_df = [ele for ele in raw_list_of_df if "Name" == ele.columns[0]][::2]

        df = pd.concat(list_of_df)

        lamb = lambda x: x.split()[-1] + ', ' + x.rsplit(' ', 1)[0]
        df['player_name'] = df['Name'].apply(lamb)
        col = list(df.columns)

        col.insert(0, col.pop())
        df = df[col]

        injury_type = filename.strip('.html').split('_')[1]
        df['injury_type'] = injury_type

        df = df[df['Pos'].notna()]
        df = df[df['Pos'].str.endswith('P', na=False)]

        df = df.drop(['Name'], axis=1)
        cols = list(df.columns)
        col = [cols[0]] + [cols[-1]] + cols[1:-1]
        df = df[col]

        if first:
            full_df = df
            first = False

        else:
            full_df = pd.concat([full_df, df])

    full_df.to_csv(write_file, index=False)


if __name__ == '__main__':
    fangraphs_raw()


