from psychopy import core, event

def proceedOrQuit(win, keys = ['space', 'escape']):
    input = event.waitKeys(keyList = keys)
    if 'escape' in input:
        print input
        win.close()
        core.quit()
    return input

# function for converting key names to nominal responses
def translate(x):
    options = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'tab': -0.5, # x-coordinate for "left" response
        'backslash': 0.5, # x-coordinate for "right" response
        'y': 'y',
        'n': 'n',
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'm': 'm',
        'f': 'f',
        'space': 'space', #NEXT/SPACE button
        'escape': 'escape',
        'lshift': 'lshift' #choosing VOWEL/SHIFT button
    }
    if not x in options:
        return '`'
    return options[x]
