#!/bin/python3
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # ;)
    v = -63
    for i in range(1, 5):
        for j in range(1, 5):
            v = max(v, sum(arr[i-1][(j-1):(j+2)]) + arr[i][j] + sum(arr[i + 1][(j-1):(j+2)]))   
    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
