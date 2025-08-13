import math

# Function to get and validate float input
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: value must be greater than zero.")
        except ValueError:
            print("Error: please enter a valid numeric value.")

# Function to calculate gallons of paint
def getGallonsOfPaint(square_feet, feet_per_gallon):
    return math.ceil(square_feet / feet_per_gallon)

# Function to calculate labor hours
def getLaborHours(gallons, labor_hours_per_gallon):
    return gallons * labor_hours_per_gallon

# Function to calculate labor cost
def getLaborCost(labor_hours, labor_charge_per_hour):
    return labor_hours * labor_charge_per_hour

# Function to calculate paint cost
def getPaintCost(gallons, paint_price):
    return gallons * paint_price

# Function to get sales tax rate based on state
def getSalesTax(state):
    state = state.upper()
    tax_rates = {
        "CT": 0.06, "MA": 0.0625, "ME": 0.055, "NH": 0.0,
        "RI": 0.07, "VT": 0.06
    }
    return tax_rates.get(state, 0.06)

# Function to display and save cost estimate
def showCostEstimate(gallons, labor_hours, paint_cost, labor_cost, tax, total_cost, last_name):
    output = (
        f"Gallons of paint: {gallons}\n"
        f"Hours of labor: {labor_hours:.1f}\n"
        f"Paint charges: ${paint_cost:.2f}\n"
        f"Labor charges: ${labor_cost:.2f}\n"
        f"Tax: ${tax:.2f}\n"
        f"Total cost: ${total_cost:.2f}\n"
    )

    print(output)

    file_name = f"{last_name}_PaintJobOutput.txt"
    with open(file_name, "w") as f:
        f.write(output)
    print(f"File: {file_name} was created.")

# Main function
def main():
    # Get user inputs
    square_feet = getFloatInput("Enter wall space in square feet: ")
    paint_price = getFloatInput("Enter paint price per gallon: ")
    feet_per_gallon = getFloatInput("Enter feet per gallon: ")
    labor_hours_per_gallon = getFloatInput("How many labor hours per gallon: ")
    labor_charge_per_hour = getFloatInput("Labor charge per hour: ")

    state = input("State job is in: ").strip()
    last_name = input("Customer Last Name: ").strip()

    # Calculations
    gallons = getGallonsOfPaint(square_feet, feet_per_gallon)
    labor_hours = getLaborHours(gallons, labor_hours_per_gallon)
    labor_cost = getLaborCost(labor_hours, labor_charge_per_hour)
    paint_cost = getPaintCost(gallons, paint_price)
    tax_rate = getSalesTax(state)
    tax = (labor_cost + paint_cost) * tax_rate
    total_cost = labor_cost + paint_cost + tax

    # Output
    showCostEstimate(gallons, labor_hours, paint_cost, labor_cost, tax, total_cost, last_name)

# Run the program
if __name__ == "__main__":
    main()
