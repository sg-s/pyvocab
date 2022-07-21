from pathlib import Path

import pandas as pd


def get_file_loc(filename: str):
    """get a path to the words.txt file"""
    path = Path(__file__)
    path = (path.parent).joinpath(filename)
    return path


def read_df(df_name: str):
    """reads the words into a dataframe"""

    file_loc = get_file_loc(df_name)
    words = pd.read_csv(
        file_loc, sep="|", header=0, converters={"distractors": pd.eval}
    )

    words.sort_values("word", inplace=True)
    words.word = words.word.str.lower()
    words.word = words.word.str.strip()
    return words


def save_df(df, name):
    """save some dataframe to disk"""

    path = get_file_loc(name)
    df.to_csv(path, index_label=False, sep="|")
