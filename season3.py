""" SEASON 3 """
import script_methods


# if __name__ == '__main__':
def season3():
    print('reformatting season 3')
    for i in range(1, 23):
        '''ALL EPISODE STUFF'''
        # create the filename with the season and episode number
        filename = 's3e'
        if i < 10:
            filename += '0'
        filename += str(i)

        '''REMOVE BLANK LINES + LOSE LINE BREAKS (A)'''
        unedited_r = open('scripts/' + filename + '.txt', 'r')
        in_progress_w = open('progress.txt', 'w')
        for l in unedited_r:
            if not l == '\n':  # if the line is not blank
                if not i == 18 and not i == 22:  # 18 and 22 don't have line breaks
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

        '''FIX DIALOGUE AND DIRECTION (C)'''
        # episode 22 is weird and needs its own method
        if i == 22:
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

        # the rest of the episodes in this season are the same as 1 and 2
        else:
            '''FIX WEIRD LINE BREAKS (A)'''
            if not i == 18:
                edited_r = open('scripts_edited/' + filename + '.txt', 'r')
                in_progress_w = open('progress.txt', 'w')
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

            '''ADD SCENE DIRECTIONS (A, B)'''
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
