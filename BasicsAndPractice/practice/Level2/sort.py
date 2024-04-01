def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1] :
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

# Test the function
arr = [5,4,7,1]
print("Original array is:", arr)
bubble_sort(arr)
print("Sorted array is:", arr)
