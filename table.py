n = int(input())  # количество строк
m = int(input())  # количество столбцов

if n == 1 and m == 1:
    print("*")
elif n == 2 and m == 2:
    print("**")
    print("**")
elif n == 1 and m == 2:
    print("**")
elif n == 2 and m == 1:
    print("*")
    print("*")
elif n == 2 and m > 2:
    while n > 0:
        h = m
        while h > 1:
            print("*", end="")
            h -= 1
        else:
            print("*")
        n -= 1
elif n > 2 and m == 2:
    while n > 0:
        print("**")
        n -= 1
elif n > 2 and m > 2:
    l = n - 2
    x = m
    while m > 1:
        print("*", end="")
        m -= 1
    print("*")
    while l > 0:
        print("*", end="")
        h = x - 2
        while h > 0:
            print(" ", end="")
            h -= 1
        print("*")
        l -= 1
    while x > 0:
        print("*", end="")
        x -= 1
