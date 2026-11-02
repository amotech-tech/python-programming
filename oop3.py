# bank account==owner,acc no., balance,history/statement
from datetime import date, datetime


class Client:
    def __init__(self, names, kra_pin, dob, gender):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, '%d.%m.%Y')
        age = today.year - birth_date.year
        return age


class BankAccount:
    def __init__(self, owner:Client, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount:int):
        self.balance += abs(amount)  # no negative number

    def withdraw(self, amount:int):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):

        self.owner.print_details()
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("----------------------------")


jane=(Client("Jane Mwangi","A001","19.07.2005",'Female'))
Ahmed=(Client("Ahmed Mohamud","A002","19.07.2009",'male'))

acc1=BankAccount(jane, acc_no="1234", balance=456_000)
acc2=BankAccount(Ahmed, acc_no="2377", balance=4_986)
acc3=BankAccount(Ahmed, acc_no="333333", balance=4986_856)


acc1.deposit(10_000)
acc1.deposit(3_000)
acc1.print_details()
acc1.withdraw(5_000)
acc1.print_details()

print("Jane's Age",jane.calc_age())
print("Ahmed's Age",Ahmed.calc_age())


print(acc1.owner.names,acc1.owner.calc_age())
print(jane.names,jane.calc_age())


# dob='18.1.2004' #d.m.y
# today=date.today()
# # print(f"{today.day}-{today.month}-{today.year}")
# # convert string to date
# birth_date=datetime.strptime(dob, '%d.%m.%Y')
# age=today.year - birth_date.year
# print(age)
