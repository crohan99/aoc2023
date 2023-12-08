import sys
import requests
import os

"""
Carson Rohan
AOC 2023
Module for creating necessary day files and getting input because I'm lazy.
"""

STATUS_OK = 200
AOC_INPUT_URL = 'https://adventofcode.com/2023/day/?/input'
URL = 'https://adventofcode.com/2023'
# your info here
COOKIES = {
    'ru': 'userstring',
    'session':
        '53616c7465645f5f1c45816137d09dc77da81d740eda4d4b0c53727a2f5dc1aabe0194b1987f54714343e5fcbe668139e5e9f892a80caac8b71e8d4aec49f035'
}

INPUT_SIZE = 2
DAY_TEMPLATE = ('"""\nCarson Rohan\nAOC 2023\nDay ?: Name_of_puzzle\n"""\n\nfrom os import path\n\n'
                'FILE_NAME = \'d?i.txt\'\n\n\n'
                'def main():\n\n\twith open(path.join(path.dirname(path.abspath(__file__)), FILE_NAME)) '
                'as file_input:\n\t\tpuzzle_input = file_input.readlines()\n\t\treturn 0\n\n\ndef part1():\n\t'
                'return 0\n\n\ndef part2():\n\treturn 0\n\n\nif __name__ == \'__main__\':\n\tmain()')

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
    inputFile = os.path.join(dayDir, 'd%s.txt'%(day))
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
