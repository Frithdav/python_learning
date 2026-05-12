
# # Python Built-in functions - comes with python by default

# # User-defined functions - user own creation

# # Third-Party functions - Installable functions.


# print(" --------------------------- ")
# print("LEARNING PYTHON SINCE 2018")
# print("---------------------------")


# # Escape Sequences in Python. - special lines.

# # Escape Double Quote - Allows inclusion without ending it.
# print("Hi \"Python\"")

# # Escape Single Quote - Allows inclusion without ending it.
# print("Path: \'Python\'")

# # Escape backslash- Allows inclusion without ending it.
# print("Path: C:\\Python\\Frimannn\\python")


# print("My son, Fri Mann \n")
# print("Is such a lively person \n I relly enjoy him calling me \'Papaa\'. It is healing the soul!")


# print("""Your Learning Path:
# \t - Python Basics 
# \t - Data Engineering 
# \t  - AI""")


# #VARIABLES
# name = "Mormont"
# language = "Python"

# print("My name is", name,"I wanna become an expert in", language)

# name = "Bambi"

# print("You are", name)



# #FUNCTIONS - Independent block of code
#   #syntax function_name(value)
# print('hello')
# type(50)

# #METHODS - Functions which belongs to object/class.
#    #syntax value.method_name()

# print("helo".upper())

# number = 50

# print(number.bit_length())



# #TYPES

# name = "Tajiri"

# print(type(name))

# age = 28

# print(type(age))
# print("Your Age is:" , age)

#DATA TRANSFORMATIONS:
  #Replace

price = "KES 18,005,899.99"
print(price.replace("KES","").replace(",",""))


  #Join - + opeerator
   
first_name ="Malia"
last_name ="Mormont"

full_name = first_name + " " +last_name

folder ="C:/Users/Tajiri/"
file ="learn.csv"

full_path = folder + file

print(full_path)


 #F-string

name = "Tajiri"
age = 2.9
is_student = False

print(f"My name is {name}, I am {age} years old, and pupil status is {is_student}.")