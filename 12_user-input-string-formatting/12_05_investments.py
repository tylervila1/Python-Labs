# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

years = int(input("how many years are you planning to invest for?  "))

while True:
    investment = float(input('How much is your startin investment? '))
    if 1000 <= investment <= 100000:
        break
    else:
        print("investments must be between $1,000 and $100,000")

apr = 3 / 100
amount = investment

for yr in range(years):
    amount = (amount) * (1.+ apr)
    print(round(amount))