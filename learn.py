"""
value = input('what do want the cat to say? ')
value_length = len(value)
print('          {}'.format('-'*value_length))
print('        < {} >'.format(value))
print('          {}'.format('-'*value_length))
print('        /')
print('      /')
print(' /\_/\ ')
print('( o.o )')
print(' > ^ < ')


value = input('how far you want to travel? ')
value = int(value)

if value<=3:
    print('you can simply walk')
elif value>3 and value<300:
    print('you cab drive!')
elif value>=300:
    print('fly pls')
else:
    print('invalid input')


list_task = []
value = 0

def get_task():
    global list_task, value
    task = input('Enter a task for your to­do list : ')
    if task != "":
        print("Task added.")
        list_task.append(task)
    else:
        value = 2

    return value


def display():
    if len(list_task) > 0:
        print("Your To-Do List:")
        print("----------------")
        index = 0
        while index<len(list_task):
            print(list_task[index])
            index +=1
    else:
        print("No task have been added") 


def call_fun():
    while value<1:
        get_task()
    display()
    

call_fun()

contacts = {"mani":["001", "005"], "priya":"002"}
contacts["sow"] = "003"

if "mani" in contacts.keys():
    print(contacts["mani"][0])

for con in contacts:
    print("value for {0} is {1}".format(con, contacts[con]))

for person, number in contacts.items():
    print("The person {0} number is {1}".format(person, number))

tuple_value = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
for n in tuple_value:
    print(n)

def high_to_low(number):
    highest = max(number)
    lowest = min(number)
    return (highest, lowest)


val = (11,15,18,75,12,95,41,32)
(high, low) = high_to_low(val)
print('The highest number is {}'.format(high))
print('The lowest number is {}'.format(low))

list_val = [("london", "LHR"), ("LA","LAX"), ("Dallas","DFW"), ("Denver","Den")]

for (airport, code) in list_val:
    print("The code for {0} International Airport is {1}.".format(airport, code))


open_file = open('/home/manikandan/Documents/readFile.txt')
print(open_file.tell())
print(open_file.read())
print(open_file.tell())
print(open_file.read())
open_file.seek(0)
print(open_file.tell())
print(open_file.read())
print('File closed? {}'.format(open_file.closed))
open_file.close()
print('File closed? {}'.format(open_file.closed))

open_file = '/home/manikandan/Documents/readFile.txt'

with open(open_file, 'a') as f:
    f.write('\n')
    f.write("writing first line \n")
    f.write("writing second line")

with open(open_file) as f:
    print(f.read())

Draw picture:
=============
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

for i in picture:
    text = ''
    for j in i:
        if(j == 0):
            text += " "
        else:
            text +="*"
    print(text)



for i in picture:
    for j in i:
        if(j == 0):
            print(" ", end='')
        else:
            print("*", end='')
    print('')


find Duplicates:
================
my_list = ['a', 'b', 'c', 'b', 'd','m','n','n']
duplicates=[]
for i in my_list:
    if my_list.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)

print(duplicates)

Reverse a String:
=================
my_str = input('Enter a string : ')
reverse_str = my_str[::-1]
print(reverse_str)

Print *:
=========
i = 1

while i<5:
    for n in range(i):
        print('*', end='')
    print('')
    i +=1

ll = ['a','s','e','w','w','e']

duplicates = list(set([val for val in ll if ll.count(val)>1]))
print(duplicates)

ll1 = [1,2,2]
ll2 = [2]

def ar_dif(a,b):
    for i in a:
    print('iteration for '+str(i))
        for j in b:
            if(i==j):
                a.remove(i)
                continue
                print('removed '+str(i))
                print(a)
    return a

ar_dif(ll1, ll2)

"""




