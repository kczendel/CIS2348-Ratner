# Kyle Dela Pena
# 2038252
from datetime import date

month_list = {"JANUARY": "1", "FEBRUARY": "2", "MARCH": "3", "APRIL": "4", "MAY": "5", "JUNE": "6", "JULY": "7",
             "AUGUST": "8", "SEPTEMBER": "9", "OCTOBER": "10", "NOVEMBER": "11", "DECEMBER": "12"}

input_file = open('inputDates.txt', 'r')
output_file = open('parsedDates.txt', 'w')

today = date.today()
today1 = today.strftime("%Y")
today2 = today.strftime("%m")
today3 = today.strftime("%d")

for line in input_file:
    if line != "-1":
        date = line.split()
        if len(date) >= 3:
            month = date[0]
            day = date[1]
            year = date[2]
        if year > today1 or (year > today1 and month > today2) or (year > today1 and month > today2 and day > today3):
            continue
        if month.upper() in month_list:
            comma = day[-1]
            if comma == ',':
                day = day[:len(day) - 1]
                month_number = month_list[month.upper()]
                ans = month_number + "/" + day + "/" + year
                output_file.write(ans)
                output_file.write("\n")

output_file.close()
input_file.close()

