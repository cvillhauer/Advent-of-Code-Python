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

print(INPUT)
print(CONTENT)

CHECKSUM1 = 0
CHECKSUM2 = 0


#PART 1


#PART 2



print(" ")
print("Solving...")
print("Part 1:", CHECKSUM1)
print("Part 2:", CHECKSUM2)