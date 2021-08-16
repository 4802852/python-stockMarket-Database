from get_krx import *
from get_per_roe import *
import os


def main():
    df = get_krx()
    df = get_per_roe(df)
    df = get_sorted(df)
    path = os.path.dirname(os.path.abspath(__file__))
    df.to_csv(path + "/sorted_krx.csv")


if __name__ == "__main__":
    main()
