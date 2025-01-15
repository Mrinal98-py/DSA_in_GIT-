
num = "23423411222222222222222222222222222222222222222222224444444446666888800000"
size = len(num) -1

# while size >= 0:
#     if int(num[size]) % 2 == 1:
#         return num[:size+1]
#         # break
#     else:
#         size -= 1
#     # print(num[:size])
# return ""

while size >= 0:
    if int(num[size]) % 2 == 1:
        print(num[:size+1])
        break
    
    size -= 1
    # print(num[:size])
print("")
