# Kyle Dela Pena
# 2038252

# Define your function here
def exact_change(total):
    num_dollars = total // 100
    total %= 100
    num_quarters = total // 25
    total %= 25
    num_dimes = total // 10
    total %= 10
    num_nickels = total // 5
    total %= 5
    num_pennies = total
    return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Type your code here.
    if input_val <= 0:
        print('no change')

    if num_dollars > 1:
        print('%d dollars' % num_dollars)
    elif num_dollars == 1:
        print('%d dollar' % num_dollars)

    if num_quarters > 1:
        print('%d quarters' % num_quarters)
    elif num_quarters == 1:
        print('%d quarter' % num_quarters)

    if num_dimes > 1:  #
        print('%d dimes' % num_dimes)
    elif num_dimes == 1:
        print('%d dime' % num_dimes)

    if num_nickels > 1:
        print('%d nickels' % num_nickels)
    elif num_nickels == 1:
        print('%d nickel' % num_nickels)

    if num_pennies > 1:
        print('%d pennies' % num_pennies)
    elif num_pennies == 1:
        print('%d penny' % num_pennies)
