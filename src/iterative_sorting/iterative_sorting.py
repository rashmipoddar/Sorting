# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        smallest_value = arr[smallest_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < smallest_value:
                smallest_index = j 
                smallest_value = arr[j]
            else:
                pass
        # TO-DO: swap
        # print('current index', cur_index)
        # print('smallest index', smallest_index)
        arr[smallest_index] = arr[cur_index] 
        arr[cur_index] = smallest_value 
        # print(arr)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(selection_sort(arr1))




    
