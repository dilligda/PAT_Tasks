def num_words(s):
    # Split the string into a list of words using the split function with no arguments
    return len(s.split())
# Get the input string from the user
s = input("Enter a string: ")
# Print the number of words in the string
print("Number of words:", num_words(s))
