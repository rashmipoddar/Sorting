# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # print('Array A', arrA)
    # print('Array B', arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # print('Start merged array', merged_arr)
    for i in range(0, len(merged_arr)):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrB[0] < arrA[0]:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        # print('End merged array', merged_arr)    
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[ : len(arr) // 2 ])
        right = merge_sort(arr[ len(arr) // 2 : ])
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

# array = [1, 4, 3, 5]
array = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print('The sorted array is ', merge_sort(array))
