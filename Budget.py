import math


income = int(input("what is your monthly income?: "))

expense1 = int(input("what is your monthly expense in gas?: "))
expense2 = int(input("What is your monthly expense in groceries? "))
expense3 = int(input("What is your monthly expense in rent? "))
expense4 = int(input("What is your monthly expense in subscriptions? "))
expense5 = int(input("What is your monthly expense in restaurants? "))


outcome = income-expense1-expense2-expense3-expense4-expense5

print(f"your montly expense is: ${expense1+expense2+expense3+expense4+expense5}")
print(f"your monthly estimated remaining is: ${outcome}")






