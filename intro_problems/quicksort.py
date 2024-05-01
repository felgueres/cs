# Quicksort is the best comparison-based sorting algorithm 
# Quicksort has different implementations that vary on pivot selection 
# It's divide and conquer
# The recursion piece of the algo runs in O(n) 
# The pivot on average breaks the array in two
# Thus, quicksort runs in O(n * log n)

def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

arr = [1,1,2,5,4,5]
sorted_arr = quicksort(arr)
print(sorted_arr)