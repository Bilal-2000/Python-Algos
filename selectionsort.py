arr = [3, 5, 8, 1, 2, 4]

for i in range(len(arr)):
    min = arr[i]
    for j in range(i+1, len(arr)):
        if min > arr[j]:
            min = arr[j]
        else:
            min = min
    arr[arr.index(min)], arr[i] = arr[i], min