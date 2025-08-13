# Function to get validated numeric input
def get_positive_number(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
            if allow_zero and value >= 0:
                return value
            elif not allow_zero and value > 0:
                return value
            else:
                print("Error: Please enter a positive number." if not allow_zero else "Error: Value must be zero or greater.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")

# Get inputs with validation
fltDeposit = get_positive_number("What is the original deposit (positive value): ")
fltRatePercent = get_positive_number("What is the interest rate percentage (positive value): ")
intMonths = int(get_positive_number("What is the number of months (positive value): "))
fltGoal = get_positive_number("What is the goal amount (can enter 0 but not negative): ", allow_zero=True)

# Convert interest rate percentage to monthly rate
fltMonthlyRate = (fltRatePercent / 100) / 12

# Display monthly balances
fltBalance = fltDeposit
for month in range(1, intMonths + 1):
    fltBalance += fltBalance * fltMonthlyRate
    print(f"Month {month}: Account Balance is ${fltBalance:,.2f}")

# If a goal is set (> 0), calculate how many months to reach it
if fltGoal > 0:
    fltGoalBalance = fltDeposit
    intGoalMonths = 0
    while fltGoalBalance < fltGoal:
        fltGoalBalance += fltGoalBalance * fltMonthlyRate
        intGoalMonths += 1
    print(f"\nIt will take {intGoalMonths:,} months to reach the goal of ${fltGoal:,.2f}")
