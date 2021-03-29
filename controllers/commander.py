#!/usr/bin/python3
# implement of command set
import time
from random import randint, choice
from subprocess import call
from models.words import Words
from models.history import History
from const import *


class Commander(object):

    def __init__(self):
        self.words = Words()
        self.history = History()

    def help(self):
        """
        subcommands support
        :return:
        """
        pass

    def recite(self):
        rows = self.words.findall()
        # print(rows)
        # add filter here to avoid `cutoffed` words
        rows = [item for item in rows if item[3] == WORD_TYPE_CUTOFF]
        maxIndex, counter = len(rows)-1, 1
        if maxIndex < 1:
            print("master vocabulary is empty.")
            return
        index, keywords = randint(0, maxIndex), []
        while True:
            key, desc = rows[index][1], rows[index][2]
            # change `index` to review worng history words
            if index % WRONG_WORDS_REVIEW_FREQUENCY == 0 and COMMANDS_REPEAT not in keywords:
                wrongRecords = self.history.findWrongWords()
                if len(wrongRecords) > 0:
                    randomChoice = choice(wrongRecords)
                    key, desc = "*" + str(randomChoice[1]), randomChoice[2]
            elif COMMANDS_REPEAT in keywords:
                # bugfix for overridnge by method of `COMMANDS_REPEAT`
                # but there also have the probelm :-(
                pass


            print(RECITE_PRINT_FORMAT.format(counter, key))

            # lstrip symbol "*" in order to aviod saiving to database.
            key = str(key).lstrip("*")
            # parse input of user, then action them
            line = str(input(">"))
            keywords = [str(item).lower() for item in line.split(" ")]

            # judge whether there has 'Enter' ot not
            if len(keywords) == 1 and keywords[0] == '':
                keywords[0] = COMMANDS_REPEAT

            # handle keywords for sub commands.
            for keyword in keywords:
                if keyword == COMMANDS_SAY:
                    call(["say", key])
                    time.sleep(1)
                    call(["say", desc])

                if keyword == COMMANDS_CUTOFF:
                    self.words.setAsCutoffed(key)

                if keyword == COMMANDS_SHOW:
                    record = self.words.find(key)
                    print(DETAILS_PRINT_FORMAT_IN_DATABASE.format(record[0], record[2], record[3]))
                    keywords.append(COMMANDS_REPEAT)

                if keyword.startswith(COMMANDS_FIND):
                    # cannot use method of `lstrip` or there will be a bug.
                    # key = keyword.lstrip(COMMANDS_FIND)
                    key = str(keyword).split("=")[1]
                    meaning = self.words.find(key)
                    if meaning is not None and len(meaning) == 4:
                        desc = meaning[2]
                    else:
                        desc = "not found the desc of \33[1m\33[33m{}\33[0m\33[0m".format(key)
                    # break the inner loop and continue current loop
                    keywords.append(COMMANDS_REPEAT)

                if keyword.startswith(COMMANDS_STATIC):
                    day = keyword.lstrip(COMMANDS_STATIC)
                    self.history.statics(day)
                    keywords.append(COMMANDS_REPEAT)

                if keyword.startswith(COMMANDS_WRONG):
                    day = keyword.lstrip(COMMANDS_WRONG)
                    self.history.outputWrongWords(int(day))
                    keywords.append(COMMANDS_REPEAT)

                if keyword.startswith(COMMANDS_EXPORT):
                    day = int(keyword.lstrip(COMMANDS_EXPORT))
                    self.history.exportWrongWords(day)
                    keywords.append(COMMANDS_REPEAT)

                if keyword == COMMANDS_YES:
                    self.history.addRecord(key, WORD_RIGHT_YES)

                if keyword == COMMANDS_NO:
                    self.history.addRecord(key, WORD_RIGHT_NO)

            # show the correct answer.
            print(PRINT_VOCABULARY_DESC.format(desc))
            if COMMANDS_QUIT in keywords:
                break
            if COMMANDS_REPEAT in keywords:
                continue
            if COMMANDS_HELP in keywords:
                print(RECITE_HELP_INFORMATION)
                keywords.append(COMMANDS_REPEAT)
                continue

            # update next round
            index, counter = randint(0, maxIndex), counter+1
