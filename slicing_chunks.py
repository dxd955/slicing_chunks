import pandas as pd
from datetime import datetime as dt


def slicing_chunk(input_df: pd.DataFrame, chunk_size: int):
    if chunk_size <= 0:
        raise ValueError('Work with Positive Numbers Only')
    star_indx = 0
    end_indx = 1
    preval = input_df.iloc[star_indx]["dt"]
    while True:
        if end_indx == input_df.size:
            yield input_df.iloc[star_indx:end_indx]
            break
        if input_df.iloc[end_indx]["dt"] != preval and chunk_size <= (end_indx - star_indx):
            yield input_df.iloc[star_indx:end_indx]
            star_indx = end_indx
        preval = input_df.iloc[end_indx]["dt"]
        end_indx += 1


def main():
    dfs = pd.date_range(
        "2023-01-01 00:00:00",
        "2023-01-01 00:00:05",
        freq="s"
    )
    df = pd.DataFrame({"dt": dfs.repeat(3)})
    df.head(10)

    for chunk in slicing_chunk(df, 4):
        print(chunk[::]["dt"].dt.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    main()