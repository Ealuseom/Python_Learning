from Operations.Addition import *

whack = addition()

inputnumbertype1 = input(
    "What numbersystem is the first number? (Bin / Okt / Dez / Hex):")

if inputnumbertype1 == "Bin":

    number1 = int(input("Enter number 1:"))
    inputnumbertype2 = input(
        "What numbersystem is the second number? (Bin/Okt/Dez/Hex):")

    if inputnumbertype2 == "Bin":
        number2 = int(input("Enter number 2:"))
        operator = input("Enter an operator ( + / - / * / /):")

        if operator == "+":
