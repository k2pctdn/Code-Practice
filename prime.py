import math


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


x = int(input("Please type a natural number: "))

print('Check prime status: ', prime(x))
if prime(x):
    print(x, 'is a prime number.')
else:
    print(x, 'is not a prime number')
