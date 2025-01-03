def largestOddNumber(num):            
    size = len(num) -1

    while size > 0:
        if int(num[size]) % 2 == 1:
            return(num[:size+1])
            break
        else:
            size -= 1
        # print(num[:size])
        
num = "123024680"
print(largestOddNumber(num))