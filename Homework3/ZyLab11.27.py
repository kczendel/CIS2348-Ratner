# Kyle Dela Pena
# 2038252

def roster():
    global data
    print("ROSTER")
    for i in sorted(data.keys()):
        print("Jersey number: " + str(i) + ", Rating: " + str(data[i]))


def addPlayer():
    global data
    jersey_number = int(input("Enter a new player's jersey number:\n"))
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number in data)):
        if (jersey_number in data):
            print("Already added")
        else:
            print("Enter values between 0-99 (inclusive)")
        jersey_number = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter player's rating:\n"))
    while (rating < 1 or rating > 9):
        print("Enter values between 1-9 (inclusive)")
        rating = int(input("Enter player's rating:\n"))
    data[jersey_number] = rating


def removePlayer():
    global data
    jersey_number = int(input("Enter a jersey number:\n"))
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number not in data)):
        if (jersey_number < 0 or jersey_number > 99):
            print("Enter values between 0-99 (inclusive)")
        else:
            print("Jersey number not added")
        jersey_number = int(input("Enter a jersey number:\n"))
    del data[jersey_number]


def updatePlayer():
    global data
    jersey_number = int(input("Enter a jersey number:\n"))
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number not in data)):
        if (jersey_number < 0 or jersey_number > 99):
            print("Enter values between 0-99 (inclusive)")
        else:
            print("Jersey number not added")
        jersey_number = int(input("Enter a jersey number:\n"))
    rating = int(input("Enter a new rating for player:\n"))
    while (rating < 1 or rating > 9):
        print("Enter values between 1-9 (inclusive)")
        rating = int(input("Enter a new rating for player:\n"))
    data[jersey_number] = rating


def aboveRating():
    global data
    rating = int(input("Enter a rating:\n"))
    print("\nABOVE " + str(rating))
    for i in sorted(data):
        if (data[i] > rating):
            print("Jersey number: " + str(i) + ", Rating: " + str(data[i]))

data = {}
i = 0

for i in range(5):
    jersey_number = int(input("Enter player " + str(i + 1) + "'s jersey number:\n"))
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number in data)):
        if (jersey_number in data):
            print("Already added")
        else:
            print("Enter values between 0-99 (inclusive)")
        jersey_number = int(input("Enter player " + str(i + 1) + "'s jersey number:\n"))
    rating = int(input("Enter player " + str(i + 1) + "'s rating:\n"))
    while (rating < 1 or rating > 9):
        print("Enter values between 1-9 (inclusive)")
        rating = int(input("Enter player " + str(i + 1) + "'s rating:\n"))
    data[jersey_number] = rating
    print("")

roster()

choice = ""
while (True):
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

    choice = input("\nChoose an option:\n")
    choice = choice.lower()

    if (choice == "a"):
        addPlayer()
    elif (choice == "d"):
        removePlayer()
    elif (choice == "u"):
        updatePlayer()
    elif (choice == "r"):
        aboveRating()
    elif (choice == "o"):
        roster()
    elif (choice == "q"):
        break
    else:
        print("Wrong choice")