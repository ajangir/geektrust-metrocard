import sys
from starter import *

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('input file name not given')
        raise Exception("File path not entered")
    
    try:
        input_file = sys.argv[1]
        f = open(input_file, 'r')
        lines = f.readlines()
    except:
        print('input_file_name could not be opened')
        raise Exception("given input file not opened")
    parseInput(lines)
    runLoop(lines)