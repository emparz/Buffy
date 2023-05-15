"""
methods for analysis (and graphing_characters, graphing_episodes, graphing_totals)
"""


# given the season (1, 2, ... 7) and episode number (1, 2, ... 22)
# return a string in the style s1e01 or s7e22
def create_filename(ssn, ep):
    # create the filename with the season and episode number
    filename = ssn
    if ep < 10:
        filename += '0'
    filename += str(ep)
    return filename


# given an episode name
# read all lines from it's edited script file
# return a list of the lines
def get_all_lines(file):
    # open cleaned up file for episode
    edited_r = open('scripts_edited/' + file + '.txt', 'r')
    lines = []
    for l in edited_r:
        # add all the lines in an episode to a list
        lines.append(l)
    edited_r.close()
    return lines


# given a list of lines and an episode name
# find all the characters in that episode
# populate a dictionary with all of each character's lines
# for each character, write lines to a file in the folder for this episode
def get_lines_per_character(lines, file):
    # create a list with every person who has dialogue
    allSpeakers = []
    for line in lines:
        speaker = get_speaker(line)
        # if the speaker isn't in all_speakers, add them
        if speaker not in allSpeakers:
            allSpeakers.append(speaker)
    # for testing
    # print(file)
    # print(allSpeakers)

    # create a dictionary with an empty list for every character
    speakersAndLines = {}
    for speaker in allSpeakers:
        speakersAndLines[speaker] = []

    # populate the dictionary with each character's lines
    for line in lines:
        speaker = get_speaker(line)
        dialogue = remove_speaker(line)
        speakersAndLines[speaker].append(dialogue)

    # add all the lines each character has to a file
    for speaker in speakersAndLines:
        speakerEpisode = open('data/per_character/' + file + '/' + speaker + '.txt', 'w')
        for word in lines_into_words(speakersAndLines[speaker]):
            speakerEpisode.write(word.strip() + '\n')
        speakerEpisode.close()


# given a line
# return the speaker
def get_speaker(line):
    # for each line in an episode, find the speaker
    colonIndex = line.find(':')
    speaker = line[:colonIndex]
    speaker = speaker.strip()
    return speaker


# takes a list of lines (strings) --> ['this is', 'an example']
# strips all the lines of punctuation
# returns a list of words (strings) --> ['this', 'is', 'an', 'example']
def lines_into_words(lines):
    linesString = ' '.join(lines)
    # strip the lines of punctuation
    punctSymbols = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    linesString = linesString.strip()
    linesString = linesString.translate(str.maketrans('', '', punctSymbols))
    # put all the lines in a file in a list
    return linesString.split(' ')


# given a line
# return the line without a speaker
def remove_speaker(line):
    # for each line in an episode, remove the speaker
    colonIndex = line.find(':')
    firstCharacterIndex = colonIndex + 2  # the first character index is 2 after :
    # get rid of speaker/scene direction
    return line[firstCharacterIndex:]


# given a list of lines and an episode name
# create a file and write ONLY the DIALOGUE lines to it
def write_dialogue_per_episode(lines, file):
    # remove speaker from every line and put in new list linesList
    linesList = []
    for line in lines:
        speaker = get_speaker(line)
        # do not include lines with scene change or direction, these aren't dialogue
        if not speaker == "scene change" and not speaker == "scene direction":
            line = remove_speaker(line)
            linesList.append(line)
    # turn a list of lines into a list of words
    wordsInLine = lines_into_words(linesList)
    # open file
    episode = open('data/dialogue/' + file + '.txt', 'w')
    # write each element of the list to a file
    for word in wordsInLine:
        # don't write empty spaces
        if not word == '' or word == '\n':
            episode.write(word.strip() + '\n')
    episode.close()


# given a list of lines and an episode name
# create a file and write the lines to it
def write_words_per_episode(lines, file):
    # remove speaker from every line and put in new list linesList
    linesList = []
    for line in lines:
        line = remove_speaker(line)
        linesList.append(line)
    # turn a list of lines into a list of words
    wordsInLine = lines_into_words(linesList)
    # open file
    episode = open('data/per_episode/' + file + '.txt', 'w')
    # write each element of the list to a file
    for word in wordsInLine:
        # don't write empty spaces
        if not word == '' or word == '\n':
            episode.write(word.strip() + '\n')
    episode.close()
