import random
from pathlib import Path

import pandas as pd

import streamlit as st

if "correct_streak" not in st.session_state:
    st.session_state.correct_streak = 0


def get_file_loc():
    """get a path to the words.txt file"""
    path = Path(__file__)
    path = (path.parent).joinpath("words.txt")
    return path


def read():
    """reads the words into a dataframe"""

    file_loc = get_file_loc()
    words = pd.read_csv(file_loc, sep="\t", header=0)

    words.sort_values("word", inplace=True)
    words.word = words.word.str.lower()
    words.word = words.word.str.strip()
    return words


words = read()

this_word = words.sample()

st.write("#")
st.write("#")
st.write("#")

st.write(" ## *" + this_word["definition"].iloc[0].strip() + "*")

st.write("#")
st.write("#")

other_words = words.sample(n=5)


correct_word = this_word["word"].iloc[0]

choices = list(other_words["word"])
choices.append(correct_word)

random.shuffle(choices)

this_def = this_word["definition"].iloc[0].strip()


def common_callback(idx):
    if choices.index(correct_word) == idx:
        st.session_state.correct_streak += 1
        if st.session_state.correct_streak > 3:
            st.success(
                f"# Correct! \n You got {st.session_state.correct_streak } right in a row!"
            )
        else:
            st.success("# Correct!")

    else:
        st.error(f"# Wrong! \n Correct answer is \n ## {correct_word} : \n {this_def}")
        st.session_state.correct_streak = 0


col1, col2, col3 = st.columns(3)

with col1:
    st.button(choices[0], on_click=common_callback, args=(0,))
    st.button(choices[1], on_click=common_callback, args=(1,))


with col2:
    st.button(choices[2], on_click=common_callback, args=(2,))
    st.button(choices[3], on_click=common_callback, args=(3,))

with col3:
    st.button(choices[4], on_click=common_callback, args=(4,))
    st.button(choices[5], on_click=common_callback, args=(5,))
