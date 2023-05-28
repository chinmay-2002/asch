def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        minind=i
        for j in range(i+1,n):
            if arr[j]<arr[minind]:
                minind=j
        arr[i],arr[minind]=arr[minind],arr[i]
        
    return arr



arr=[76,48,85,83,9,64]
sorted_arr=selection_sort(arr)
print(sorted_arr)