import sys
import requests
import os

"""
Carson Rohan
AOC2022
Module for creating necessary day files and getting input because I'm lazy.
"""

STATUS_OK = 200
AOC_INPUT_URL = 'https://adventofcode.com/2022/day/?/input'
URL = 'https://adventofcode.com/2022'
COOKIES = {
    'ru': 'userstring',
    'session': 'cookiestring'
}

INPUT_SIZE = 2
DAY_TEMPLATE = '"""\nCarson Rohan\nAOC2022\nDay ?: Name_of_puzzle\n"""\n\nimport os\n\nFILE_NAME = \'d?i.txt\'\n\ndef main():\n\n\twith open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:\n\t\tfileInput = input.readlines()\n\t\treturn 0\n\nclass Part1:\n\n\tdef blah():\n\t\treturn 0\n\nclass Part2:\n\n\tdef blah():\n\t\treturn 0\n\nif __name__ == \'__main__\':\n\tmain()'

def main():

    # error checking
    if (len(sys.argv) != INPUT_SIZE):
        print('Usage: %s <day #>'%(os.path.basename(__file__)))
        return

    if (not sys.argv[INPUT_SIZE - 1].isdigit()):
        print('Input must be integer')
        return

    # prep for 
    day = sys.argv[INPUT_SIZE - 1]

    cookiesForHeader = ''.join(f'{key}={value};' for key, value in COOKIES.items())[:-1]

    header = {
        'Accept': '*/*',
        'Host': 'Me',
        'User-Agent': 'Python/3.6.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': cookiesForHeader
    }

    response = requests.get(AOC_INPUT_URL.replace('?', day), headers=header)

    if (response.status_code != STATUS_OK):
        print(response.status_code)
        return

    # create dirs/files
    parentDir = os.path.dirname(os.path.abspath(__file__))
    dayDir = os.path.join(parentDir, '../d%s'%(day))
    inputFile = os.path.join(dayDir, 'd%si.txt'%(day))
    dayFile = os.path.join(dayDir, 'd%s.py'%(day))
    testInputFile = os.path.join(dayDir, 'testinput.txt')
    template = DAY_TEMPLATE.replace('?', str(day))

    if (not os.path.exists(dayDir)):
        os.mkdir(dayDir)

    if (not os.path.exists(inputFile)):
        with open(inputFile, 'w') as input:
            input.write(response.text)

    if (not os.path.exists(dayFile)):
        with open(dayFile, 'w') as p1:
            p1.write(template)

    if (not os.path.exists(testInputFile)):
        open(testInputFile, 'w')

    return 0

if __name__ == '__main__':
    main()
