# Function to check if a string is a palindrome
def palindrome_checker(Checker):
  # Remove non-alphanumeric characters and convert to lowercase
  Checker = ''.join(filter(str.isalnum, Checker)).lower()
  # Check if the length of the string is less than or equal to 1
  if len(Checker) <= 1:
        return True
   # Check if the first and last characters are the same
  elif Checker[0] == Checker[-1]:
        # Recursively check the rest of the string
        return palindrome_checker(Checker[1:-1])
  else:
        # Return False if the first and last characters are not the same
        return False
# Test the function
String = input("Enter a string: ")
print(palindrome_checker(String))
