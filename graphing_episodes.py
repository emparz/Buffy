"""
graph the scores of all the words per episode and all the dialogue per episode
graph the scores per 100 words individual episodes
"""

import matplotlib.pyplot as plt
import analysis_methods
import numpy as np

wordsPerEpisode = {}
dialoguePerEpisode = {}

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


def do_for_every_season(file):
    episode = open('data/per_episode/' + file + '.txt', 'r')
    words = []
    for word in episode:
        words.append(word)
    wordsPerEpisode[file] = words
    episode.close()

    episode = open('data/dialogue/' + file + '.txt', 'r')
    words = []
    for word in episode:
        words.append(word)
    dialoguePerEpisode[file] = words
    episode.close()


def get_scores(episode):
    structureTotal = 0.0
    powerTotal = 0.0
    dangerTotal = 0.0
    numValidWords = 0.0
    # get the scores for the episode
    for word in episode:
        word = word.strip()
        word = word.lower()
        if word in scoringDict.keys():
            # print(word + " found")
            # add the values of this word to the totals
            numValidWords += 1.0
            structureTotal += float(scoringDict[word][0])
            powerTotal += float(scoringDict[word][1])
            dangerTotal += float(scoringDict[word][2])
    # this value will be 0 if a character doesn't have any lines in an episode
    if not numValidWords == 0.0:
        return structureTotal/numValidWords, powerTotal/numValidWords, dangerTotal/numValidWords
    return 0.0, 0.0, 0.0


# create and save graphs for each character
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
    axs.set_ylabel('score', fontsize=16)
    axs.set_xlabel('words', fontsize=16)
    axs.margins(0)
    axs.grid()

    axs.set_xticks(np.arange(0, 8000, 200))
    axs.set_yticks(np.arange(-0.25, 0.25, .05))

    # plt.show()
    fig.tight_layout()
    plt.savefig('plots/' + episode + 'Scores.png')
    plt.close()

    # also write words per episode to file to make it easier to read
    totalWordsFile = open('plots/plotsData/' + episode + 'Scores.txt', 'w')
    for e in episodeScores:
        totalWordsFile.write(str(e) + ': ' + str(episodeScores[e][0]) + ', ' +
                             str(episodeScores[e][1]) + ', ' + str(episodeScores[e][0]) + '\n')
    totalWordsFile.close()


# create and save graphs for each character
def graph_show(scoring, episodeScores):
    # put structure, power, danger scores into lists
    structure = []
    power = []
    danger = []
    # for getting character average scores
    structureTotal = 0.0
    powerTotal = 0.0
    dangerTotal = 0.0
    totalEpisodes = 0
    for e in episodeScores:
        strct = episodeScores[e][0]
        structure.append(strct)
        pwr = episodeScores[e][1]
        power.append(pwr)
        dngr = episodeScores[e][2]
        danger.append(dngr)
        if isinstance(strct, float) and isinstance(pwr, float) and isinstance(dngr, float):
            structureTotal += strct
            powerTotal += pwr
            dangerTotal += dngr
            totalEpisodes += 1

    plt.rcParams['figure.figsize'] = [25, 10]
    fig, axs = plt.subplots(1)
    fig.suptitle(scoring + ' scores per episode', fontsize=20)
    # graph the characters scores
    episodes = list(range(1, 145, 1))
    axs.plot(episodes, structure, 'tab:orange', marker='o')
    axs.plot(episodes, power, 'tab:blue', marker='o')
    axs.plot(episodes, danger, 'tab:red', marker='o')
    axs.set_title('(structure ave=' + str(structureTotal / totalEpisodes) + ', power ave=' +
                  str(powerTotal / totalEpisodes) + ', danger ave=' + str(dangerTotal / totalEpisodes) + ')', fontsize=16)
    axs.set_ylabel('score', fontsize=16)
    axs.set_xlabel('episode number', fontsize=16)
    axs.margins(0)
    axs.grid()

    axs.set_xticks(np.arange(0, 145, 2))
    axs.set_yticks(np.arange(-0.25, 0.25, .05))

    # plt.show()
    fig.tight_layout()
    plt.savefig('plots/all' + scoring + 'Scores.png')
    plt.close()

    # also write words per episode to file to make it easier to read
    totalWordsFile = open('plots/plotsData/all' + scoring + 'Scores.txt', 'w')
    for e in episodeScores:
        totalWordsFile.write(e + ": " + str(episodeScores[e][0]) + ", " +
                             str(episodeScores[e][1]) + ", " + str(episodeScores[e][0]) + "\n")
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
        totalWordsScores[w] = get_scores(wordsPerEpisode[w])
    graph_show('words', totalWordsScores)

    ''' get the scores for every episode (dialogue only)'''
    totalDialogueScores = {}
    for w in dialoguePerEpisode:
        totalDialogueScores[w] = get_scores(dialoguePerEpisode[w])
    graph_show('dialogue', totalDialogueScores)

    ''' put season 1, episode 1 words into list '''
    s1e01Words = []
    episodeWords = open('data/per_episode/s1e01.txt', 'r')
    for l in episodeWords:
        s1e01Words.append(l)
    episodeWords.close()

    s1e12Words = []
    episodeWords = open('data/per_episode/s1e12.txt', 'r')
    for l in episodeWords:
        s1e12Words.append(l)
    episodeWords.close()

    ''' get the scores for episode with function '''
    s1e01Scores = {}
    windowSize = 100
    for w in range(0, len(s1e01Words), windowSize):
        s1e01Scores[w + windowSize] = get_scores(s1e01Words[w:w + windowSize])
    graph_episode('s1e01', s1e01Scores)

    s1e12Scores = {}
    windowSize = 100
    for w in range(0, len(s1e12Words), windowSize):
        s1e12Scores[w + windowSize] = get_scores(s1e12Words[w:w + windowSize])
    graph_episode('s1e12', s1e12Scores)
