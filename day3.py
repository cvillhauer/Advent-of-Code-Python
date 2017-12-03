#http://adventofcode.com/2017/day/3
#In a spiral of memory locations, find the distance of the shortest path
#Then, in a spiral of memory locations, each position is the sum of its neighbors

import sys

if len(sys.argv) > 1:
    INPUT = sys.argv[1]
else:
    INPUT = "1024"

INPUT = int(INPUT)
DISTANCE1 = 0
DISTANCE2 = 0

#I had to draw out this one on paper and count and think.
#But I noticed a pattern: You move right by n, up by n,
#then left by n+1, down by n+2, then right by n+3, up by n+3,
#and so on and so forth until you've done INPUT steps.
#If you take the difference between your total Lefts and your total Rights
#Then add the differene between your total Ups and your total Downs
#That should be the answer??

#PART1
RIGHTS = 0
UPS = 0
LEFTS = 0
DOWNS = 0
i = 1
STEPS = 1
SIDEWAYS = True
while i < INPUT:
    if i + STEPS > INPUT:
        STEPS = INPUT - i
    if SIDEWAYS:
        if RIGHTS > LEFTS:
            LEFTS = LEFTS + STEPS
            i = i + STEPS
            SIDEWAYS = False
        else:
            RIGHTS = RIGHTS + STEPS
            i = i + STEPS
            SIDEWAYS = False
    else:
        if UPS > DOWNS:
            DOWNS = DOWNS + STEPS
            i = i + STEPS
            STEPS = STEPS + 1
            SIDEWAYS = True
        else:
            UPS = UPS + STEPS
            i = i + STEPS
            STEPS = STEPS + 1
            SIDEWAYS = True

DISTANCE1 = abs(UPS - DOWNS) + abs(LEFTS - RIGHTS)

#PART2
i = 1



print(" ")
print("Solving...")
print("Part 1:", DISTANCE1)
print("Part 2:", DISTANCE2)
