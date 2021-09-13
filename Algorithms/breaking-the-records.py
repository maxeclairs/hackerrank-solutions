# problem URL: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# solution

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
# 
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_count, min_count = 0, 0
    max_ = min_ = scores[0]

    for score in scores:
        if max_ < score:
            max_count += 1
            max_ = score

        if min_ > score:
            min_count += 1
            min_ = score

    return max_count, min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
