# Input the amount in cents
cents = int(input("Enter the amount in cents: "))

# Calculate the number of dollars and update the remaining cents
dollars = cents // 100
cents %= 100

# Calculate the number of quarters and update the remaining cents
quarters = cents // 25
cents %= 25

# Calculate the number of dimes and update the remaining cents
dimes = cents // 10
cents %= 10

# Calculate the number of nickels and update the remaining cents
nickels = cents // 5
cents %= 5

# The remaining cents are the number of pennies
pennies = cents

# Print the result
print(f" Dollars: {dollars}\n Quarters: {quarters}\n Dimes: {dimes}\n Nickels: {nickels}\n Pennies: {pennies}")