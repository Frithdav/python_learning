#List - [20,10,30,] - common!
#Tuple - (10,20,15) - Locked - No changes!
#Set - {10,20,49} Unique!
#dict - {a:10,d:20,n:90} - Key value pair!

#List

empty = list()
print(empty)
letters = 'Python'
print(list(letters))


numbers = list(range(5))
print(numbers)

 #Nested List
matrix = [['a','b','c'],['d','e','f'],[True]]
print(matrix[:3][1:])

lst = ['a','b','c','d']
print(lst[1])

#List unpacking

numbers =[1,2,3,50,90]
one,two,three,fifty,ninty = numbers
 
 #astericks * unpacking
person = ['Malia','33 days','Data Engineer','Female','Mombasa']
name,*details, city = person

print(name)
print(details)
print(city)
