#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 is 0:
            print('{:s}'.format('FizzBuzz'), end=' ')
        elif i % 3 is 0:
            print('{:s}'.format('Fizz'), end=' ')
        elif i % 5 is 0:
            print('{:s}'.format('Buzz'), end=' ')
        else:
            print('{:d}'.format(i), end=' ')
