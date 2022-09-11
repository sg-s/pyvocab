import os

from pycore.core import check_type

from pyvocab.utils import build_distractor_db, read_df


def test_words():
    """checks the word db and distractors"""

    if not os.path.exists("distractors.csv"):
        build_distractor_db()
    distractors = read_df("distractors.csv")

    words = read_df("words.csv")

    for _, row in words.iterrows():
        word = row["word"]

        other_words = distractors[distractors["word"] == word]["distractors"].to_list()[
            0
        ]

        check_type(other_words, list)
        assert len(other_words) == 5, f"Wrong length of distractors for {word}"
