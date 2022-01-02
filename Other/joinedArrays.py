
arr = [1,2,3]
arr2 = [4,5,6]
arr3 = []

for i in range(len(arr)):
    arr3.append(arr[i])
for i in range(len(arr)):
    arr3.append(arr2[i])

print(arr3)