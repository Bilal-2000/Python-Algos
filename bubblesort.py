arr = [6, 7, 2, 1, 7, 4, 5]

for j in range(len(arr)):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)
