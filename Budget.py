def get_total(numbers_seperated_by_comma):
    numbers_list = numbers_seperated_by_comma.split(",")
    outcome = []  #new list with values as float for calculation
    for number in numbers_list:
        outcome.append(float(number))   #this will convert every value in the list into a float
    calculation_sum = sum(outcome)  #this will add together every value in the list "outcome"
    return calculation_sum
    
income = get_total(input("Enter your income: "))
expense = get_total(input("Enter your expenses: "))
remaining = income - expense
print(f"Your total remaining is {remaining}")