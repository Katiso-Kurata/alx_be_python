

def main():
    # Prompt the user for the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user for the second number
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user for the operation
    operation = input("Choose the operation (+, -, *, /): ").strip()
    
    # Perform calculation based on the operation
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                result = "Cannot divide by zero."
            else:
                result = num1 / num2
        case _:
            result = "Invalid operation."

    # Display the result
    print(f"The result is: {result}")

# Call the main function
if __name__ == "__main__":
    main()
