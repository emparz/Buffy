"""
methods for fixing the scripts, used in season files
"""
import re


# given a line
# if it's not dialogue, add 'scene change:' or 'scene direction:' to the beginning of the line --> return line
# if it is dialogue, look for scene directions within line, marked by (), move directions to own line --> return lines
# used: 1, 2, 3, 4, 5, 6, 7
def add_scene_dir(line):
    # if this is a line of dialogue it will end with a :
    colonIndex = line.find(':')

    # SCENE DIRECTION/CHANGE
    if colonIndex == -1:
        # check if it is a scene change
        if 'Cut to' in line or 'Act' in line or '***' in line or 'Fade to' in line or 'Dissolve to' in line:
            line = 'scene change: ' + line
        else:
            line = 'scene direction: ' + line

    # DIALOGUE
    else:
        speaker = line[:colonIndex]  # the substring up to the colon
        currLine = line
        openParenIndex = currLine.find('(')  # represents the index of an open parenthesis
        # check if parenthesis in speaker
        if 0 < openParenIndex < colonIndex:
            closeParenIndex = currLine.find(')')  # represents the index of a closed parenthesis
            # remove the parenthesis
            currLine = currLine[0:openParenIndex] + currLine[openParenIndex
                                                             + 1:closeParenIndex] + currLine[closeParenIndex + 1:]
            # reset the following values:
            speaker = currLine[:colonIndex]  # the substring up to the colon
            openParenIndex = currLine.find('(')  # represents the index of an open parenthesis

        newLines = ''
        # keeps looping until there are no more open parenthesis
        while not openParenIndex == -1:
            colonIndex = currLine.find(':')
            firstCharacterIndex = colonIndex + 2  # the first character index is 2 after :
            lastCharacterIndex = currLine.find('\n') - 1  # the last character index is right before \n
            closeParenIndex = currLine.find(')')  # represents the index of a closed parenthesis
            # ** we are assuming there IS a closing parenthesis on the same line **

            # if there is dialogue before (, add it to newLines
            if not openParenIndex == firstCharacterIndex:
                # add dialogue before ( to newLines
                newLines += currLine[: openParenIndex - 1] + '\n'

            # add text within () as scene direction to newLines
            newLines += 'scene direction: ' + speaker + ' ' + currLine[openParenIndex + 1: closeParenIndex] + '\n'

            # if there is dialogue after ), add the speaker and set it to currLine, otherwise make currLine blank
            if not closeParenIndex == lastCharacterIndex:
                currLine = speaker + ': ' + currLine[closeParenIndex + 2:]
            else:
                currLine = ''

            # check to see if there is another set of parenthesis
            openParenIndex = currLine.find('(')

        # once we have exited the loop, add whatever is left in currLine to newLines
        newLines += currLine
        line = newLines
    return line


# given a line
# if it's not dialogue, add 'scene change:' or 'scene direction:' to the beginning of the line --> return line
# if it is dialogue, look for scene directions within line (and within speaker!), marked by (),
# move directions to their own line --> return lines
# used: 3, 4
def fix_dialogue_and_dir(line):
    # if this is a line of dialogue it will have a :
    colonIndex = line.find(':')

    # if there is no : it is not a character's line
    if colonIndex == -1:
        # check if it is a scene change
        if 'Cut to' in line or 'Act' in line or '***' in line or 'Fade to' in line or 'Dissolve to' in line:
            newLine = 'scene change: ' + line
        else:
            newLine = 'scene direction: ' + line

    # we are looking at a line of dialogue
    else:
        # split the dialogue at the colon
        temp = line.split(':', 1)

        # the first half has the speaker and poss scene dirs in (), initialize blank speaker
        firstHalf = temp[0]
        # the second half has the line of dialogue and possibly multiple scene dirs in ()
        secondHalf = temp[1]

        # get rid of all newlines
        firstHalf = firstHalf.strip()
        secondHalf = secondHalf.strip()

        # check if there is scene direction with the first half
        # IS scene direction
        if not firstHalf.find('(') == -1:
            # split first half into speaker and scene dir
            temp = firstHalf.split('(', 1)
            speaker = temp[0].strip()  # remove trailing whitespace
            sceneDir = temp[1]
            # remove second ')' from sceneDir
            sceneDir = sceneDir[:sceneDir.find(')')]
            # first half is now a line of scene direction then a newline char
            firstHalf = 'scene direction: ' + speaker + ' ' + sceneDir + '\n'

        # NO scene direction
        else:
            speaker = firstHalf
            # first half is now blank
            firstHalf = ''

        # get rid of " "
        temp = secondHalf.split('\"')
        secondHalf = temp[1]

        # currSceneDir signifies if the second half starts with parenthesis
        # AKA whether the first element of splitAtParens is sceneDir
        currSceneDir = False
        if secondHalf.find('(') == 0:
            currSceneDir = True

        # split the second half into a list at the beginning parenthesis
        splitAtParens = [j for j in re.split(r'[()]', secondHalf) if j != ' ']

        # reset second half to blank
        secondHalf = ''

        # loop through the list of scene directions and dialogue
        for part in splitAtParens:
            # part = scene description
            if part == '':
                pass
            elif currSceneDir:
                secondHalf += 'scene direction: ' + speaker + ' ' + part + '\n'
                currSceneDir = False
            # part = dialogue
            else:
                part = part.strip()
                secondHalf += speaker + ': ' + part + '\n'
                currSceneDir = True

        newLine = firstHalf + secondHalf
    return newLine


# given a line
# if the line does NOT end in punctuation (or the punctuation is preceded by a title) --> strip /n and return line
# otherwise --> return line unchanged
# used: 1, 2, 3, 4, 5, 6
def fix_line_breaks(line):
    newLineIndex = line.find('\n')  # the index of /n
    lastCharacterIndex = newLineIndex - 1  # the last character index is right before /n
    lastCharacter = line[lastCharacterIndex: newLineIndex]  # python substrings start included, end not

    # if the last character of a line is NOT punctuation, then assume it was a continuation from the previous line
    if not (lastCharacter == '.' or lastCharacter == '?' or lastCharacter == '!'
            or lastCharacter == '.\'' or lastCharacter == '?\'' or lastCharacter == '!\''
            or lastCharacter == '.\"' or lastCharacter == '?\"' or lastCharacter == '!\"'
            or lastCharacter == ')' or lastCharacter == '*'):
        line = line[:newLineIndex]
        line += ' '

    # check for exceptions (if the last word of a line is Mr., Dr., etc)
    if lastCharacter == '.':
        lastSpaceIndex = line.rfind(' ')  # the index of the last space in the line
        lastWord = line[lastSpaceIndex + 1: newLineIndex]
        if lastWord == 'Dr.' or lastWord == 'Mr.' or lastWord == 'Mrs.' or lastWord == 'Det.':
            # remove the newline character and add a space
            line = line[:newLineIndex]
            line += ' '
    return line


# given two lines
# if the line #1 has a speaker and line #2 does NOT, check if line #2 is a continuation of dialogue or scene direction
# it's more dialogue if line #2 has 1st/2nd person pronouns or starts with open parenthesis
# --> strip /n on line #1 and return
# otherwise --> return line #1 unchanged
# used: 1, 2, 3, 4
def fix_unclear_punc(line1, line2):
    newLineIndex = line1.find('\n')  # the index of /n
    # check if line1 is dialogue and line2 is NOT dialogue
    colonIndex1 = line1.find(':')
    colonIndex2 = line2.find(':')
    if not colonIndex1 == -1 and colonIndex2 == -1:
        # if the line2 contains "I ", "we ", "We", "we're ", "We're " it's more dialogue
        if 'I ' in line2 or \
                'we ' in line2 or 'We ' in line2 or \
                'we\'re ' in line2 or 'We\'re ' in line2 or \
                'you ' in line2 or 'You ' in line2 or \
                'you\'re ' in line2 or 'You\'re ' in line2:
            line1 = line1[:newLineIndex]
            line1 += ' '
        # if line2 starts with an open parenthesis, it's more dialogue
        indexOfOpenParen = line2.find('(')
        if indexOfOpenParen == 0:
            line1 = line1[:newLineIndex]
            line1 += ' '
    return line1


# given a line
# if the line is surrounded by () --> remove () and return line
# otherwise --> return line unchanged
# used: 4 (episode 9)
def remove_parenthesis(line):
    newLineIndex = line.find('\n')  # the index of /n
    lastCharacterIndex = newLineIndex - 1  # the last character index is right before /n
    lastCharacter = line[lastCharacterIndex: newLineIndex]  # python substrings start included, end not
    firstCharacter = line[0]
    if firstCharacter == '(' and lastCharacter == ')':
        # return line without parenthesis
        return line[1: lastCharacterIndex] + '\n'
    return line


# given a line
# if it's a cut --> return ''
# if line is all uppercase --> figure out if it's a character speaking or scene directions, fix and return line
# otherwise --> return line unchanged
# used: 5, 7 (when the speaker and dialogue are on different lines)
def change_dialogue_style(line):
    # if the line is "Cut to:", delete line
    if line == 'Cut to:\n':
        return ''
    # if the line is all uppercase
    if line.isupper():
        firstCharacter = line[0:1]  # the first character of the line
        if firstCharacter == '*':
            return line
        elif firstCharacter.isdigit():  # if the first character is a digit, it is a scene change line
            return 'cut to ' + line.title()
        elif 'CUT TO' in line or 'DISSOLVE TO' in line or 'CUT WITH' in line:
            return line.title()
        else:
            newLineIndex = line.find('\n')  # the index of /n
            line = line.title()
            return line[:newLineIndex] + ': '  # return line with proper casing, no newline, and a colon
    return line
