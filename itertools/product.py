from itertools import product

def read(): return list(map(int, input().split()))

A = read()
B = read()

print(" ".join(["("+str(x)+", "+str(y)+")" for x,y in product(A, B)]))
