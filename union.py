u=[]
a=[1,77,23,4,2,5]
b=[4,2,5]
for i in a:
    if i not in u:
        u.append(i)
for i in b:
    if i not in u:
        u.append(i)
print(len(u))
        #code here

## OR
print(len(set(a+b)))