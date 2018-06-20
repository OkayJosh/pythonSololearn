### Set are data structures, similar to lists or dictionaries. They are created using curly braces, or the set fuction

num_set = {1,2,3,4,5}
word_set = set(['spam','eggs','sausage'])

print(3 in num_set)
print('spam' not in word_set)

## To create an empty set, you must use set(), as {} creates an empty dictionary
rint('\n')
## set and list share similar functions. instead of using append to add to a set use add

nums = {1,2,3,4,5,6}
print(nums)
nums.add(-7)
print(nums)

## Mathematical Operators in set
print('\n')

first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)