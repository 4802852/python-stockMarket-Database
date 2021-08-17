import pandas as pd
import os
import requests


def get_data(df):
    for i in range(len(df)):
        print("getting {} information....".format(df.loc[i]["name"]))
        url = "https://finance.naver.com/item/main.nhn?code=" + df.loc[i]["code"]
        req = requests.get(url)
        tmp_df = pd.read_html(req.text)[3]
        tmp = list(tmp_df.columns)
        tmp_columns = []
        for data in tmp:
            tmp_columns.append(data[1])
        tmp_df.columns = tmp_columns
        tmp_df.set_index('주요재무정보', drop=True, inplace=True)
        print(tmp_df.loc['PER(배)', tmp_columns[4]])
        
    return df


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(path + "/krx.csv", index_col=0, dtype="str")
    df = get_data(df)
    df.to_csv(path + "/merged_krx.csv")
