#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    low = scores[0]
    high = scores[0]
    low_count = 0
    high_count = 0

    for i in scores:
        if i < low:
            low = i
            low_count += 1

        elif i > high:
            high = i
            high_count += 1

    return high_count, low_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
