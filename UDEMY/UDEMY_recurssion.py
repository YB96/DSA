#factorial
def fact(n):
    if n > 1:
        f = n * fact(n-1)
    else:
        f = 1
    return f
print(fact(1))
print('-------------------')

#fibonacci series
def fib(n):
    if n in [0,1]:
        f = n
    else:
        f = fib(n-1) + fib(n-2)
    return f
print(fib(7))
print('-------------------')

#How to find the sum of n positive integer using recursion?
def sum_of_n(n):
    if n > 0:
        s = n + sum_of_n(n-1)
    else:
        s = 0
    return s
print(sum_of_n(23))
print('---------------------')

#How to find the sum of digits of a positive number using recursion?
def sum_of_digits(n):
    if n < 10:
        s = n
    else:
        s = int(n%10) + sum_of_digits(int(n//10))
    
    return s 
print(sum_of_digits(101))
print('-------------------------')

#How to calculate power using recusrsion?
def power(num,its_power):
    if its_power == 0:
        pow = 1
    elif its_power < 0:
        pow = 1/num * power(num, its_power + 1)
    else:
        pow = num * power(num, its_power-1)
    return pow
print(power(4,-2))
print('-------------------------')

# greatest common divisor using recursion


def gcd(a,b):
    if b == 0:
        return a
    else:
        return  gcd(b, a%b)
print(gcd(48,18))

# decimal to binary
def bin(a):
    l1 = []
    l1.append(bin(a%2))
    return l1

print(bin(10))
print(5%2)

