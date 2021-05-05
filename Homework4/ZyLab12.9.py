# Kyle Dela Pena
# 2038252

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
    except Exception as ex:
        age = 0

    print('{} {}'.format(name, age))
    # Get next line
    parts = input().split()
    name = parts[0]