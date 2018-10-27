#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    :param s: Initial point Sam's house
    :param t: End point Sam's house
    :param a: Location of apple tree
    :param b: Location of orange tree
    :return: Number of oranges and apples in safe zone
    """
    
    print(sum(map(lambda x: int(a + x >= s and a + x <= t), apples)))
    print(sum(map(lambda x: int(b + x >= s and b + x <= t), oranges)))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
