low = int(raw_input('Enter low number: '))
high = int(raw_input('Enter high number: '))

# i = low
# while i <= high:
#     print(i)
#     i += 1

my_list = range(low, high+1)
for i in my_list:
    print(i)
