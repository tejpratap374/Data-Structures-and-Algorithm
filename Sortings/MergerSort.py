# Merge two sorted halves of the array into one sorted array.
def merge(arr, left, mid, right):
    # Sizes of the left and right halves
    n1 = mid - left + 1
    n2 = right - mid

    # Temporary arrays to hold the two halves
    L = [0] * n1
    R = [0] * n2

    # Copy data into temporary arrays
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    # Merge the two halves back into the original array
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements from the left half
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements from the right half
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Recursive merge sort function
# Divides the array into two halves, sorts them, and then merges them.
def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Sort the left and right halves
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)

# Example usage
Id = [38, 27, 43, 3, 9, 82, 10, 19]
n = len(Id)

print("Original Ids': ", Id)

mergeSort(Id, 0, n - 1)
print("Sorted Ids': ", Id)
