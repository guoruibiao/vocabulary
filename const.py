#!/usr/bin/python3

DATABASE = "./vocabulary.db"

WORD_TYPE_CUTOFFED = 1
WORD_TYPE_CUTOFF   = 0

WORD_RIGHT_YES     = 1
WORD_RIGHT_NO      = 0

# wrong words review frequency, N means wrong words will occur each N times.
WRONG_WORDS_REVIEW_FREQUENCY = 3

# highlight and with font color red.
RECITE_PRINT_FORMAT   = "[{}]> \33[1m\33[31m{}\33[0m\33[0m"
# answer with font color green
PRINT_VOCABULARY_DESC = "[Answer]\33[1m\33[32m{}\33[0m\33[0m"
# details in database
DETAILS_PRINT_FORMAT_IN_DATABASE = "[Detail]ID:\33[1m\33[32m{}\33[0m\33[0m\t desc=\33[1m\33[32m{}\33[0m\33[0m\tcutoff=\33[1m\33[32m{}\33[0m\33[0m"


# help information
RECITE_HELP_INFORMATION = """
COMMANDS OF RECITING VOCABULARIES
`\33[1m\33[33myes\33[0m\33[0m`     : i have know this vocabulary, just pass it.
`\33[1m\33[33mno\33[0m\33[0m`      : i don't know this vocabulary, tell me the meaning.
`\33[1m\33[33msay\33[0m\33[0m`     : play the audio by using system setting.
`\33[1m\33[33mcutoff\33[0m\33[0m`  : never show this vocabulary again.
`\33[1m\33[33mrepeat\33[0m\33[0m`  : repeat current word and stay in this round.
`\33[1m\33[33mshow  \33[0m\33[0m`  : show details in database.
`\33[1m\33[33mfind=  \33[0m\33[0m` : find=xxx, get the meaning in database with key=xxx
`\33[1m\33[33mstatic=N\33[0m\33[0m`: static=N, show the statics of N days ago. N=0 means current day. N <= 0
`\33[1m\33[33mwrong=N \33[0m\33[0m`: wrong=N, show the wrong words of N days ago. N=0 means current day. N <= Zero
`\33[1m\33[33mquit\33[0m\33[0m`    : quit this recite round.
`\33[1m\33[36mhelp\33[0m\33[0m`    : tip me with keywords.

example:
>say say repeat
>say show
>find=hello
"""

# sub commands to act for reciting words.
COMMANDS_HELP = "help"
COMMANDS_SAY  = "say"
COMMANDS_CUTOFF = "cutoff"
COMMANDS_REPEAT = "repeat"
COMMANDS_SHOW   = "show"
COMMANDS_FIND   = "find="
COMMANDS_STATIC = "static="
COMMANDS_WRONG  = "wrong="
COMMANDS_YES    = "yes"
COMMANDS_NO     = "no"
COMMANDS_QUIT   = "quit"