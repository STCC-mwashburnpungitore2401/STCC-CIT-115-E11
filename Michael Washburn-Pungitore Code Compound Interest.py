# Get user input
principal = float(input("Enter the starting principal: "))
rate = float(input("Enter the annual interest rate: "))
times_compounded = int(input("How many times per year is the interest compounded? "))
years = int(input("For how many years will the account earn interest? "))

# Calculate compound interest
amount = principal * (1 + (rate / 100) / times_compounded) ** (times_compounded * years)

# Format and display the result
print(f"At the end of {years} years you will have ${amount:,.2f}")
