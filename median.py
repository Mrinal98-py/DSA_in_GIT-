# Python3 code to demonstrate working of 
# Median of list 
# Using loop + "~" operator 

# initializing list 
test_list = [4, 5, 80, 9, 10, 17,89] 

# printing list 
print("The original list : " + str(test_list)) 

# Median of list 
# Using loop + "~" operator 
test_list.sort() 
print("Sorted list is: ",test_list)
mid = len(test_list) // 2
res = (test_list[mid] + test_list[~mid]) / 2

# Printing result 
print("Median of list is : " + str(res)) 
