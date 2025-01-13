s = "the sky is blue"

arr = s.split()

arr = arr[::-1]

r = ""
for i in arr:
    r =  r + i + " "
 
print(arr)
print(r)