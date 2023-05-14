
def create_filename(ssn, ep):
    # create the filename with the season and episode number
    filename = ssn
    if ep < 10:
        filename += '0'
    filename += str(ep)
    return filename


# write words per episode
def write_words_per_episode(lines, file):
    # add new lines to a string linesString
    linesList = []
    for line in lines:
        line = remove_speaker(line)
        linesList.append(line)

    wordsInLine = lines_into_words(linesList)

    # open file
    episode = open('data/per_episode/' + file + '.txt', 'w')
    # write each element of the list to a file
    for word in wordsInLine:
        # don't write empty spaces
        if not word == '' or word == '\n':
            episode.write(word.strip() + '\n')
    episode.close()


# write dialogue per episode
def write_dialogue_per_episode(lines, file):
    # add new lines to a string linesString
    linesList = []
    for line in lines:
        speaker = get_speaker(line)
        if not speaker == "scene change" and not speaker == "scene direction":
            line = remove_speaker(line)
            linesList.append(line)
    wordsInLine = lines_into_words(linesList)
    # open file
    episode = open('data/dialogue/' + file + '.txt', 'w')
    # write each element of the list to a file
    for word in wordsInLine:
        # don't write empty spaces
        if not word == '' or word == '\n':
            episode.write(word.strip() + '\n')
    episode.close()


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


# helper function to find speaker
def get_speaker(line):
    # for each line in an episode, find the speaker
    colonIndex = line.find(':')
    speaker = line[:colonIndex]
    # get rid of periods, spaces, and /
    # speaker = speaker.replace(' ', '_')
    # speaker = speaker.replace('.', '')
    # speaker = speaker.replace('/', '~')
    speaker = speaker.strip()
    return speaker


# helper function to return line without speaker
def remove_speaker(line):
    # for each line in an episode, remove the speaker
    colonIndex = line.find(':')
    firstCharacterIndex = colonIndex + 2  # the first character index is 2 after :
    # get rid of speaker/scene direction
    return line[firstCharacterIndex:]


# takes a list of lines,
# strips all the lines of punctuation
# returns a list of words
def lines_into_words(lines):
    linesString = ' '.join(lines)
    # strip the lines of punctuation
    punctSymbols = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    linesString = linesString.strip()
    linesString = linesString.translate(str.maketrans('', '', punctSymbols))
    # put all the lines in a file in a list
    return linesString.split(' ')


def get_all_lines(file):
    # open cleaned up file for episode
    edited_r = open('scripts_edited/' + file + '.txt', 'r')
    lines = []
    for l in edited_r:
        # add all the lines in an episode to a list
        lines.append(l)
    edited_r.close()
    return lines
