def task1():
    cup = int(input("Input number of cups: "))
    bonus = int(cup/6)
    print(f"You have {bonus} bonus cups")

def task2():
    cows = int(input("Input number of cows: "))
    chikens = int(input("Input number of chikens: "))
    pigs = int(input("Input number of pigs: "))
    legs_sum = (cows * 4) + (chikens * 2) + (pigs * 4)
    print(f"Fum of legs on the farm : {legs_sum}")

def task3():
    minute = int(input("Input minute: "))
    flag = True
    while flag:
        if minute > 60 or minute < 0:
            minute = int(input("Not valid input \nTry again: "))
        else:
            flag = False
    if minute > 0 and minute < 15:
        print("The first quarter.")
    elif minute == 15:
        print("Arrow on the border of the first and second quarter.")
    elif minute > 15 and minute < 30:
        print("The second quarter.")
    elif minute == 30:
        print("Arrow on the border of the second and third quarter.")
    elif minute > 30 and minute < 45:
        print("The third quarter.")
    elif minute == 45:
        print("Arrow on the border of the third and fourth quarter.")
    elif minute == 0:
        print("Arrow on the border of the fourth and first quarter.")
    else:
        print("The fourth quarter.")

def task4_using_while():
    n = int(input("Input num of stars: "))
    num = 1
    while num <= n:
        print("*" * num)
        num +=1

def task4_using_for():
    n = int(input("Input num of stars: "))
    num = 1
    for i in range(n):
        print("*"*(i+1))
