import random
import sys
import numpy as np
def task1():
    arr = []
    for i in range(100):
        arr.append(random.randint(0, 100))
    print(f"Start list\n")
    for i in range(len(arr)):
        print(arr, end=' ')

    print("\n\nBubble\n")
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    for i in range(len(arr)):
        print(arr, end=' ')

    arr.clear()
    for i in range(100):
        arr.append(random.randint(0, 100))

    print(f"\nStart list\n ")
    for i in range(len(arr)):
        print(arr, end=' ')

    print("\n\nSelection sort\n")
    for i in range(len(arr)):
        low_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low_value]:
                low_value = j
        arr[i], arr[low_value] = arr[low_value], arr[i]

    for i in range(len(arr)):
        print(arr, end=' ')

    arr.clear()
    for i in range(100):
        arr.append(random.randint(0, 100))
    print(f"\nStart list\n ")
    for i in range(len(arr)):
        print(arr, end=' ')
    print("\n\nStandart sort\n")
    arr.sort()
    for i in range(len(arr)):
        print(arr, end=' ')
def task2(mac: list) -> list:
    return [adress.replace(':', '.') for adress in mac]
def task3(n):
    l = []
    temp_list = []
    for i in range(1, n):
        temp_list.append(i)
        l.append(temp_list.copy())
    print(l)
def task4( rows, ryadki = None):
    row = [1]
    for i in range(ryadki, rows):
        print('\t', row, '\t')
        row = [sum(x) for x in zip([0] + row, row + [0])]
def task5(rows, ryadki = None):
    row = [1]
    for i in range(ryadki, rows):
        print('\t', row, '\t')
        row = [sum(x) for x in zip([0] + row, row + [0])]
def task6(chunk_size, *args):
    l = []
    for i in range(len(args)):
         l.append(list(args[i:i + chunk_size]))
         print(l)
def task7(encoding='utf-8', errors='surrogatepass'):
     size = 3
     matrix = [[1, 4, 5],
               [6, 7, 8, ],
               [1, 1, 6], ]

     maxNumber = matrix[0][0]
     if size < 2:
         print(maxNumber)
         sys.exit()

     halfSize = int(size / 2)

     for y in range(halfSize + 1):
         for x in range(y + 1):
             if matrix[y][x] > maxNumber:
                 maxNumber = matrix[y][x]

     for y in range(halfSize, size):
         for x in range(halfSize, size - y - 2, -1):
             if matrix[x][y] > maxNumber:
                 maxNumber = matrix[x][y]

     for x in range(halfSize, size):
         for y in range(size - x):
             if matrix[x][y] > maxNumber:
                 maxNumber = matrix[x][y]

     for x in range(halfSize, size):
         for y in range(halfSize, x + 1):
             if matrix[y][x] > maxNumber:
                 maxNumber = matrix[y][x]

     print(maxNumber)
def task8():
    s = 'f3'
    x = int(s[0], 16) - 10
    y = int(s[1]) - 1

    lst = (
         (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, 2),
        (1, -2),
        (2, 1),
        (2, -1), )
    result = np.chararray((8, 8))
    result[:] = '.'
    result[x][y] = 'N'
    for xi, yi in lst:
        result[x + xi][y + yi] = '*'
    print(result)
def task10():
    N = int(input())
    length = N * N
    mx = [[None for z in range(N)] for z in range(N)]
    y = 0
    x = N // 2
    mx[y][x] = 1
    for i in range(2, length + 1):
        old_x, old_y = x, y
        x = (x + 1) % N
        y = (y - 1) % N
        if not mx[y][x] is None:
            x = old_x
            y = (old_y + 1) % N
        mx[y][x] = i
    a = []
    for y in mx:
        a += y
    print(' '.join(map(str, a)))
def task11(n, m):
    matrix = [[0 for i in range(m)] for _ in range(n)]
    count = 1
    for i in range(n):
        for j in range(m):
            matrix[i][j] += count
            count += 1
    for i in range(n):
        if i % 2 == 0:
            print(*matrix[i])
        else:
            matrix[i].reverse()
            print(*matrix[i])
def task12(n, m):
    mtx = [[0] * m for _ in range(n)]
    sequence, k = 1, 0

    while sequence != n * m + 1:
        for i in range(n):
            for j in range(m):
                if i + j == k:
                    mtx[i][j] = sequence
                    sequence += 1
        k += 1
    return mtx
def task13(n, m):
    mat = [[0] * int(m) for i in range(n)]

    a, b, c = 0, 0, 1
    rows, cols = n - 1, m - 1

    while a <= cols and b <= rows:
        for i in range(a, cols + 1):
            mat[a][i] = c
            c += 1
        b += 1
        for i in range(b, rows + 1):
            mat[i][cols] = c
            c += 1
        cols -= 1
        if b <= rows:
            for i in range(cols, a - 1, -1):
                mat[rows][i] = c
                c += 1
            rows -= 1
        if a <= cols:
            for i in range(rows, b - 1, -1):
                mat[i][a] = c
                c += 1
            a += 1

    for s in mat:
        print(*s)
def main():
    while(True):
        v = int(input("Choose task 1-10:\nExit: 0 "))
        if (v == 1):
            task1()
        elif (v == 2):
            mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
            task2(mac)
        elif (v == 3):
            n = int(input("Input n: "))
            task3(n)
        elif (v == 4):
            task4(2,10)
        elif (v == 5):
            task5(2,10)
        elif (v == 6):
            task6(2, 'a', 'b', 'c', 'd')
        elif (v == 7):
            task7()
        elif (v == 8):
            task8()
        elif (v == 10):
            task10()
        elif (v == 11):
            task11(3, 5)
        elif (v == 12):
            task12(11, 22)
        elif (v == 13):
            task13(11, 22)
        elif (v == 0):
            exit(0)
        else:
            print('Wrong task!!!')
main()



