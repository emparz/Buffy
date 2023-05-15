"""
methods for graphing_characters, graphing_episodes, graphing_totals
"""
import os


# given a dictionary with each episode as keys and a list of the character's lines for said episode as values
# return a dictionary with each episode and the # of words the character says and the total # of words a character says
def count_character_words(lines):
    # count all the words
    numWordsPerEp = {}
    totWords = 0
    for ep in lines:
        currWords = 0
        # for every word in the character's lines for an episode
        for _ in lines[ep]:
            currWords += 1
        numWordsPerEp[ep] = currWords
        totWords += currWords
    return numWordsPerEp, totWords


# given a character (string) and an episode (string)
# go through all the files in that episode's folder, find one(s) with character's name
# return a list with lines from the file(s)
def get_character_lines(character, file):
    episode = 'data/per_character/' + file
    lines = []
    for file in os.listdir(episode):
        # turn filename into string
        fileString = str(os.path.join(episode, file))
        # when there is brackets around a name, it means someone else is pretending to be them
        in_brackets = '[' + character + ']'
        if character in fileString and in_brackets not in fileString and 'buffybot' not in fileString:
            linesFile = open(fileString, 'r')
            for l in linesFile:
                # add every line to lines list
                lines.append(l)
            linesFile.close()
    return lines


# given an episode (string)
# navigate to the folder with all the characters' lines files
# return the number of files in that folder
def get_num_chars(file):
    episode = 'data/per_character/' + file
    chars = 0
    # count the number of character files in this folder
    for c in os.listdir(episode):
        # if the file exists, count the files
        if os.path.isfile(os.path.join(episode, c)):
            chars += 1
    return chars


# given an episode (string)
# open up the file with all the DIALOGUE words from that episode
# return number of dialogue words in that episode
def get_num_dialogue(file):
    episode = open('data/dialogue/' + file + '.txt', 'r')
    words = 0
    # count the number of spoken words in the episode
    for w in episode:
        # ensure word isn't blank line
        if not w == '\n':
            words += 1
    episode.close()
    return words


# given an episode (string)
# open up the file with all the words from that episode
# return number of words in that episode
def get_num_words(file):
    episode = open('data/per_episode/' + file + '.txt', 'r')
    words = 0
    # count the number of words in the episode
    for w in episode:
        # ensure word isn't blank line
        if not w == '\n':
            words += 1
    episode.close()
    return words
