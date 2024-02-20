# Define the limit for the numbers to be printed in the pyramid
finish = 20

# Initialize the current number to be printed
start = 1

# Determine the number of rows needed for the pyramid
# This calculation ensures that all numbers from 1 to 20 can be included
rows = 0
while start <= finish:
    rows += 1
    start += rows

# Reset the current number to start from 1 again
start = 1

# Use nested for loops to print each row of the pyramid
for row in range(1, rows + 1):
    # Print leading spaces for alignment
    for space in range(rows - row):
        print(" ", end="")
    
    # Print numbers in each row
    for num in range(row):
        if start <= finish:
            print(start, end=" ")
            start += 1
        else:
            break  # Exit the loop if limit is reached
    
    # Move to a new line after each row
    print()
