# bubbleSort(array)
#   for i <- 1 to indexOfLastUnsortedElement-1
#     if leftElement > rightElement
#       swap leftElement and rightElement
# end bubbleSort


def bubble_sort(array):
    #  Time complexity O(n^2)
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i  - 1):
            
            if array[j] > array[j + 1]:
                swapped = True
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1 ]  = temp
        if not swapped:
            break
data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print('Sorted Array in Ascending Order:')
print(data)