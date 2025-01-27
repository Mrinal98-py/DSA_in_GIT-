child = [1,3,2]
cookies = [1,1]

flag = 0

child.sort()
cookies.sort()

i = 0
j = 0

while j< len(cookies) and i<len(child):
    if cookies[j] >= child[i] :
        i+=1
    
    j+=1
 
print(i)