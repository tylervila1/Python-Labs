# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

random_word = input("Type a Random Word: ")
random_word = str.lower(random_word)
print(random_word.index("t"))