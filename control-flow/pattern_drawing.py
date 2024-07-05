# pattern_drawing.py

def main():
    # Prompt the user to enter a positive integer for the size of the pattern
    size = int(input("Enter the size of the pattern: "))
    
    # Initialize the row counter
    row = 0
    
    # Use a while loop to iterate through each row of the pattern
    while row < size:
        # Use a for loop to print asterisks (*) side by side
        for _ in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment the row counter
        row += 1

# Call the main function
if __name__ == "__main__":
    main()
