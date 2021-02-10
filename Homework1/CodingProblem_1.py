# Kyle Dela Pena
# 2038252

from datetime import date


def calculate_age(current_date, birth_date):
    today = current_date
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


print("Birthday Calculator")

print('current Day')
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))

print('Birthday')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))

print("you are ", calculate_age(date(year, month, day), date(birth_year, birth_month, birth_day)), "years old.")
if day == birth_day & month == birth_month & year == birth_year:
    print("Happy Birthday!")
