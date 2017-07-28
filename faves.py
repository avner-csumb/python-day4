fave_food = raw_input('What\'s your favorite food? ')
fave_food = fave_food.upper()
vowels = ['A', 'E', 'I', 'O', 'U']

for v in vowels:
    fave_food = fave_food.replace(v, v * 5)
print(fave_food)
