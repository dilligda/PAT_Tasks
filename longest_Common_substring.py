# Function to find the longest common substring between two strings
def longest_common_substring(s1, s2):
    # Get the lengths of the two input strings
    m, n = len(s1), len(s2)
    # Initialize the length of the longest common substring and the longest common substring itself
    longest, lcs = 0, ""
    # Iterate over the length of the first string
    for i in range(m):
        # For each index i in the first string, iterate over the length of the second string
        for j in range(n):
            # For each index j in the second string, iterate over the minimum length of the remaining substrings in the first and second strings
            for k in range(min(m-i, n-j)):
                if s1[i:i+k+1] == s2[j:j+k+1] and k+1 > longest:
                    longest, lcs = k+1, s1[i:i+k+1]
    # Return the longest common substring
    return lcs
s1 = input("Enter your First String:")
s2 = input("Enter your Second String:")
print("Longest common substring:", longest_common_substring(s1, s2))
