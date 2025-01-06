matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
# Output =  [1,2,3,4,8,12,11,10,9,5,6,7]

output = []

print(len(matrix))

if len(matrix) <= 1:
    print(matrix)
    output.append(matrix[0])
else:
    output.append(matrix[0])
    
    for i in range (len(matrix)) :
        print (matrix[i][i])

print("OUTPUT",output)
    