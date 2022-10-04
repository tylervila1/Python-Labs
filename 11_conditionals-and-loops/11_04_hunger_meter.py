# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.


hunger = input("What is your hunger level 1-10: ")

hunger_level  = float(hunger)

if hunger_level <= 3:
    print("Eat an Apple")
elif hunger_level > 3 < 6:
    print("Eat a Pizza")
else:
    print("you need to order something bigger")
