# Kyle Dela Pena
# 2038252

# FIXME (1): Finish reading other items into variables, then output the three ingredients
lemon_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings_cups = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_cups))
print('{:.2f} cup(s) lemon juice'.format(lemon_cups))
print('{:.2f} cup(s) water'.format(water_cups))
print('{:.2f} cup(s) agave nectar'.format(nectar_cups))

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

desired_servings = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_cups * desired_servings / servings_cups))
print('{:.2f} cup(s) water'.format(water_cups * desired_servings / servings_cups))
print('{:.2f} cup(s) agave nectar'.format(nectar_cups * desired_servings / servings_cups))

# FIXME (3): Convert and output the ingredients from (2) to gallons

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} gallon(s) lemon juice'.format(lemon_cups * desired_servings / servings_cups / 16))
print('{:.2f} gallon(s) water'.format(water_cups * desired_servings / servings_cups / 16))
print('{:.2f} gallon(s) agave nectar'.format(nectar_cups * desired_servings / servings_cups / 16))
