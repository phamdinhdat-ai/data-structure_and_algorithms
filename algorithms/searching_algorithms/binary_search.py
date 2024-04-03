# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1



def binary_search_recursion(arr, value, low, hight):
    
    if low <= hight:
        
        mid = low + (hight - low)//2 
        
        if arr[mid]  == value:
            return mid 
        
        
        elif arr[mid] > value:
            return binary_search_recursion(arr, value, low, mid - 1)
        
        else: 
            return binary_search_recursion(arr, value, mid + 1, hight)
    else:
        
        return -1  


# Time Complexities

# Best case complexity: O(1)
# Average case complexity: O(log n)
# Worst case complexity: O(log n)
# Space Complexity

# The space complexity of the binary search is O(1).


array = [3, 4, 5, 6, 7, 8, 9]
x = 4



result = binary_search_recursion(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
    
    
    
    
    