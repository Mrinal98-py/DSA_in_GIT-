expense = [2200,2350,2600,2130,2190]
print("1. In Feb, how many dollars you spent extra compare to January?")    

sum = 0
for i in expense[0:3]:
    sum+=i
print(sum)
print(expense[0]+expense[1]+expense[2],"continueous sum")

#exactly 2000 dollars in any month
print("3. Find out if you spent exactly 2000 dollars in any month")
for i in expense:
    if i == 2000:
        print(i)
    else:
        print("No 2000 dollars spent in any months\n")
        break

expense.append(1980)
print("4. June month expenses are 1980 dollars. Add this item to our monthly expense list\n",expense)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expense[3] = expense[3]-200
print("5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this\n",expense)
        