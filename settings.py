"""small module to allow GUI access to utility functions"""

import numpy as np
import pandas as pd
from Levenshtein import distance

import streamlit as st
from utils import read_df, save_df


def check_db():

    words = read_df("words.csv")

    bar = st.progress(0)

    bad_words = []

    for index, row in words.iterrows():

        percent_complete = int(index / len(words)) * 100

        bar.progress(percent_complete)

        if type(words["definition"][index]) == str:
            continue

        if np.isnan(row["definition"]):
            bad_words.append(row["word"])

    bar.progress(100)

    if len(bad_words) > 0:
        st.write(bad_words)
    else:
        st.success("database looks good!")


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
    bar = st.progress(0)

    words = read_df("words.csv")
    words = words["word"]

    distractors = []

    for i, word in enumerate(words):

        percent_complete = int(i / len(words) * 100)

        bar.progress(percent_complete)
        distractors.append(find_n_closest_words(word))
    bar.progress(100)

    distractors_db = dict()
    distractors_db["word"] = words
    distractors_db["distractors"] = distractors

    distractors_db = pd.DataFrame(distractors_db)

    st.write(distractors_db)

    save_df(distractors_db, "distractors.csv")


st.button("Check database", on_click=check_db)


st.button("Build distractor words DB", on_click=build_distractor_db)
