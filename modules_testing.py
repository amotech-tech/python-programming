# import functions as f
#
# print(f.module_function(2,3))
# #
import math

import functions
from functions import module_function
print(module_function(2,3))

# from my_package import shapes
# print(shapes.triangle_area(3,4,5))

# from my_package.shapes import triangle_area as area
# print(area(3,4,5))

print(dir(math))
print(dir(functions))