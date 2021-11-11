#!/Users/courtney.bawuah/.pyenv/shims/python

from datetime import datetime

def myfunction(my_user_date):
    age = datetime.now().year - int(my_user_date)
    print(age)

date = input("Enter the year you were born?")
myfunction(date)

date = input("Enter the year you were born?")
myfunction(date)

date = input("Enter the year you were born?")
myfunction(date)
