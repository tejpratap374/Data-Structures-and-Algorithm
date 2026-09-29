# This function places the pivot element in its correct position.
# All elements smaller than the pivot move to the left, and all larger elements move to the right.
def partition(arr, low, high):
    pivot = arr[high]          # Choose the last element as the pivot
    i = low - 1                # Index of the smaller element region

    # Traverse the array and rearrange elements around the pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # Swap smaller element into the left partition

    # Put the pivot in its final sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Recursive quick sort function to divide and sort the array
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)   # Get pivot index

        # Recursively sort elements before and after the pivot
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Example usage
arr = [56, 12, 78, 34, 23, 90, 15]
n = len(arr)

print("Original array:", arr)

quickSort(arr, 0, n - 1)
print("Sorted array:", arr)