class Person:
    def __init__(self,name,dob,color, weigth,height,age):
        self.name=name
        self.age=age
        self.dob=dob
        self.weigth=weigth
        self.color=color
        self.height=height

    def display(self):
          print(f"Your name is {self.name} and DOB is {self.dob} years old")

    def get_bmi(self):
        result=self.weigth/self.height**2
        return round(result,2)

p1= Person("Stephen","20-04-2003","black",50.2,5.6,22)
p2 = Person("Amos", "19-07-2005", "white", 52.2, 5.6, 22)
p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")