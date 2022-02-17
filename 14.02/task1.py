def apples():
    n = int(input("Input count of children: "))
    k = int(input("Input count of apples: "))
    if n == 0 or k == 0:
        print("Children's or apples exist!")
        return
    elif k < n:
        print("Children's more than apples. All apples stay in basket")
        return
    print("Apples in basket: ", k % n)
    print("Apples for children: ", int(k / n))

apples()



