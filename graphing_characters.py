"""
graph the number of words per episode per character and the scores per episode per character
"""
import matplotlib.pyplot as plt
import analysis_methods
import graphing_methods
import numpy as np

buffyLines = {}
willowLines = {}
xanderLines = {}
gilesLines = {}
angelLines = {}
cordeliaLines = {}
dawnLines = {}
ozLines = {}
joyceLines = {}
faithLines = {}
druLines = {}
taraLines = {}
anyaLines = {}
spikeLines = {}

# 'character': [[structure, power, danger], total words said]
averages = {'buffy': [[0.0, 0.0, 0.0], 0.0], 'willow': [[0.0, 0.0, 0.0], 0.0], 'xander': [[0.0, 0.0, 0.0], 0.0],
            'giles': [[0.0, 0.0, 0.0], 0.0], 'angel': [[0.0, 0.0, 0.0], 0.0], 'cordelia': [[0.0, 0.0, 0.0], 0.0],
            'dawn': [[0.0, 0.0, 0.0], 0.0], 'oz': [[0.0, 0.0, 0.0], 0.0], 'joyce': [[0.0, 0.0, 0.0], 0.0],
            'faith': [[0.0, 0.0, 0.0], 0.0], 'drusilla': [[0.0, 0.0, 0.0], 0.0], 'tara': [[0.0, 0.0, 0.0], 0.0],
            'anya': [[0.0, 0.0, 0.0], 0.0], 'spike': [[0.0, 0.0, 0.0], 0.0]}

''' get the ousiometry data '''
scores = open('data/ousiometry_data_augmented.tsv', 'r')
scoringDict = {}
for line in scores:
    # split data by tab
    # store it in list
    wordScores = line.split('\t')
    # have word as key and list of [structure, power, danger] scores
    scoringDict[wordScores[0]] = [wordScores[6], wordScores[7], wordScores[8].strip()]
scores.close()


# put methods in here that need to be done for every episode (file)
def do_for_every_season(file):
    buffyLines[file] = graphing_methods.get_character_lines("buffy", file)
    willowLines[file] = graphing_methods.get_character_lines("willow", file)
    xanderLines[file] = graphing_methods.get_character_lines("xander", file)
    gilesLines[file] = graphing_methods.get_character_lines("giles", file)
    angelLines[file] = graphing_methods.get_character_lines("angel", file)
    cordeliaLines[file] = graphing_methods.get_character_lines("cordelia", file)
    dawnLines[file] = graphing_methods.get_character_lines("dawn", file)
    ozLines[file] = graphing_methods.get_character_lines("oz", file)
    joyceLines[file] = graphing_methods.get_character_lines("joyce", file)
    faithLines[file] = graphing_methods.get_character_lines("faith", file)
    druLines[file] = graphing_methods.get_character_lines("drusilla", file)
    taraLines[file] = graphing_methods.get_character_lines("tara", file)
    anyaLines[file] = graphing_methods.get_character_lines("anya", file)
    spikeLines[file] = graphing_methods.get_character_lines("spike", file)


# given a character (string)
# go into the global variable averages
# reset the values for structure, power, danger to their average structure, power, danger scores
def find_averages(character):
    averages[character][0][0] = averages[character][0][0] / averages[character][1]
    averages[character][0][1] = averages[character][0][1] / averages[character][1]
    averages[character][0][2] = averages[character][0][2] / averages[character][1]


# given a character (string) and all their lines for an episode (list)
# sum up the scores, add to the average count
# return the average score for structure, power, danger
def get_scores(character, lines):
    structureTotal = 0.0
    powerTotal = 0.0
    dangerTotal = 0.0
    numValidWords = 0.0
    # get the scores for the episode
    for word in lines:
        word = word.strip()
        word = word.lower()
        if word in scoringDict.keys():
            # for testing
            # print(word + " found")
            # add the values of this word to the totals
            numValidWords += 1.0
            structureTotal += float(scoringDict[word][0])
            powerTotal += float(scoringDict[word][1])
            dangerTotal += float(scoringDict[word][2])

    # add to averages
    averages[character][0][0] += structureTotal
    averages[character][0][1] += powerTotal
    averages[character][0][2] += dangerTotal
    averages[character][1] += numValidWords

    # only want to count scores if character has more than 20 words
    if numValidWords > 20:
        return structureTotal / numValidWords, powerTotal / numValidWords, dangerTotal / numValidWords
    return None, None, None


# given a character (string) and their scores in a dictionary
# create and save graphs for each character
def graph_scores(character, characterScores):
    # put structure, power, danger scores into lists
    structure = []
    power = []
    danger = []
    for e in characterScores:
        structure.append(characterScores[e][0])
        power.append(characterScores[e][1])
        danger.append(characterScores[e][2])

    ''' graphing '''
    plt.rcParams['figure.figsize'] = [25, 10]
    fig, axs = plt.subplots(1)
    fig.suptitle(character + ' scores per episode', fontsize=20)
    # graph the characters scores
    episodes = list(range(1, 145, 1))
    axs.plot(episodes, structure, 'tab:orange', marker='o')
    axs.plot(episodes, power, 'tab:blue', marker='o')
    axs.plot(episodes, danger, 'tab:red', marker='o')
    axs.set_title('(structure average=' + '{:.8f}'.format(averages[character][0][0]) +
                  ', power average=' + '{:.8f}'.format(averages[character][0][1]) +
                  ', danger average=' + '{:.8f}'.format(averages[character][0][2]) + ')')

    # print(character)
    # print('(structure average=' + '{:.8f}'.format(averages[character][0][0]) +
    #               ', power average=' + '{:.8f}'.format(averages[character][0][1]) +
    #               ', danger average=' + '{:.8f}'.format(averages[character][0][2]) + ')')

    axs.set_ylabel('score', fontsize=16)
    axs.set_xlabel('episode number', fontsize=16)
    axs.margins(0)
    axs.grid()

    axs.set_xticks(np.arange(0, 145, 2))
    axs.set_yticks(np.arange(-0.25, 0.25, .05))

    # plt.show()
    fig.tight_layout()
    plt.savefig('plots/' + character + 'Scores.png')
    plt.close()

    # also write words per episode to file to make it easier to read
    totalWordsFile = open('plots/plotsData/' + character + 'Scores.txt', 'w')
    for e in characterScores:
        writing = e + ': '
        # structure
        if isinstance(characterScores[e][0], float):
            writing += '{:.8f}'.format(characterScores[e][0])
        else:
            writing += str(characterScores[e][0])
        # power
        if isinstance(characterScores[e][1], float):
            writing += '{:.8f}'.format(characterScores[e][1])
        else:
            writing += str(characterScores[e][1])
        # danger
        if isinstance(characterScores[e][2], float):
            writing += '{:.8f}'.format(characterScores[e][2])
        else:
            writing += str(characterScores[e][2])
        writing += '\n'
        totalWordsFile.write(writing)
    totalWordsFile.close()


# given a character (string) and their lines (dictionary)
# create and save graphs for each character
def graph_total_words(character, lines):
    # returns a dictionary with each episode and the number of lines the character has in it,
    # and the total number of words a character says
    wordsPerEp, totWords = graphing_methods.count_character_words(lines)

    ''' graphing '''
    plt.rcParams['figure.figsize'] = [25, 10]
    fig, axs = plt.subplots(1)
    fig.suptitle(character + ' # of words (total=' + str(totWords) + ')', fontsize=20)
    # graph number of words
    episodes = list(range(1, 145, 1))
    numWords = list(wordsPerEp.values())
    axs.plot(episodes, numWords, 'tab:orange', marker='o')
    axs.set_ylabel('number of words', fontsize=16)
    axs.set_xlabel('episode number', fontsize=16)
    axs.margins(0)
    axs.grid()
    axs.set_xticks(np.arange(0, 145, 2))
    axs.set_yticks(np.arange(0, 1950, 50))
    # plt.show()
    fig.tight_layout()
    plt.savefig('plots/' + character + 'NumWords.png')
    plt.close()

    # also write words per episode to file to make it easier to read
    totalWordsFile = open('plots/plotsData/' + character + 'NumWords.txt', 'w')
    for e in wordsPerEp:
        totalWordsFile.write(e + ": " + str(wordsPerEp[e]) + "\n")
    totalWordsFile.close()


# if __name__ == '__main__':
def graphing_characters():
    print('graphing characters')
    ''' season 1 '''
    for ep in range(1, 13):
        # open file for every episode
        filename = analysis_methods.create_filename('s1e', ep)
        do_for_every_season(filename)
    ''' season 2 '''
    for ep in range(1, 23):
        # open file for every episode
        filename = analysis_methods.create_filename('s2e', ep)
        do_for_every_season(filename)
    ''' season 3 '''
    for ep in range(1, 23):
        # open file for every episode
        filename = analysis_methods.create_filename('s3e', ep)
        do_for_every_season(filename)
    ''' season 4 '''
    for ep in range(1, 23):
        # open file for every episode
        filename = analysis_methods.create_filename('s4e', ep)
        do_for_every_season(filename)
    ''' season 5 '''
    for ep in range(1, 23):
        # open file for every episode
        filename = analysis_methods.create_filename('s5e', ep)
        do_for_every_season(filename)
    ''' season 6 '''
    for ep in range(1, 23):
        # open file for every episode
        filename = analysis_methods.create_filename('s6e', ep)
        do_for_every_season(filename)
    ''' season 7 '''
    for ep in range(1, 23):
        # open file for every episode
        filename = analysis_methods.create_filename('s7e', ep)
        do_for_every_season(filename)

    ''' get the character's scores '''
    buffyScores = {}
    for ep in buffyLines:
        buffyScores[ep] = get_scores('buffy', buffyLines[ep])
    willowScores = {}
    for ep in willowLines:
        willowScores[ep] = get_scores('willow', willowLines[ep])
    xanderScores = {}
    for ep in xanderLines:
        xanderScores[ep] = get_scores('xander', xanderLines[ep])
    gilesScores = {}
    for ep in gilesLines:
        gilesScores[ep] = get_scores('giles', gilesLines[ep])
    angelScores = {}
    for ep in angelLines:
        angelScores[ep] = get_scores('angel', angelLines[ep])
    cordeliaScores = {}
    for ep in cordeliaLines:
        cordeliaScores[ep] = get_scores('cordelia', cordeliaLines[ep])
    dawnScores = {}
    for ep in dawnLines:
        dawnScores[ep] = get_scores('dawn', dawnLines[ep])
    ozScores = {}
    for ep in ozLines:
        ozScores[ep] = get_scores('oz', ozLines[ep])
    joyceScores = {}
    for ep in joyceLines:
        joyceScores[ep] = get_scores('joyce', joyceLines[ep])
    faithScores = {}
    for ep in faithLines:
        faithScores[ep] = get_scores('faith', faithLines[ep])
    druScores = {}
    for ep in druLines:
        druScores[ep] = get_scores('drusilla', druLines[ep])
    taraScores = {}
    for ep in taraLines:
        taraScores[ep] = get_scores('tara', taraLines[ep])
    anyaScores = {}
    for ep in anyaLines:
        anyaScores[ep] = get_scores('anya', anyaLines[ep])
    spikeScores = {}
    for ep in spikeLines:
        spikeScores[ep] = get_scores('spike', spikeLines[ep])

    '''calculate averages for all characters'''
    find_averages('buffy')
    find_averages('willow')
    find_averages('xander')
    find_averages('giles')
    find_averages('angel')
    find_averages('cordelia')
    find_averages('dawn')
    find_averages('oz')
    find_averages('joyce')
    find_averages('faith')
    find_averages('drusilla')
    find_averages('tara')
    find_averages('anya')
    find_averages('spike')

    ''' graphing scores per character'''
    graph_scores('buffy', buffyScores)
    graph_scores('willow', willowScores)
    graph_scores('xander', xanderScores)
    graph_scores('giles', gilesScores)
    graph_scores('angel', angelScores)
    graph_scores('cordelia', cordeliaScores)
    graph_scores('dawn', dawnScores)
    graph_scores('oz', ozScores)
    graph_scores('joyce', joyceScores)
    graph_scores('faith', faithScores)
    graph_scores('drusilla', druScores)
    graph_scores('tara', taraScores)
    graph_scores('anya', anyaScores)
    graph_scores('spike', spikeScores)

    ''' graphing total words per character '''
    graph_total_words('buffy', buffyLines)
    graph_total_words('willow', willowLines)
    graph_total_words('xander', xanderLines)
    graph_total_words('giles', gilesLines)
    graph_total_words('angel', angelLines)
    graph_total_words('cordelia', cordeliaLines)
    graph_total_words('dawn', dawnLines)
    graph_total_words('oz', ozLines)
    graph_total_words('joyce', joyceLines)
    graph_total_words('faith', faithLines)
    graph_total_words('drusilla', druLines)
    graph_total_words('tara', taraLines)
    graph_total_words('anya', anyaLines)
    graph_total_words('spike', spikeLines)
