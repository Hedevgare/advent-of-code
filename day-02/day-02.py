"""
Solutions for Day 2
- Part 1: 421
- Part 2: 476
"""

import sys

file = open(sys.argv[1], "r").read()
reports = file.split("\n")

def checkReportSafety(report):
    return all(1 <= int(report[i]) - int(report[i - 1]) <= 3 for i in range(1, len(report))) or all(-3 <= int(report[i]) - int(report[i - 1]) <= -1 for i in range(1, len(report)))

def partOne():
    safeReports = 0
    for report in [r.split() for r in reports]:
        # 'True' is equal to 1 and 'False' is equal to 0
        safeReports += checkReportSafety(report)
    print("Part 1 => ", safeReports)
    
def partTwo():
    safeReports = 0
    for report in [r.split() for r in reports]:
        for i in range(len(report)):
            # Check if the report is safe by removing one element at a time
            if checkReportSafety(report[:i] + report[i + 1:]):
                safeReports += 1
                break
    print("Part 2 => ", safeReports)

if __name__ == "__main__":
    partOne()
    partTwo()