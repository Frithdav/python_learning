# MATH

x = 5
y = 5.7
z = 2 + 3J

print(type(z))
print(complex(x, y))

# Measure Distance

print(abs(2-10))

# Rounding Numbers
price = 429.192797 
print(round(price))

import math
print(math.floor(price))
print(math.ceil(price))

import random
print(random.random())
print(random.randint(1,10))

#Numeric Validation
x = 7.0
print(x.is_integer())
print(isinstance(x,int))

print(random.randint(1,100).is_integer())


#LOGICAL OPERATOR

  #AND || OR || NOT || IN
print( not 3>2)

  #"a" in "Data" || 'a' not in 'Data'
print (3 in [1,2,3])


  #IDF ELSE
score = 50
if score >=90:
    print("A")
else :
    print("Wololo!")