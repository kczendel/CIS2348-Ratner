# Kyle Dela Pena
# 2038252

month_list = {"JANUARY": "1", "FEBRUARY": "2", "MARCH": "3", "APRIL": "4", "MAY": "5", "JUNE": "6", "JULY": "7",
             "AUGUST": "8", "SEPTEMBER": "9", "OCTOBER": "10", "NOVEMBER": "11", "DECEMBER": "12"}

input_file = open('inputDates.txt', 'r')
output_file = open('parsedDates.txt', 'w')

for line in input_file:
    if line != "-1":
        date = line.split()
        if len(date) >= 3:
            month = date[0]
            day = date[1]
            year = date[2]
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
