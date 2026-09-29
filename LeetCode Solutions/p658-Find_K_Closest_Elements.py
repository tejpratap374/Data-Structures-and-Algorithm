# Find k elements in a sorted array that are closest to a target value x.
# We use a sliding window approach with two pointers.
def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - 1

    # Shrink the window until its size becomes exactly k.
    while right - left >= k:
        # Compare distances of the left and right ends from x.
        # If the right end is closer, remove the left side; otherwise remove the right side.
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1

    # Build the final k-element window starting from left.
    result = [-1] * k
    for i in range(k):
        result[i] = arr[left + i]

    return result


# Read the sorted array, k, and target x from user input.
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("k: "))
x = int(input("x: "))

closest = findClosestElements(arr, k, x)
print(f"Closest Elements: {closest}")