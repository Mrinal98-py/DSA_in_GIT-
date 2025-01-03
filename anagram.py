from typing import Counter


# s = "ggii"
# t = "eekk"
s = "go"
t = "og"

s = s.lower()
t = t.lower()
sum1 = 0
sum2 = 0

if Counter(s) == Counter(t):
    print("true")

# for i in s:
#     # print(i)
#     sum1 = sum1 + ord(i)
# print(sum1)

# for j in t:
#     # print(i)
#     sum2 = sum2 + ord(j)
# print(sum2)

# if sum1 == sum2: return True
# else : return False

 
# g = 103 
# i = 105 

# e = 101
# k = 107
 
# 103 + 103 + 105 + 105 == 513
# 101 + 101 + 107 + 107 == 513  
 
# x = ord('k')
# print(x)