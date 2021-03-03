# Kyle Dela Pena
# 2038252

string = input()
original = ""
reverse = ""
for i in range(len(string)):
   if string[i].isalpha():
       original += string[i].lower()
       reverse = string[i].lower() + reverse

if original == reverse:
   print(string + " is a palindrome")
else:
   print(string + " is not a palindrome")