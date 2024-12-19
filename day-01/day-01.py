"""
Solutions for Day 1
- Part 1: 1341714
- Part 2: 27384707
"""

import sys

leftList = []
rightList = []
file = open(sys.argv[1], "r").read()

def setup():
    for i in file.split("\n"):
        n1, n2 = i.split()
        leftList.append(int(n1))
        rightList.append(int(n2))

def partOne():
    total = sum(abs(x - y) for x,y in zip(sorted(leftList), sorted(rightList)))
    print("Part 1 => ", total)
    
def partTwo():
    total = sum(x * rightList.count(x) for x in leftList)
    print("Part 2 => ", total)
    
if __name__ == "__main__":
    setup()
    partOne()
    partTwo()