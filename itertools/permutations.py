from itertools import permutations

word, n = input().split()

for x in permutations(sorted(word), int(n)):
    print("".join(x))
