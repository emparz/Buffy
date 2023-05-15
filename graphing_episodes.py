"""
graph the scores of all the words per episode and all the dialogue per episode
graph the scores per 100 words individual episodes
"""

import matplotlib.pyplot as plt
import analysis_methods
import numpy as np

wordsPerEpisode = {}
dialoguePerEpisode = {}

# 'episode/what we're counting for the entire show': [[structure, power, danger], total words]
averages = {'dialogue': [[0.0, 0.0, 0.0], 0.0], 'words': [[0.0, 0.0, 0.0], 0.0],
            's1e01': [[0.0, 0.0, 0.0], 0.0], 's1e12': [[0.0, 0.0, 0.0], 0.0]}


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
    episode = open('data/words_per_ep/' + file + '.txt', 'r')
    words = []
    for word in episode:
        words.append(word)
    wordsPerEpisode[file] = words
    episode.close()

    episode = open('data/dialogue_per_ep/' + file + '.txt', 'r')
    words = []
    for word in episode:
        words.append(word)
    dialoguePerEpisode[file] = words
    episode.close()


# given what's being scored: episode name, words in series, dialogue (string)
# and the lines we're looking at for an episode: a window or words, all words, all dialogue (list)
# sum up the scores, add to the average count
# return the average score for structure, power, danger
def get_scores(scoring, lines):
    structureTotal = 0.0
    powerTotal = 0.0
    dangerTotal = 0.0
    numValidWords = 0.0
    # get the scores for the episode
    for word in lines:
        word = word.strip()
        word = word.lower()
        if word in scoringDict.keys():
            # print(word + " found")
            # add the values of this word to the totals
            numValidWords += 1.0
            structureTotal += float(scoringDict[word][0])
            powerTotal += float(scoringDict[word][1])
            dangerTotal += float(scoringDict[word][2])

    # add to averages
    averages[scoring][0][0] += structureTotal
    averages[scoring][0][1] += powerTotal
    averages[scoring][0][2] += dangerTotal
    averages[scoring][1] += numValidWords
    # this value will be 0 if a character doesn't have any lines in an episode
    if numValidWords > 20:
        return structureTotal/numValidWords, powerTotal/numValidWords, dangerTotal/numValidWords
    return None, None, None


# given the episode name and all the scores per window, graph
def graph_episode(episode, episodeScores):
    plt.rcParams['figure.figsize'] = [25, 10]
    fig, axs = plt.subplots(1)
    fig.suptitle(episode + ' scores per episode', fontsize=20)
    # put structure, power, danger scores into lists
    structure = []
    power = []
    danger = []
    for e in episodeScores:
        structure.append(episodeScores[e][0])
        power.append(episodeScores[e][1])
        danger.append(episodeScores[e][2])
    # graph number of words
    windows = list(episodeScores.keys())
    axs.plot(windows, structure, 'tab:orange', marker='o')
    axs.plot(windows, power, 'tab:blue', marker='o')
    axs.plot(windows, danger, 'tab:red', marker='o')
    axs.set_title('(structure average=' + '{:.4f}'.format(averages[episode][0][0]) +
                  ', power average=' + '{:.4f}'.format(averages[episode][0][1]) +
                  ', danger average=' + '{:.4f}'.format(averages[episode][0][2]) + ')')
    axs.set_ylabel('score', fontsize=16)
    axs.set_xlabel('words', fontsize=16)
    axs.margins(0)
    axs.grid()

    axs.set_xticks(np.arange(0, 8000, 200))
    axs.set_yticks(np.arange(-0.25, 0.25, .025))

    # plt.show()
    fig.tight_layout()
    plt.savefig('plots/' + episode + 'Scores.png')
    plt.close()

    # also write words per episode to file to make it easier to read
    totalWordsFile = open('plots/plotsData/' + episode + 'Scores.txt', 'w')
    for e in episodeScores:
        writing = str(e) + ': '
        # structure
        if isinstance(episodeScores[e][0], float):
            writing += '{:.4f}'.format(episodeScores[e][0]) + ', '
        else:
            writing += str(episodeScores[e][0]) + ', '
        # power
        if isinstance(episodeScores[e][1], float):
            writing += '{:.4f}'.format(episodeScores[e][1]) + ', '
        else:
            writing += str(episodeScores[e][1]) + ', '
        # danger
        if isinstance(episodeScores[e][2], float):
            writing += '{:.4f}'.format(episodeScores[e][2])
        else:
            writing += str(episodeScores[e][2])
        writing += '\n'
        totalWordsFile.write(writing)
    totalWordsFile.close()


# given what's being graphed (dialogue vs all words) and scores for each episode, graph
def graph_show(scoring, episodeScores):
    # put structure, power, danger scores into lists
    structure = []
    power = []
    danger = []

    for e in episodeScores:
        structure.append(episodeScores[e][0])
        power.append(episodeScores[e][1])
        danger.append(episodeScores[e][2])

    plt.rcParams['figure.figsize'] = [25, 10]
    fig, axs = plt.subplots(1)
    fig.suptitle(scoring + ' scores per episode', fontsize=20)
    # graph the characters scores
    episodes = list(range(1, 145, 1))
    axs.plot(episodes, structure, 'tab:orange', marker='o')
    axs.plot(episodes, power, 'tab:blue', marker='o')
    axs.plot(episodes, danger, 'tab:red', marker='o')
    axs.set_title('(structure average=' + '{:.4f}'.format(averages[scoring][0][0]) +
                  ', power average=' + '{:.4f}'.format(averages[scoring][0][1]) +
                  ', danger average=' + '{:.4f}'.format(averages[scoring][0][2]) + ')')
    axs.set_ylabel('score', fontsize=16)
    axs.set_xlabel('episode number', fontsize=16)
    axs.margins(0)
    axs.grid()

    axs.set_xticks(np.arange(0, 145, 2))
    axs.set_yticks(np.arange(-0.25, 0.25, .025))

    # plt.show()
    fig.tight_layout()
    plt.savefig('plots/all' + scoring + 'Scores.png')
    plt.close()

    # also write words per episode to file to make it easier to read
    totalWordsFile = open('plots/plotsData/all' + scoring + 'Scores.txt', 'w')
    for e in episodeScores:
        writing = e + ': '
        # structure
        if isinstance(episodeScores[e][0], float):
            writing += '{:.4f}'.format(episodeScores[e][0]) + ', '
        else:
            writing += str(episodeScores[e][0]) + ', '
        # power
        if isinstance(episodeScores[e][1], float):
            writing += '{:.4f}'.format(episodeScores[e][1]) + ', '
        else:
            writing += str(episodeScores[e][1]) + ', '
        # danger
        if isinstance(episodeScores[e][2], float):
            writing += '{:.4f}'.format(episodeScores[e][2])
        else:
            writing += str(episodeScores[e][2])
        writing += '\n'
        totalWordsFile.write(writing)
    totalWordsFile.close()


# if __name__ == '__main__':
def graphing_episodes():
    print('graphing episodes')
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

    ''' get the scores for every episode (all words)'''
    totalWordsScores = {}
    for w in wordsPerEpisode:
        totalWordsScores[w] = get_scores('words', wordsPerEpisode[w])
    graph_show('words', totalWordsScores)

    ''' get the scores for every episode (dialogue only)'''
    totalDialogueScores = {}
    for w in dialoguePerEpisode:
        totalDialogueScores[w] = get_scores('dialogue', dialoguePerEpisode[w])
    graph_show('dialogue', totalDialogueScores)

    ''' put episode's words into list '''
    s1e01Words = []
    episodeWords = open('data/words_per_ep/s1e01.txt', 'r')
    for l in episodeWords:
        s1e01Words.append(l)
    episodeWords.close()

    s1e12Words = []
    episodeWords = open('data/words_per_ep/s1e12.txt', 'r')
    for l in episodeWords:
        s1e12Words.append(l)
    episodeWords.close()

    ''' get the scores for episode '''
    s1e01Scores = {}
    windowSize = 100
    for w in range(0, len(s1e01Words), windowSize):
        s1e01Scores[w + windowSize] = get_scores('s1e01', s1e01Words[w:w + windowSize])
    graph_episode('s1e01', s1e01Scores)

    s1e12Scores = {}
    windowSize = 100
    for w in range(0, len(s1e12Words), windowSize):
        s1e12Scores[w + windowSize] = get_scores('s1e12', s1e12Words[w:w + windowSize])
    graph_episode('s1e12', s1e12Scores)
