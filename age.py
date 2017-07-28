birth_year = raw_input('What year were you born? ')

your_age = 2017 - int(birth_year)

fave_color = 'blue'

my_string = 'By the end of the year you will be {1} and your favorite color\nis {1}. By the way, your favorite color is {0}.'.format(str(your_age), fave_color)

print(my_string)
