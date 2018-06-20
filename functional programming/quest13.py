### itertools.
#  count: counts up infinitely from a value
#  cycle: infintely iterates through an iterable
#  repeat: repeats an object, either infinitely or a specify number of times.
# takewhile: takes items from an iterable while a predicate function remains true.
# chain: combines several iterables into one long one;
# accumulate- return a running total of values in an iterable.
# product, permuation: combinatoric functions

from itertools import *

for i in count(3):
    print(i)
    if i >=11:
        break


###
print("\n")
#####

""" 
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

 """

###
print("\n")
#####

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))