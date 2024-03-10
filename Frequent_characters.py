#string_input 
OG=input("Enter your string: ")
# printing original string
print("Original input is: ",OG)
#Maximum frequency character in String
freq = {}
for i in OG:
 if i in freq:
  freq[i] += 1
 else:
  freq[i] = 1
res = max(freq, key = freq.get)
print ("The maximum of all characters in String is : " + str(res))
