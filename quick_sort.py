input = [7, 3, 5, 2, 1, 4, 8, 6]

def partition(arr, begin, end):
    print (arr, begin, end)
    if (begin < end):
        # select pivot to be final element
        pivot = arr[end]
        # used to count swaps made for values less than pivot
        i = begin - 1
        print(arr[begin:end+1])
        for index, value in enumerate(arr[begin:end], start=begin):
            print (index, value, pivot)
            if value <= pivot:
                # found a value smaller than pivot, increment i
                i += 1
                # place value in ith position  
                arr[index], arr[i] = arr[i], arr[index]
        # place pivot in position i+1, after all smaller values
        arr[i+1], arr[end] = arr[end], arr[i+1]
        return i+1
    else:
        return end

def quicksort(arr, begin, end):
    if (begin < end):
        # find final index of pivot chosen by partition()
        partition_index = partition(arr, begin, end)
        # recursively sort side of arr with elements less than arr[pivot]
        quicksort(arr, begin, partition_index - 1)
        # recursively sort side of arr with elements greater than arr[pivot]
        quicksort(arr, partition_index + 1, end)

print(quicksort(input, 0, 7))
