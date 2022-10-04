# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.


the_numb = input("Choose a Number between 1 & 1,000,000: ")

int_numb = int(the_numb)

if int_numb%3 == 0:
    print("This number is divisible by 3")
else:
    print("this nubmer is not divisible by 3")
