
from typing import List
import random

def process_data() -> List:
    with open('names.txt', 'r', encoding='utf-8') as f:
        names = [x.strip() for x in f.readlines()]
    return names

def task_1(name: str, names: List) -> None:
    index = names.index(name)
    print(names[0], names[index], names[ -1], sep='\n')
names = process_data()
task_1('Козира',names)

def task_2(data):
    return random.choice(data)
print(task_2(names))

def task_3(data):
    for i in range(len(data)-1, 0, -1):
        print(data[i])
task_3(names)

def task_4(data):
    return max(data, key=len), min(data, key=len)
print("Longest and shortest  = ", task_4(names))

def task_5(data):
    letter_count = 0
    row_count = len(data)
    for i in data:
        for j in i:
            letter_count+=1
    words = len(data)
    return letter_count, row_count, words
print(f"Num of letters, rows and words = {task_5(names)}")

def task_6(file_name:str):
    file = open(file_name, 'r', encoding='utf-8')
    s = 0
    for line in file.readlines():
        arr = line.split()
        s += int(arr[1]) * int(arr[2])
    file.close()
    return s
print(task_6('prices'))

def task_7():
    s = 0
    with open('nums', 'r', encoding='utf-8') as f:
        for i in f.read():
            if i.isdigit():
                s+=int(i)
    return s
print(task_7())

def read_csv():
    import csv
    l = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            l.append(row)
    return l
print(read_csv())

def task_9():
    with open('random.txt','w', encoding='utf-8') as f:
        for i in range(2525):
            f.write(str(random.randint(111,778))+'\n')
task_9()






