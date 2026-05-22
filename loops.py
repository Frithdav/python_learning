#LOOPS

#For Loop
items = [1,2,3,4,5,"Hi"]
for item in items:
    print(f"Round {item}")

 #Range function
for item in range(10,50,10):
    print(f"Range Value {item}")


scores = [80, 50, 60,75]
total =0
for score in scores:
    total += score
    print(f"Subtotal:{total}")
print(f"Grand Total:{total}")


files = [ 'Report.csv ', 'DATA.csv',' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt','.csv')
    print(f"Processing {file}")

for item in range(1,11):
    print(f"7 X {item} = {7 * item}")

for i in range(1,7):
    print(f"{'*' * i}")

  #Break - iteration

names = ['John','Doe','', 'Marcus']
for index, name in enumerate(names):
    if name =='':
        print(f"Empty detected at position {index + 1} of the list")
        break
    print(f"Name: {name}")

days =["Mon","Sun","Wed","Tue"]
weekends =['Sat',"Sun"]
for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")

emails=[
    'data@gmail.com',
    'goingbad@gmail.com',
    'DROp TABLE USERS;',
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print(f"potential sql injection: Hacker attacker: \n'{email}'")
        break
    print(f"Processing Email: {email}")
