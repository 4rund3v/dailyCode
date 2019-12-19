"""
What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

fo f in functions:
    print(f())
"""
import copy

functions = []
for i in range(10):
    temp = i
    s = copy.deepcopy(temp)
    functions.append(lambda : s)

for f in functions:
    print(f())