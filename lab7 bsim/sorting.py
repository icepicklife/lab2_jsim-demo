def sort(n, arr):
    # Bubble sort
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    new_arr = [n] + arr
        
    return new_arr

print(sort(7,[5,7,8,6,4,9,3]))