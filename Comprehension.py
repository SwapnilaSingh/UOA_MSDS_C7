L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]
L3 = []
for i in range(len(L1)):
    L3.append(L1[i] - L2[i])
print(L3)

# using list comprehension
L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]
L3 = [L1[i] - L2[i] for i in range(0, len(L1))]
print(L3)

ordinary_dict = {}

for i in range(2, 21):
    if i % 2 == 0:
        ordinary_dict[i] = i ** 2

print(ordinary_dict)
# With Comprehension
updated_dict = {i: i ** 2 for i in range(2, 21) if i % 2 == 0}
print(updated_dict)

# Coding Questions

import ast
import sys

n = int(input())
L3 = [i ** 2 for i in range(1, n + 1)]
print(L3)

# Coding question2
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_vowel = [word for word in input_list if word[0] in 'aeiou']

print(list_vowel)
