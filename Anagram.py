def anagram(s1, s2):
    # Check if the lengths of the two strings are equal
    if len(s1) != len(s2):
        # If not
        return False
    # Use the all function and a generator expression to check if the two strings are anagrams
    return all(s1.count(c) == s2.count(c) for c in set(s1))

# Get the two input strings from the user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Print the result
print("The given input strings are anagrams ?", anagram(s1, s2))
