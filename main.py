import sys
name = input("what is your name?")
age= input ("Enter your age")
if not age.isnumeric():
    print("invalid age")
    #terminate
    sys.exit()

if int(age) >18:
    print(name + "is an adult")
else:
    print(name + "is an child")
