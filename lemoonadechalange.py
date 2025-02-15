bills = [5,5,10,10,20]

five = bills.count(5)
ten = bills.count(10)
twenty = bills.count(20)

rev_five = five - ten

if twenty <= ten and twenty <= five:
    while twenty >= 0:
        twenty = twenty - 1
        ten = ten - 1
        five = five - 1
        # print(twenty,"twenty")

if five > 0: print("True")
else: print("false")
