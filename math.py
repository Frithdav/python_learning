# MATH

import random
import math
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

print(math.floor(price))
print(math.ceil(price))

print(random.random())
print(random.randint(1, 10))

# Numeric Validation
x = 7.0
print(x.is_integer())
print(isinstance(x, int))

print(random.randint(1, 100).is_integer())


# LOGICAL OPERATOR

# AND || OR || NOT || IN
print(not 3 > 2)

# "a" in "Data" || 'a' not in 'Data'
print(3 in [1, 2, 3])

# IF ELSE
score = 50
if score >= 90:
    print("A")
else:
    print("Wololo!")

  # ELIF
score = 79.999999999999999
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("D!")

    # Nested  IF
score = 84
cat = 25
if score >= 70:
    if cat >=25:
        print("Excellent")
    else:
        print("Very Good")
elif score >= 60:
    print("Good")
elif score >= 50:
    print("Fair")
else:
    print("Fail")

email = " Debo@gmail.net"
password = "3ebo@Gmail.ne7"

# clean email string
email = email.strip()
 # email must not be empty check
if email == "":
    print("Email cannot be empty!")
 # email must contain '@' and '.' symbol
if not ('.' in email and '@' in email):
    print("Email must contain '.' and '@' symbols. ")
 # Email must end with .com,.org or .net
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com,.org or .net")
 # Email must contain exactly 1 '@' symbol.
if email.count('@') != 1:
    print("Email must contain exactly 1 '@' symbol.")
 # email must start and end with a letter
if not(email[0].isalpha() and email[-1].isalpha()):
    print("Email must start and end with a letter")
 #password must be atlest 8 characters!
if len(password) <8:
    print("password must be atlest 8 characters!")
 #password can't be same as email.
if password == email:
    print("password can't be same as email.")
 #Password must contain atleast 1 upper annd lower characters
if not any(p.isupper() for p in password) and any(p.islower() for p in password):
    print("Password must contain atleast 1 upper annd lower characters")
 #password must start and end with a digit
if not(password[0].isdigit() and  password[-1].isdigit):
    print("password must start and end with a digit")
else:
    print("Email is valid")

