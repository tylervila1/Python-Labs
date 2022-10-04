# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


#random_phrase = input("Say something random: ")
#first_letter = random_phrase[0]

#updated_phrase = random_phrase.replace(first_letter, "z")

#print("did you say " + random_phrase + "?" + " or did you say " + updated_phrase + "?")



#Mike Tyson Cypher
from time import sleep
phrase = input("Please Type what you want to trasnlate to Mike Tyson language: ")
phrase_mod = str.lower(phrase)

translated = phrase_mod.replace("s", "th")

print("Your translation is being processed please wait...... \n ")
sleep(3)
print("......")
sleep(2)
print("......")
sleep(1)
print("......")
sleep(1)
print(translated + " \n \nThanks for using Iron Mike Translator.. Have a Good Day\n \n  ")