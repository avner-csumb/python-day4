fruit = raw_input("What's your favorite fruit? ")
fruit = fruit.lower()

if fruit == 'banana' or fruit == 'apple':
    print(fruit + ' is a good choice')
elif fruit == 'mango':
    print(fruit + ' is a great choice')
elif fruit == 'tomato':
    print('Why would you enter in ' + fruit + '?!')
else:
    print('I have no opinion on ' + fruit)
