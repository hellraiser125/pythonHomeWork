def numbers():
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    c = int(input("Input third number: "))
    nums = [a, b, c]
    nums.sort()
    max = nums.pop()
    print("Greatest number is : ", max)
    print("Lower number is : ", nums[0])
    print("Left next num : ", nums[1])
numbers()



