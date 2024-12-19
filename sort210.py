array = [0,0,2,1,2,0]
c0 = 0
c1 = 0
c2 = 0
for i in range(len(array)):
    # print(i,array[i])
    if array[i] == 0:
        c0 = c0+1
    elif array[i] == 1:
        c1 += 1
    else:  
        c2 += 1
print(c0,c1,c2)
for i in range(0,c0,1):
    array[i]=0
for i in range(c0,c0+c1):
    array[i]=1
for i in range(c0+c1,len(array)):
    array[i]=2
print (array)