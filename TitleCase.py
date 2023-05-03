import ast
import sys

#input_str = sys.stdin.read()
# string_list = ast.literal_eval(input_str)


# Type your code here
# define a list of string elements
string_list = ["this is a string", "ANOTHER STRING", "ThIrD sTrInG"]


# function to convert string to title case
def to_title_case(s):
    return s.title()


# use map function to apply to_title_case to each element in the list
title_list = list(map(to_title_case, string_list))

# print the new list with elements in title case
print(title_list)
