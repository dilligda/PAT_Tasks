# string input from the user
str = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize an empty string
result = ""

# check through each character in the input string
for i in str:
    # Check if character is not a vowel and add it to the result if so
    if i not in vowels:
        result += i

# Print the string with vowels removed
print("String after removing vowels:", result)
