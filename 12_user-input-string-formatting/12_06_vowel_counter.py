# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

string_input =  str.lower(input("Say something funny: "))

vowel_list = list('aeiou')

vowel_count = 0

for phrase in string_input:
    for l in phrase:
        if l == 'a':
            acount += 1
        if l == 'e':
            ecount += 1
        if l == 'i':
            icount += 1
        if l == 'o':
            ocount += 1
        if l == 'u':
            ucount += 1
    print(acount)
