#Searching in an sorted array
def binary_search(arr,l,end,key):
    mid = (l + end) // 2
    if arr[mid] == key:
        return mid
    
    if key > arr[mid]:
        return binary_search(arr,mid+1,end,key)
    
    if key < arr[mid]:
        return binary_search(arr,l,mid-1,key)
    

def main():
    arr = [1,2,3,4,5,6,7]
    key = 7
    print(binary_search(arr,0,len(arr)-1,key))
    

if __name__ == "__main__":   
    main()