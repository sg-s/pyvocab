from pathlib import Path

import numpy as np
import pandas as pd


def get_file_loc():
    """get a path to the words.txt file"""
    path = Path(__file__)
    path = (path.parent).joinpath("words.txt")
    return path


def read():
    """reads the words into a dataframe"""

    file_loc = get_file_loc()
    words = pd.read_csv(file_loc, sep="|", header=0)

    words.sort_values("word", inplace=True)
    words.word = words.word.str.lower()
    words.word = words.word.str.strip()
    return words
