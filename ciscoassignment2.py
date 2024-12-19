a=[1,2,3,4,5,6,1,1,7,8,9,10]
#even no to another array |3.Python program to store all even numbers from an array in another array
even=[]
for i in a:
    if i%2==0:
        even.append(i)
print("list of even array",even)
# 2.Python program to find the average of all numbers in a Python array

avg=0
for i in a:
    avg+=i
print("avg/mean of array is ",avg/len(a))

#1.Find the minimum and maximum element in an array
print("min element of array is",min(a))
print("max element of array is",max(a))