from Addition import *

whack = addition()

zahl1 = int(input("Enter number 1:"))
zahl2 = int(input("Enter number 2:"))
operator = input("Enter operator:")
if operator == "+":
    print(whack.plus(2, 3))
