import math

income = (input("Type in your income for the month: "))
text = (input("Type in your expenses for the month separating each expense by a coma (Ex. 60,40,34): "))
expenses = (text.split(','))
expense_total = sum([int(num) for num in expenses])

outcome = float(income)-float(expense_total)

print(f"Your monthly estimated remaining is {outcome} ")
