# Function to get the number of unique characters in a string
def unique_characters(uni):
    unique_chars = set()
    # Iterate through each character in the string
    for uniq in uni:
        unique_chars.add(uniq)
    # Return the length of the set
    return len(unique_chars)
# Get input from the user
uni = input("Enter a string: ")
unique_characters = unique_characters(uni)
print("Unique_characters in given String is :", unique_characters)
