index = 703

if index <= 26:
    print("single",chr(64 + index))
else:

    a = index // 26 
    b = index % 26

    print(chr(64 + a))
    print(chr(64 + b))
    i= chr(64 + a)
    j= chr(64 + b)

    print(i+j)

    print(a)
    print(b)