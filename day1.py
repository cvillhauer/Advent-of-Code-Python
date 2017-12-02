#http://adventofcode.com/2017/day/1
#find the sum of all digits that match the next digit in the list
#then, consider the digit halfway around the circular list

import sys

if len(sys.argv) > 1:
    INPUT = sys.argv[1]
else:
    INPUT = "1212"

if len(INPUT) % 2 != 0:
    print("Truncating invalid input...")
    INPUT = INPUT[:-1]

SUM1 = 0
SUM2 = 0
INPUTINT = map(int, INPUT)
ARRAY = []
for i in INPUTINT:
    ARRAY.append(i)
LENGTH = len(ARRAY)
HALFWAY = int(len(ARRAY) / 2)

#PART 1
CURRENT = 0
COMPARE = 0
for CURRENT in range(0, LENGTH):
    if CURRENT == 0:
        COMPARE = LENGTH - 1
    else:
        COMPARE = CURRENT - 1
    if ARRAY[CURRENT] == ARRAY[COMPARE]:
        SUM1 = SUM1 + ARRAY[CURRENT]

#PART 2
CURRENT = 0
COMPARE = 0
for CURRENT in range(0, LENGTH):
    if CURRENT == 0:
        COMPARE = LENGTH - HALFWAY
    else:
        COMPARE = CURRENT - HALFWAY
    if ARRAY[CURRENT] == ARRAY[COMPARE]:
        SUM2 = SUM2 + ARRAY[CURRENT]


print(" ")
print("Solving...")
print("Part 1:", SUM1)
print("Part 2:", SUM2)
