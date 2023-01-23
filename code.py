from collections import Counter, OrderedDict #OrderedDict is a dict subclass that preserves the order in which key-value pairs, commonly known as items, are inserted into the dictionary
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())



'''
we need to develop a python program that can read an integer and string as an input separated with each line, 
and then we need to print the number of occurrence of the distinct word in the given string on the output screen.
'''

