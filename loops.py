# LOOPS

# For Loop
items = [1, 2, 3, 4, 5, "Hi"]
for item in items:
    print(f"Round {item}")

 # Range function
for item in range(10, 50, 10):
    print(f"Range Value {item}")


scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print(f"Subtotal:{total}")
print(f"Grand Total:{total}")


files = ['Report.csv ', 'DATA.csv', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")

for item in range(1, 11):
    print(f"7 X {item} = {7 * item}")

for i in range(1, 7):
    print(f"{'*' * i}")

  # Break - iteration

names = ['John', 'Doe', '', 'Marcus']
for index, name in enumerate(names):
    if name == '':
        print(f"Empty detected at position {index + 1} of the list")
        break
    print(f"Name: {name}")

days = ["Mon", "Sun", "Wed", "Tue"]
weekends = ['Sat', "Sun"]
for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")

emails = [
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

# For ... Else
items = [1, 2, 3, 5]
for i in items:
    if i % 2 == 0:
        print(f"Even Number: {i}")
        break
else:
    print(f"odd nomber only array.")

files = ['data.csv', 'report.pdf', 'dasboard.csv', 'time.txt']
for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not a csv")
        break
else:
    print('All files are csv')


files = ['data.csv', 'report.pdf', 'dasboard.csv', 'time.txt', 'data.csv']

seen = set()

for file in files:
    if file in seen:
        print(f"Duplicates found")
        break
    seen.add(file)
else:
    print('All files are uniques')

for x in range(3):
    for y in range(2):
        for z in range(2):
            print(f"({x},{y},{z})")

years = [2026, 2027, 2028]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
days = range(1, 28)
for y in years:
    for m in months:
        for d in days:
            print(f"Reports_{y}_{m}_{d}.csv")


#Looping through tables:
 #SELECT count(*) FROM customers where id is IS NULL;

tables =['customers','orders','products','prices']
columns = ['id','code','create_date']
for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} where {c} IS NULL;")


#WHILE .... LOOP

count = 1
while count <= 10:
    print(count)
    count +=2

#Dynamic while ... loop

ans = ""
while ans.lower() !="yes":
    ans = input("Wallahi, you are gay! (yes/no):")
print("Hahahahah, you inversely straight")

#WHILE .... TRUE

while True:
    answer = input("Aren't you gay? (Yes/No):")
    if answer.lower() == "Yes":
        break
print("{Gay! * 2}")