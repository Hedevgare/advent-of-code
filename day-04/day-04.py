"""
Solutions for Day 4
- Part 1: 2593
- Part 2: 1950
"""

import itertools
import sys

file = open(sys.argv[1], "r").read().splitlines()

def partOne():
    total = 0
    nLines = len(file)
    nColumns = len(file[0])
    # l = line, c = column
    for l in range(nLines):
        for c in range(nColumns):
            # Check horizontally
            if c < nColumns - 3 and file[l][c] + file[l][c+1] + file[l][c+2] + file[l][c + 3] in ("XMAS", "SAMX"):
                total += 1
            # Check vertically
            if l < nLines - 3 and file[l][c] + file[l+1][c] + file[l+2][c] + file[l+3][c] in ("XMAS", "SAMX"):
                total += 1
            # Check diagonally (top to bottom)
            if l < nLines - 3 and c < nColumns - 3 and file[l][c] + file[l+1][c+1] + file[l+2][c+2] + file[l+3][c+3] in ("XMAS", "SAMX"):
                total += 1
            # Check diagonally (bottom to top)
            if l < nLines - 3 and c >= 3 and file[l][c] + file[l+1][c-1] + file[l+2][c-2] + file[l+3][c-3] in ("XMAS", "SAMX"):
                total += 1
            
    print("Part 1 =>", total)
    
def partTwo():
    nLines = len(file)
    nColumns = len(file[0])
    total = 0
    # l = line, c = column
    total = sum(
        file[l][c] + file[l+1][c+1] + file[l+2][c+2] in ("MAS", "SAM") 
        and 
        file[l+2][c] + file[l+1][c+1] + file[l][c+2] in ("MAS", "SAM") 
        for c in range(nColumns - 2) 
        for l in range(nLines - 2)
    )
            
    print("Part 2 =>", total)
    
if __name__ == "__main__":
    partOne()
    partTwo()