import ast

num = "123450"
# ast.literal.eval(input())
rev_number = 0
l = len(num)
number = int(num)
for i in range(l, 0, -1):

    rev_number = rev_number + (number % 10) * 10 ** (i-1)
    number = number//10

print(rev_number)
