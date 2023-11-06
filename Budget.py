# def get_total(numbers_seperated_by_comma):
#     numbers_list = numbers_seperated_by_comma.split(",")
#     outcome = []  #new list with values as float for calculation
#     for number in numbers_list:
#         outcome.append(float(number))   #this will convert every value in the list into a float
#     calculation_sum = sum(outcome)  #this will add together every value in the list "outcome"
#     return calculation_sum
    
# income = get_total(input("Enter your income: "))
# expense = get_total(input("Enter your expenses: "))
# remaining = income - expense
# print(f"Your total remaining is {remaining}")

class expense:
    def __init__(self, name, quantity, description, date):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.date = date

    def print_all(self):
        return f"name: {self.name}, quantity: {self.quantity}, description: {self.description}, date: {self.date}\n"

def get_total(expenses_list):
    quantity_list = []

    for expense_number in expenses_list:
        quantity_list.append(expense_number.quantity)

    total = sum(quantity_list)

    return total

class income (expense):
    pass

# Expenses
number_of_expenses = int(input("How many expenses do you want to insert? "))
expenses = []

for number in range(number_of_expenses):
    print(f"\nWe are in expense # {number+1}\n")
    name = input("Enter expense name: ")
    quantity = float(input("Enter expense quantity: "))
    description = input("Enter expense description: ")
    date = input("Enter expense date: ")

    new_expense = expense(name, quantity, description, date)
    expenses.append(new_expense)

expense_total = get_total(expenses)

# Incomes
number_of_incomes = int(input(f"\nHow many incomes do you want to insert? "))
incomes = []

for number in range(number_of_incomes):
    print(f"\nWe are in income # {number+1}\n")
    name = input("Enter income name: ")
    quantity = float(input("Enter income quantity: "))
    description = input("Enter income description: ")
    date = input("Enter income date: ")

    new_income = income(name, quantity, description, date)
    incomes.append(new_income)

income_total = get_total(incomes)

total_remaining = income_total - expense_total

print(f"\n\nYour total remaninig is: {total_remaining}")