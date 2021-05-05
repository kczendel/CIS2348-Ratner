# Kyle Dela Pena
# 2038252

# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(int_list):
    for i in range(len(int_list)-1):
        ind = i
        for k in range(i + 1, len(int_list)):
            if int_list[ind] < int_list[k]:
                ind = k
        int_list[i], int_list[ind] = int_list[ind], int_list[i]
        for x in int_list:
            print(x,end=" ")
        print()
    return int_list

if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)