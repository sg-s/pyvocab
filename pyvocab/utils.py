from pathlib import Path

import numpy as np
import pandas as pd
from Levenshtein import distance


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


def find_n_closest_words(target_word, n=5):
    """find  n closest words to word using the Levenstein distance"""

    words = read_df("words.csv")
    words = list(words["word"])

    # make a list of possible distractor words
    distractor_words = words

    # find distancs to all possible distractors
    distances = []
    for word in distractor_words:
        distances.append(distance(word, target_word))

    distances = np.array(distances)

    # reorder distractors by distance
    distractor_words = list(pd.Series(distractor_words)[np.argsort(distances)])

    distractor_words = distractor_words[1 : n + 1]
    return distractor_words


def build_distractor_db():

    words = read_df("words.csv")
    words = words["word"]

    distractors = []

    for i, word in enumerate(words):
        distractors.append(find_n_closest_words(word))

    distractors_db = dict()
    distractors_db["word"] = words
    distractors_db["distractors"] = distractors

    distractors_db = pd.DataFrame(distractors_db)

    save_df(distractors_db, "distractors.csv")
