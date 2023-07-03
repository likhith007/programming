# Online Python compiler (interpreter) to run Python online.
# Write Python 3 cod

arr = [43,3,12,2,1]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    
    return arr

def selection_sort(arr):
    
    
    for i in range(0,len(arr)):
        min_val = arr[i]
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    
    return arr

def insertion_sort(arr):
    j = 1
    while j<len(arr):
        i = j-1
        while i >= 0:
            if arr[i+1]<arr[i]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
            i-=1
            
        j+=1
    
    return arr
    
def merge(left_arr,right_arr):
    result = []
    i = j =0
    
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1
    
    result += left_arr[i:] + right_arr[j:]
    
    return result
    
    

def merge_sort(arr):
    
    if len(arr)<=1:
        return arr
        
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left,right)
    
    
    
        
    
    
        
# print(selection_sort(arr))

# print(insertion_sort(arr))
        
# print(bubble_sort(arr))

# print(merge_sort(arr))


