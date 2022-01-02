#Reverse array loop

arr = [1,2,3,4,5]
arrb = []

for i in range(len(arr)):
    arr.reverse()
    arrb.append(arr)
print(arrb[i])