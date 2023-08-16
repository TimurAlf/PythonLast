# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем
# Программа должна возвращать сумму и произведение дробей 
# Для проверки своего кода используйте модуль fractions

import fractions

first: str = str(input("Enter the numerator of the first fraction::\n"))
second: str = str(input("Enter the denominator of the first fraction::\n"))
third: str = str(input("Enter the numerator of the second fraction::\n"))
fourth: str = str(input("Enter the denominator of the second fraction:\n:"))
number1: int = int(first)
number2: int = int(second)
number3: int = int(third)
number4: int = int(fourth)
result1 = (number1 / number2 ) + (number3 / number4)
result2 = (number1 / number2 ) * (number3 / number4)
print(result1)
print(result2)
firstfraction = fractions.Fraction(number1, number2)
secondfraction = fractions.Fraction(number3, number4)
result3 = firstfraction + secondfraction
result4 = firstfraction * secondfraction
print(result3)
print(result4)