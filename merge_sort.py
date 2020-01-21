# merge sort - how can we sort better than n^2?
# start with an array and break it down into small sorted arrays, then combine

# breakdown into small sorted arrays is O(log(n)) (use recursion)

# merging step: two-finger algorithm
# L = [2, 7, 13, 20]
# R = [1, 9, 11, 12]
# step pointers (fingers) separately through L and R, picking off smallest element
# add each sequentially larger value to final sorted array
# O(n) linear time for merging

input = [7, 3, 5, 2, 1, 4, 8, 6]

def merge_sort(arr):
    print(f'calling mergesort with {arr}')
    arr_length = len(arr)
    if arr_length < 2:
        print('reached length < 2')
        return arr
    sorted_arr = []
    mid = arr_length//2
    left_arr = merge_sort(arr[0:mid])
    right_arr = merge_sort(arr[mid:])
    print(f'left arr: {left_arr}')
    print(f'right arr: {right_arr}')
    i, j = 0, 0
    while i < mid and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            print(f'added {left_arr[i]} to sorted_arr')
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            print(f'added {right_arr[j]} to sorted_arr')
            j += 1
    if i < mid:
        sorted_arr.extend(left_arr[i:])
        print(f'added {left_arr[i:]} to sorted_arr')
    elif j < len(right_arr):
        sorted_arr.extend(right_arr[j:])
        print(f'added {right_arr[j:]} to sorted_arr')

    print(sorted_arr)

    return sorted_arr

print(merge_sort(input))

