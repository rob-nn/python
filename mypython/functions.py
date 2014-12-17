from time import time
from math import *
x = time()
x = floor(x)


if x%2 == 0: 
    def func(): print("It's even")
else:
    def func(): print("It's odd")

func()


def funcpar(a, b, c):
    print ('A = %s, B = %s and C = %s' % (a, b, c))


funcpar('1', '2', '3')

funcpar.attr = ['4', '5', '6']


x = 10

def printx(): print('Value of x: %d' % x)

def changx(): x = 20


print('Value of x: %d' % x)

printx()
