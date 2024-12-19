arr= [1, -1, 3, 2, -7, -5, 11, 6]

     
n=[]
p=[]
for i in arr:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
    
# print(p)
print(' '.join(map(str, p+n)))

