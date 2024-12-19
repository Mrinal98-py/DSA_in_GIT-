""" 1.Print the first 10 natural numbers using for loop."""
for cisco in range(1,11):
    print(cisco)

"""2.Calculate the sum of all numbers from 1 to a given number."""
a= int(input("Enter a number: "))
xum=0
for i in range(1,a+1):
    xum+=i
print(xum)

"""3.Calculate the sum of all the odd numbers within the given range"""
a= int(input("Enter a number: "))
oddsum=0
for i in range(1,a+1):
    if i%2!=0:
        oddsum+=i
    print("sum of odd num",oddsum)

"""4.Print a multiplication table of a given number."""

a= int(input("Enter a number: "))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

# 5. Count the total number of digits in a number

a= int(input("Enter a number: "))
print(len(str(a)))


"""6.sum of all odd no in range 15"""