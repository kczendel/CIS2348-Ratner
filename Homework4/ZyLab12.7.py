# Kyle Dela Pena
# 2038252

def get_age():
    age = int(input())
    # TODO: Raise excpetion for invalid ages
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")  # raise exception if age is not valid
    return age


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.7  # Calculation of fat-burning heart rate
    return heart_rate


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, fat_burning_heart_rate(age)))
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.")
        print()
