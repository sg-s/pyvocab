"""small module to allow GUI access to utility functions"""

import numpy as np

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


st.button("Check database", on_click=check_db)


st.button("Build distractor words DB", on_click=build_distractor_db)
