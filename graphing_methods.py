import os


def get_character_lines(character, file):
    episode = 'data/per_character/' + file
    lines = []
    for file in os.listdir(episode):
        # turn filename into string
        fileString = str(os.path.join(episode, file))
        # check if buffy is in the file name
        if character in fileString and '[' + character + ']' not in fileString:
            # print(fileString)
            # for testing print(fileString)
            linesFile = open(fileString, 'r')
            for l in linesFile:
                # add every line to lines list
                lines.append(l)
            linesFile.close()
    return lines


def count_character_words(lines):
    # count words
    numWordsPerEp = {}
    totWords = 0
    for ep in lines:
        currWords = 0
        for word in lines[ep]:
            currWords += 1
        numWordsPerEp[ep] = currWords
        totWords += currWords
    return numWordsPerEp, totWords


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


def get_num_chars(file):
    episode = 'data/per_character/' + file
    chars = 0
    # count the number of character files in this folder
    for c in os.listdir(episode):
        # if the file exists, count the files
        if os.path.isfile(os.path.join(episode, c)):
            chars += 1
    return chars
