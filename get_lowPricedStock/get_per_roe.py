import pandas as pd
import os
import requests


def get_per_roe(df):
    df["per"] = 0
    df["roe"] = 0
    for i in range(len(df)):
        print("getting {} information....".format(df.loc[i]["name"]))
        url = "https://finance.naver.com/item/main.nhn?code=" + df.loc[i]["code"]
        req = requests.get(url)
        tmp_df = pd.read_html(req.text)[3]
        try:
            lista = tmp_df.values.tolist()
            df.loc[i, "per"] = float(lista[5][3])
            df.loc[i, "roe"] = float(lista[10][3])
        except:
            print("no information at {}".format(df.loc[i]["name"]))
            df.loc[i, "per"] = float("inf")
            df.loc[i, "roe"] = -float("inf")
    return df


def get_sorted(df):
    print("sorting")
    tmp_df = df.sort_values(by=["per"])
    step = [i for i in range(len(tmp_df))]
    tmp_df["per_sort"] = step
    tmp_df = tmp_df.sort_values(by=["roe"], ascending=True)
    tmp_df["roe_sort"] = step
    tmp_df["sort"] = tmp_df["per_sort"] + tmp_df["roe_sort"]
    tmp_df = tmp_df.sort_values(by=["sort"])
    return tmp_df


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(path + "/krx.csv", index_col=0, dtype="str")
    df = get_per_roe(df)
    df = get_sorted(df)
    df.to_csv(path + "/sorted_krx.csv")
