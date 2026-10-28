# lists
ages=[21,72,43,76,23,78,88,90,15]
names=["zack","jane","moha","rick"]

ages.append(31)
ages.sort()
ages.reverse()


names.sort()
print(ages)
print(names)
jack_count=names.count("zack")
print(jack_count)
print(len(names))
print(round(sum(ages)/len(ages,),2))
print(ages[1])
print(ages[-2])
print(names[1:])
#sets
score ={8,88,78,99,65,77,78} #no duplicates
print(score)

#tuples- immutable
weekdays=("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays[0])


#dictionary
person={"name":"john", "age":22,"weight":53}
print(person["name"])
print(person["age"])

people=[{"name":"john","age":22,"weight":53},
        {"name":"amos","age":20,"weight":56}]
print(people[1]["weight"])