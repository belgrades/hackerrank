#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# https://www.hackerrank.com/challenges/bfsshortreach/problem

# Complete the bfs function below.
def bfs(n, m, edges, s):
    g = defaultdict(list)
    for i, j in edges:
        g[i].append(j)
        g[j].append(i)

    q, distances = [], [-1]*n
    q.append((s, 0))
    distances[s-1] = 0
    n = 1

    while n > 0:
        i, d = q[0]
        q.remove((i, d))
        n -= 1
        
        if distances[i-1] <= 0:
            distances[i-1] = d
        else:
            continue

        for v in g[i]:
            if distances[v-1] < 0:
                n += 1
                q.append((v, d+6))

    r = []

    for (i, v) in enumerate(distances):
        if i == (s-1):
            continue
        else:
            r.append(v)
    
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
