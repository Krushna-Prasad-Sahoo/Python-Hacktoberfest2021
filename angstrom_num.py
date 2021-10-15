# // Author :RUDRANSH SRIVASTAVA
import math

num = int(input("eneter your number :"))
n = num
reverse_num = 0
while n > 0:

    last_digit = n % 10

    reverse_num = reverse_num + pow(last_digit, 3)

    n = int(n / 10)

if reverse_num == num:
    print("{} is angstrom number".format(num))

else:
    print("{} is not angstrom number".format(num))
