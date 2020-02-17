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
    swap_performed = True
    while swap_performed == True:
        if arr == []:
            swap_performed = False
        didSwap = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp_value = arr[i]
                arr[i] = arr[i + 1]
                arr [i + 1] = temp_value
                didSwap = True
            else:
                if didSwap == False and i == len(arr) - 2:
                    swap_performed = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(arr1))

print(bubble_sort(arr1))




    
