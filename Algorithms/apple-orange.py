# Solution for Apple and Orange
# Problem URL: https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    # the following commented code also works

    # app_dist = [apple + a for apple in apples]
    # ora_dist = [orange + b for orange in oranges]
    # app_count = len([app for app in app_dist if s <= app <= t ])
    # ora_count = len([ora for ora in ora_dist if s <= ora <= t ])
    # print(app_count, ora_count, sep='\n')
    
    print(sum(s <= a + d <= t for d in apples))
    print(sum(s <= b + d <= t for d in oranges))
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
