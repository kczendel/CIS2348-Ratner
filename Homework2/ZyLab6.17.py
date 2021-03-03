# Kyle Dela Pena
# 2038252

word = input()
password = ''

for x in word:
    if x == 'i':
        password += "!"
    elif x == 'a':
        password += "@"
    elif x == 'm':
        password += "M"
    elif x == 'B':
        password += "8"
    elif x == 'o':
        password += "."
    else:
        password += x

password += "q*s"
print(password)
