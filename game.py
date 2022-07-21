import random

import streamlit as st
from utils import read_df

st.set_page_config(page_title="pyvocab", layout="wide")

if "correct_streak" not in st.session_state:
    st.session_state.correct_streak = 0


if "words" not in st.session_state:
    st.session_state.words = read_df("words.csv")

if "distractors" not in st.session_state:
    st.session_state.distractors = read_df("distractors.csv")

words = st.session_state.words
distractors = st.session_state.distractors

this_word = words.sample()

st.write("#")
st.write("#")

st.write(" ## *" + this_word["definition"].iloc[0].strip() + "*")

st.write("#")
st.write("#")

other_words = words.sample(n=5)


other_words = distractors[distractors["word"] == this_word["word"].iloc[0]][
    "distractors"
].to_list()[0]

correct_word = this_word["word"].iloc[0]

choices = other_words
choices.append(correct_word)

random.shuffle(choices)

this_def = this_word["definition"].iloc[0].strip()


def common_callback(idx):
    if choices.index(correct_word) == idx:
        st.session_state.correct_streak += 1
        if st.session_state.correct_streak > 3:
            n_stars = int(st.session_state.correct_streak / 5) + 1
            st.success(
                f"# Correct! \n You got {st.session_state.correct_streak} right in a row! "
                + n_stars * "⭐️"
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
