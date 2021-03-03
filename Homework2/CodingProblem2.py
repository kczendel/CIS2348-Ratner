month_list = {"January":"1", "February":"2", "March":"3", "April":"4", "May":"5", "June":"6", "July":"7",
             "August":"8", "September":"9", "October":"10", "November":"11", "December":"12"}

input_file = open(input(), 'r')
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
