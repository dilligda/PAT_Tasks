count_a, count_e, count_i, count_o, count_u = 0, 0, 0, 0, 0 #  initalize count
input="Guvi Geeks Network private limited" # String input 
for char in input: # Loop through each character in the input
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
      count_u += 1
#Calculate the total number of vowels in the given input
Total_vowels = count_a+count_e+count_i+count_o+count_u 
# Print the total vowels and individual counts
print("Total number of vowels:", Total_vowels) 
print("a:", count_a)
print("e:", count_e)
print("i:", count_i)
print("o:", count_o)
print("u:", count_u)
