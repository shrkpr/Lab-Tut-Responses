import logging
a = input('Key in a number: ')
b = input('Key in a number: ')
c = input('Key in a number: ')
avg = 0
try:
    a = float(a); b = float(b); c = float(c)
    avg = (a+b+c)/3
    print('Average: %.2f'%avg)
except ValueError as e:
    logging.exception(e)
    print(e)
    print('Key a valid input')
