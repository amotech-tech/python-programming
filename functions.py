from custom_functions import greet

greet()
def addition(*nums): #list
    """
    RETURNS SUM OF NUMBERS passed as arguments
    :param nums: input arguments
    :return: integers of floats
    """
    total=sum(nums)
    return total
addition(1,2,3,4)

# def build_profile(**kwargs): #dict key-word args
#     for k, w in kwargs.items():
#         print(f"{k}: {w}")

def funcy_function(name,*nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)


funcy_function("Amos",(3,4,5,67))
#
#
# build_profile(experience=100, name="Jane", proffession="IT")
#
# print(addition(4, 5,4,3,4,3,2,3,6,7,4,8,9))
#
# #anonymous functions
#
# # def square(num):
# #     return num*num
# # result=square(5)
# # print(result)
# square = lambda num: num*num
# print(square(4))


surface_area_cylinder = lambda r,h:22/7*r**2 *2 +22/7*2*r*h
print(round(surface_area_cylinder(20,7),2))

people=[
    {"name":"Amos","age":30 },
    {"name":"bob","age":30},
    {"name":"Charlie","age":40},

]
sorted_by_age=sorted(people, key=lambda x: x["age"], reverse=True)
print(sorted_by_age)