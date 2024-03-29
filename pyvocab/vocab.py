"""A python-based vocabulary builder"""

from pathlib import Path

import praw
from PyDictionary import PyDictionary


def lookup():
    """look up definitions of words"""

    words = read()
    dictionary = PyDictionary

    for i in range(len(words)):
        if not (words.at[i, "definition"]):
            word = words.at[i, "word"].lower().strip()
            words.at[i, "word"] = word

            print("looking up " + word)
            try:
                this_meaning = dictionary.meaning(word)
                words.at[i, "definition"] = this_meaning[list(this_meaning.keys())[0]][
                    0
                ]
            except:
                pass

    print("Done!")
    save(words)


def save(words):
    """save changes made to dictionary to disk"""

    file_loc = get_file_loc()
    words.to_csv(file_loc, sep="\t", index=False)


def reddit():
    """scrape /r/logophilia for new words"""

    # read client ID and client secret
    path = Path(__file__)
    path = (path.parent).joinpath(".clientid")
    f = open(path, "r")
    clientid = f.read()
    f.close()

    path = Path(__file__)
    path = (path.parent).joinpath(".clientsecret")
    f = open(path, "r")
    secret = f.read()
    f.close()

    reddit = praw.Reddit(
        client_id=clientid, client_secret=secret, user_agent="agent", limit=None
    )

    reddit_words = []

    for submission in reddit.subreddit("logophilia").hot(limit=None):
        reddit_words.append(submission.title)

    # write to disk
    path = Path(__file__)
    path = (path.parent).joinpath("reddit_words.txt")
    with open(path, "w") as f:
        f.writelines("%s\n" % line for line in reddit_words)
    f.close()
    parseAndAddWords()


def parseAndAddWords(filename="reddit_words.txt"):
    """convert raw dump into words + definitions"""
    path = Path(__file__)
    path = (path.parent).joinpath("reddit_words.txt")
    f = open(path, "r")
    lines = f.readlines()
    f.close()

    words = read()

    for line in lines:

        # if line contains a ?, skip it
        if line.find("?") > 0:
            continue

        # replace a bunch of junk
        line = line.replace("(adj.)", "")
        line = line.replace("(trans.)", "")
        line = line.replace("[adj.]", "")
        line = line.replace("(n.)", "")
        line = line.replace("(n)", "")
        line = line.replace("(verb)", "")
        line = line.replace("(v.)", "")
        line = line.replace("(adj)", "")

        # skip lines that don't contain any known identifier
        ids = []
        if line.find(":") > 0:
            ids.append(line.find(":"))
        if line.find("-") > 0:
            ids.append(line.find("-"))
        if line.find("|") > 0:
            ids.append(line.find("|"))

        if len(ids) != 1:
            continue

        line = line.split(line[ids[0]])

        word = line[0]
        definition = line[1]

        word = word.replace('"', "")
        word = word.lower()

        print(word)
        print(definition)

        words.loc[len(words.index)] = [word, definition, -1]

    save(words)
