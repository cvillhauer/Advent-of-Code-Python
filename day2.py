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

LINES = CONTENT.split('\n')
CHECKSUM1 = 0
CHECKSUM2 = 0

#PART 1
NUMBERS = []
SMALLEST = 0
LARGEST = 0
for line in LINES:
    NUMBERS = line.split(' ')
    if len(NUMBERS) <= 1:
        NUMBERS = line.split('\t')
    for number in NUMBERS:
        number = int(number)
        if SMALLEST == 0 or number < SMALLEST:
            SMALLEST = number
        if LARGEST == 0 or number > LARGEST:
            LARGEST = number
    CHECKSUM1 = CHECKSUM1 + (LARGEST - SMALLEST)
    SMALLEST = 0
    LARGEST = 0

#PART 2
NUMBERS = []
for line in LINES:
    NUMBERS = line.split(' ')
    if len(NUMBERS) <= 1:
        NUMBERS = line.split('\t')
    for number in NUMBERS:
        number = int(number)
        for divisor in NUMBERS:
            divisor = int(divisor)
            if number % divisor == 0 and number / divisor != 1:
                CHECKSUM2 = CHECKSUM2 + int((number / divisor))
                break


print(" ")
print("Solving...")
print("Part 1:", CHECKSUM1)
print("Part 2:", CHECKSUM2)
