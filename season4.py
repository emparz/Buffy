""" SEASON 4 """
import script_methods


# if __name__ == '__main__':
def season4():
    print('reformatting season 4')
    for i in range(1, 23):
        '''ALL EPISODE STUFF'''
        # create the filename with the season and episode number
        filename = 's4e'
        if i < 10:
            filename += '0'
        filename += str(i)

        '''REMOVING BLANK LINES'''
        unedited_r = open('scripts/' + filename + '.txt', 'r')
        in_progress_w = open('progress.txt', 'w')
        for l in unedited_r:
            if not l == '\n':  # if the line is not blank
                # episodes that have random line breaks
                if i == 5 or i == 7 or i == 13 or i == 14 or i == 15 or i == 16 \
                        or i == 17 or i == 19 or i == 21 or i == 22:
                    l = script_methods.fix_line_breaks(l)  # fix the line breaks
                in_progress_w.write(l)  # write fixed line to in progress file
        unedited_r.close()
        in_progress_w.close()
        # **** write to edited ****
        in_progress_r = open('progress.txt', 'r')
        edited_w = open('scripts_edited/' + filename + '.txt', 'w')
        for l in in_progress_r:
            edited_w.write(l)
        in_progress_r.close()
        edited_w.close()
        # *************************

        '''REMOVE PARENTHESIS'''
        # episodes 9, 18
        if i == 9 or i == 18:
            edited_r = open('scripts_edited/' + filename + '.txt', 'r')
            in_progress_w = open('progress.txt', 'w')
            for l in edited_r:
                l = script_methods.remove_parenthesis(l)
                in_progress_w.write(l)  # write line to in progress file
            edited_r.close()
            in_progress_w.close()
            # **** write to edited ****
            in_progress_r = open('progress.txt', 'r')
            edited_w = open('scripts_edited/' + filename + '.txt', 'w')
            for l in in_progress_r:
                edited_w.write(l)
            in_progress_r.close()
            edited_w.close()
            # *************************

        # """FIX UPPERCASE SPEAKER"""
        # # episodes 18, 19, 22
        # if i == 18 or i == 19 or i == 22:
        #     edited_r = open('scripts_edited/' + filename + '.txt', 'r')
        #     in_progress_w = open('progress.txt', 'w')
        #     for l in edited_r:
        #         l = methods.fix_uppercase(l)
        #         in_progress_w.write(l)  # write line to in progress file
        #     edited_r.close()
        #     in_progress_w.close()
        #     # **** write to edited ****
        #     in_progress_r = open('progress.txt', 'r')
        #     edited_w = open('scripts_edited/' + filename + '.txt', 'w')
        #     for l in in_progress_r:
        #         edited_w.write(l)
        #     in_progress_r.close()
        #     edited_w.close()
        #     # *************************

        '''INDIVIDUAL EPISODES'''
        # episodes 4, 10, 11
        if i == 4 or i == 10 or i == 11:
            '''FIXING DIALOGUE AND DIRECTION'''
            edited_r = open('scripts_edited/' + filename + '.txt', 'r')
            in_progress_w = open('progress.txt', 'w')
            for l in edited_r:
                l = script_methods.fix_dialogue_and_dir(l)
                in_progress_w.write(l)  # write line to in progress file
            edited_r.close()
            in_progress_w.close()
            # **** write to edited ****
            in_progress_r = open('progress.txt', 'r')
            edited_w = open('scripts_edited/' + filename + '.txt', 'w')
            for l in in_progress_r:
                # make everything lowercase
                l = l.lower()
                edited_w.write(l)
            in_progress_r.close()
            edited_w.close()
            # *************************
        # other episodes
        elif i == 1 or i == 2 or i == 3 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 12 or i == 13 \
                or i == 14 or i == 15 or i == 16 or i == 17 or i == 18 or i == 19 or i == 20 or i == 21 or i == 22:
            '''FIX WEIRD LINES'''
            edited_r = open('scripts_edited/' + filename + '.txt', 'r')
            in_progress_w = open('progress.txt', 'w')
            l1 = ''
            l2 = ''
            for l in edited_r:
                l1 = l2  # l1 is the previous line
                l2 = l  # l2 is the current line
                if not l1 == '':  # make sure l1 isn't blank
                    l = script_methods.fix_unclear_punc(l1, l2)  # fix unclear punctuation things
                    in_progress_w.write(l)  # write fixed line to edited file
            in_progress_w.write(l2)  # write the final line
            edited_r.close()
            in_progress_w.close()
            # **** write to edited ****
            in_progress_r = open('progress.txt', 'r')
            edited_w = open('scripts_edited/' + filename + '.txt', 'w')
            for l in in_progress_r:
                edited_w.write(l)
            in_progress_r.close()
            edited_w.close()
            # *************************

            '''ADD SCENE DIRECTIONS'''
            edited_r = open('scripts_edited/' + filename + '.txt', 'r')
            in_progress_w = open('progress.txt', 'w')
            for l in edited_r:
                l = script_methods.add_scene_dir(l)  # add the scene directions
                in_progress_w.write(l)  # write fixed line to in progress file
            edited_r.close()
            in_progress_w.close()
            # **** write to edited ****
            in_progress_r = open('progress.txt', 'r')
            edited_w = open('scripts_edited/' + filename + '.txt', 'w')
            for l in in_progress_r:
                # make everything lowercase
                l = l.lower()
                edited_w.write(l)
            in_progress_r.close()
            edited_w.close()
            # *************************
