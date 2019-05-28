import math


def get_input():
    x = int(input("Please type a natural number: "))
    return x


def prime(n):
    if n < 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def body(n):
    print('Check prime status: ', prime(n))
    if prime(n):
        print(n, 'is a prime number.')
    else:
        print(n, 'is not a prime number')


def checkpoint():
    y = (input('Check more number? Y/N: '))
    if y == 'N' or y == 'n':
        return False
    else:
        return True


check = True

while check:
    body(get_input())
    check = checkpoint()
    print(check)
