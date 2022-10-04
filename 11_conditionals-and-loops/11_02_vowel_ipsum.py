# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

a = (lorem_ipsum.count('a'))
numb_a = float(a)
e = (lorem_ipsum.count('e'))
numb_e = float(e)
i = (lorem_ipsum.count('i'))
numb_i = float(i)
o = (lorem_ipsum.count('o'))
numb_o = float(o)
u = (lorem_ipsum.count('u'))
numb_u = float(u)
print(numb_a + numb_e + numb_i + numb_u)