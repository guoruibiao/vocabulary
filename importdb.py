#!/usr/bin/python3

from models.words import Words


with open("./data/vocabularies.txt", "r") as f:
    lines = f.readlines()
    f.close()

    words = Words()
    for line in lines:
        row = str(line).strip("\n").split("\t")
        words.insert(row[0], row[1])

    print("done.")