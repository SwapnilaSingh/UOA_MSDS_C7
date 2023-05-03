import ast

n = ast.literal_eval(input())
for i in range(0, n):
    for k in range(n - 1, i, -1):
        print(" ", end='')
    print("*", end='')
    for k in range(0, i):
        print("_*", end='')
    print()

