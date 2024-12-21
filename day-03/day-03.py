"""
Solutions for Day 3
- Part 1: 190604937
- Part 2: 82857512
"""

import re
import sys

file = open(sys.argv[1], "r").read()

def partOne():
    total = sum(int(mul.group(1)) * int(mul.group(2)) for mul in re.finditer(r"mul\((\d+),(\d+)\)", file))
    print("Part 1 =>", total)
    
def partTwo():
    enabled = True
    total = 0
    for mul in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", file):
        match mul.group(0):
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                if enabled:
                    total += int(mul.group(1)) * int(mul.group(2))
                    
    print("Part 2 =>", total)

if __name__ == "__main__":
    # partOne()
    partTwo()