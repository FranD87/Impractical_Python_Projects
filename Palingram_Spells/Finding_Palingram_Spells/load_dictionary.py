'''Load a text file as a list.

Arguements:
-text file name (and directory path, if needed)

Exceptions:
-IO Error if filename not found.


Returns:
    -A list of all words in a text file in lower case.

Requires-import sys
'''

import sys

def load(file):
    """Open a text file and return as lower case string"""
    try:
        with open('dict.txt') as file:
            loaded_txt = file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return  loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
