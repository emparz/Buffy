""" SEASON 6 """
import script_methods


# if __name__ == '__main__':
def season6():
    print('reformatting season 6')
    for i in range(1, 23):
        # create the filename with the season and episode number
        filename = 's6e'
        if i < 10:
            filename += '0'
        filename += str(i)

        '''REMOVING BLANK LINES'''
        unedited_r = open('scripts/' + filename + '.txt', 'r')
        in_progress_w = open('progress.txt', 'w')
        for l in unedited_r:
            if not l == '\n':  # if the line is not blank
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

        # """FIX ALL-UPPERCASE SPEAKER"""
        # edited_r = open('scripts_edited/' + filename + '.txt', 'r')
        # in_progress_w = open('progress.txt', 'w')
        # for l in edited_r:
        #     l = methods.fix_uppercase(l)  # change the speaker lines so they're not uppercase
        #     in_progress_w.write(l)  # write fixed line to in progress file
        # edited_r.close()
        # in_progress_w.close()
        # # **** write to edited ****
        # in_progress_r = open('progress.txt', 'r')
        # edited_w = open('scripts_edited/' + filename + '.txt', 'w')
        # for l in in_progress_r:
        #     edited_w.write(l)
        # in_progress_r.close()
        # edited_w.close()
        # # *************************

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
