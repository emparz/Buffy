""" get files of all words, all character lines, number lines, number lines per character """
import analysis_methods


def do_for_every_season(file):
    allLines = analysis_methods.get_all_lines(file)
    # take all the lines from the episode and write to file
    analysis_methods.write_words_per_episode(allLines, file)
    # take all dialogue from episode and write to file
    analysis_methods.write_dialogue_per_episode(allLines, file)
    analysis_methods.get_lines_per_character(allLines, file)


# if __name__ == '__main__':
def analysis():
    print('analyzing')
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
