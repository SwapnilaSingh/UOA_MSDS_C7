import ast
import sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
len(list(map(lambda x: x if x.startswith('S') else None, input_list)))
