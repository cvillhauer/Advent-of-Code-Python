#http://adventofcode.com/2017/day/2
#For each row, determine the difference between the largest value and the smallest value
#The checksum is the sum of all of these differences.
#then

import argparse

#from https://stackoverflow.com/a/39730702/3053913
PARSER = argparse.ArgumentParser()
PARSER.add_argument("--file", "-f", type=str, required=True)
ARGS = PARSER.parse_args()
INPUT = ARGS.file
with open(INPUT, 'r') as content_file:
    CONTENT = content_file.read()

SMALLEST = 0
LARGEST = 0
CURRENT = ""
CHECKSUM1 = 0
CHECKSUM2 = 0
CONTENT = CONTENT + '\n' #Otherwise final character will not be processed!

#PART 1
for char in CONTENT:
    if char == '\n' or char == '\t' or char == ' ':
        if SMALLEST == 0 or int(CURRENT) < SMALLEST:
            SMALLEST = int(CURRENT)
        if LARGEST == 0 or int(CURRENT) > LARGEST:
            LARGEST = int(CURRENT)
        CURRENT = ""
        if char == '\n':
            CHECKSUM1 = CHECKSUM1 + (LARGEST - SMALLEST)
            SMALLEST = 0
            LARGEST = 0
            print("CHECKSUM is now ", CHECKSUM1)
    else:
        CURRENT = CURRENT + char

#PART 2



print(" ")
print("Solving...")
print("Part 1:", CHECKSUM1)
print("Part 2:", CHECKSUM2)
