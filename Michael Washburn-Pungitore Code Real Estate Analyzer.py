# Function to get a valid float input from the user
def getFloatInput(prompt):
    while True:
        try:
            # Get user input and attempt to convert to float
            value = float(input(prompt))
            
            # Ensure the value is greater than zero
            if value <= 0:
                print("Input a number that is greater than 0.")
                continue
            
            return value  # Return the valid float value
        except ValueError:
            # Handles case when input is not a number
            print("Input a valid numeric value.")

# Function to calculate the median manually (no statistics module)
def getMedian(values):
    # Ensure list is sorted
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    if n % 2 == 1:  # Odd number of elements
        return sorted_values[n // 2]
    else:  # Even number of elements
        mid1 = sorted_values[(n // 2) - 1]
        mid2 = sorted_values[n // 2]
        return (mid1 + mid2) / 2

# Main function
def main():
    sales = []  # List to store property sales values
    
    while True:
        # Get property value using getFloatInput function
        sale_price = getFloatInput("Enter property sales value: ")
        sales.append(sale_price)
        
        # Ask if user wants to enter another value
        choice = input("Enter another value Y or N: ").strip().lower()
        if choice not in ['y', 'yes']:
            break  # Exit loop if not 'Y'
    
    # Sort the list for display
    sales.sort()
    
    # Output each property value formatted as currency
    for i, price in enumerate(sales, start=1):
        print(f"Property {i} = ${price:,.2f}")
    
    # Calculate statistics
    minimum = min(sales)
    maximum = max(sales)
    total = sum(sales)
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03  # 3% commission
    
    # Display statistics formatted as currency
    print(f"Minimum:    ${minimum:,.2f}")
    print(f"Maximum:    ${maximum:,.2f}")
    print(f"Total:      ${total:,.2f}")
    print(f"Average:    ${average:,.2f}")
    print(f"Median:     ${median:,.2f}")
    print(f"Commission: ${commission:,.2f}")

# Run the main function
if __name__ == "__main__":
    main()
