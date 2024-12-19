a=[4,-3,5,-2,-1,2,6,-2]
p=[]
n=[]
new=[]
for i in a:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
for i in range(len(n)):
    new.append(p[i])
    new.append(n[i])

print(new)