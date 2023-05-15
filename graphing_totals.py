"""
graphs the total number of words per episode, characters per episode, and dialogue per episode
"""
import graphing_methods
import matplotlib.pyplot as plt
import analysis_methods
import numpy as np

wordsPerEpisode = {}
numCharacters = {}
dialoguePerEpisode = {}


# put methods in here that need to be done for every episode (file)
def do_for_every_season(file):
    wordsPerEpisode[file] = graphing_methods.get_num_words(file)
    numCharacters[file] = graphing_methods.get_num_chars(file)
    dialoguePerEpisode[file] = graphing_methods.get_num_dialogue(file)


# if __name__ == '__main__':
def graphing_totals():
    print('graphing totals')
    ''' season 1 '''
    for e in range(1, 13):
        filename = analysis_methods.create_filename('s1e', e)
        do_for_every_season(filename)
    ''' season 2 '''
    for e in range(1, 23):
        filename = analysis_methods.create_filename('s2e', e)
        do_for_every_season(filename)
    ''' season 3 '''
    for e in range(1, 23):
        filename = analysis_methods.create_filename('s3e', e)
        do_for_every_season(filename)
    ''' season 4 '''
    for e in range(1, 23):
        filename = analysis_methods.create_filename('s4e', e)
        do_for_every_season(filename)
    ''' season 5 '''
    for e in range(1, 23):
        filename = analysis_methods.create_filename('s5e', e)
        do_for_every_season(filename)
    ''' season 6 '''
    for e in range(1, 23):
        filename = analysis_methods.create_filename('s6e', e)
        do_for_every_season(filename)
    ''' season 7 '''
    for e in range(1, 23):
        filename = analysis_methods.create_filename('s7e', e)
        do_for_every_season(filename)

    # values we will be graphing
    episodes = list(range(1, 145, 1))
    numWords = list(wordsPerEpisode.values())
    numDialogue = list(dialoguePerEpisode.values())
    numChars = list(numCharacters.values())

    ''' graphing '''
    # no method for graphing in this file because each one is individualized
    plt.rcParams['figure.figsize'] = [25, 10]

    # graphing total number of words per episode
    fig, axs = plt.subplots(1)
    fig.suptitle('words per episode', fontsize=20)
    axs.plot(episodes, numWords, 'tab:green', marker='o')
    axs.set_ylabel('number of words', fontsize=16)
    axs.set_xlabel('episode number', fontsize=16)
    axs.margins(0)
    axs.grid()
    axs.set_xticks(np.arange(0, 145, 2))
    axs.set_yticks(np.arange(0, 13000, 500))
    fig.tight_layout()
    plt.savefig('plots/numWords.png')
    plt.close()
    # write data to file to look at easier
    totalWordsFile = open('plots/plotsData/numWords.txt', 'w')
    for e in wordsPerEpisode:
        totalWordsFile.write(e + ": " + str(wordsPerEpisode[e]) + "\n")
    totalWordsFile.close()

    # graphing number of characters per episode
    fig, axs = plt.subplots(1)
    fig.suptitle('characters per episode', fontsize=20)
    axs.plot(episodes, numChars, 'tab:green', marker='o')
    axs.set_ylabel('number of characters', fontsize=16)
    axs.set_xlabel('episode number', fontsize=16)
    axs.margins(0)
    axs.grid()
    axs.set_xticks(np.arange(0, 145, 2))
    axs.set_yticks(np.arange(0, 50, 5))
    fig.tight_layout()
    plt.savefig('plots/numCharacters.png')
    plt.close()
    # write data to file to look at easier
    totalWordsFile = open('plots/plotsData/numCharacters.txt', 'w')
    for e in numCharacters:
        totalWordsFile.write(e + ": " + str(numCharacters[e]) + "\n")
    totalWordsFile.close()

    # graphing total number of dialogue words per episode
    fig, axs = plt.subplots(1)
    fig.suptitle('dialogue words per episode', fontsize=20)
    axs.plot(episodes, numDialogue, 'tab:green', marker='o')
    axs.set_ylabel('number of words spoken', fontsize=16)
    axs.set_xlabel('episode number', fontsize=16)
    axs.margins(0)
    axs.grid()
    axs.set_xticks(np.arange(0, 145, 2))
    axs.set_yticks(np.arange(0, 13000, 500))
    # plt.show()
    fig.tight_layout()
    plt.savefig('plots/numDialogue.png')
    plt.close()
