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

print(f"{name}, {details},{city}")

 # underscore _ unpacking
lst = [20,30,40,50,]
_, nd, rd, _ = lst

num = [1,4,5,10,3]
print("Max:", max(num), num.count(10))

#Changing List
  # - New data - add | append() | insert(psn,val)
  # - Wrong data - remove
  # - new data - update

letters = ['a','b','c']
letters.append('d')
letters.insert(0,'x')


matrix = [['a','c','b'],['d','e','f']]
matrix[0].sort()
print(matrix)

#Reversing List

a = [4,3,2,1]
a.reverse()
b= reversed(a)
print(list(b))

#Copying
letters = ['a','b','c']
lettters_copy = letters.copy()
letters.pop()
lettters_copy.append('z')

print("original: ", letters)
print("Copy:", lettters_copy)

#Deep Copy - copy.deepcopy()

import copy

matrix = [['a','b'],
          ['c','d']
]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')

print('Original: ', matrix)
print('Copy:',  matrix_copy)

#just Copy - copy.copy()
matrix = [['a','b'],
          ['c','d']
]
matrix_copy = copy.copy(matrix)
matrix.pop()
matrix_copy[0].append('z')

print('Original: ', matrix)
print('Copy:',  matrix_copy)


#Combining List

letters = ['a','b','c']
numbers = [1,2,3]

comb = letters + numbers
merge = [letters, numbers]
numbers.extend(letters)
zipz = list(zip(letters,numbers))


print(letters)
print(numbers)
print(comb)
print(merge)
print(zipz)

#Iterating List - Iterators & Iterables
  # why need Iterators ?
  # 1.build a Loop thro a list
  # 2.save memory 
  # 3.for speed and flexibility

letters = ['a','b','c']
new_list = []
for i in letters:
    new_list.append(i.upper())
    print(new_list)

letters = ['a','b','c','d']
for index, value in enumerate(letters):
    print(index,value)

for i in reversed(letters):
    print(i)


#Iterator map
ls = ['x','y','z']
print(list(map(str.upper,ls)))

num = [2,4,6]
print(list(map(int, num)))

names =['  mark','John','Kumar  ']
for n in map(str.title,map(str.strip,names)):
    print(n)

#iterator filter

ds = ['a',10,'',None,False,'b','c']
print(list(filter(None, ds)))
print(list(filter(bool, ds)))


tools = ['Sql','123','10','python']
print(list(filter(str.isalpha,tools)))
for i in filter(str.isalpha, tools):
    print(i)