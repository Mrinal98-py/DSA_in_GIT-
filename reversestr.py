s = "hello Buddy Bok"

nums  = s.split()
retu = ''
for i in nums[::-1]:
    retu += i + " "


print(retu)