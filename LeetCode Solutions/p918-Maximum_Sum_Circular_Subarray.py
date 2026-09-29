# Kadane's algorithm variant for a circular array.
# We track both the maximum subarray sum and the minimum subarray sum.
def maxSubarraySumCircular(nums):
    # total = sum of all elements in the array
    total = nums[0]

    # curMax = maximum sum ending at current index
    curMax = nums[0]
    maxSum = nums[0]

    # curMin = minimum sum ending at current index
    curMin = nums[0]
    minSum = nums[0]

    for i in range(1, len(nums)):
        x = nums[i]

        # Update maximum subarray ending here.
        curMax = curMax + x if curMax + x > x else x
        if curMax > maxSum:
            maxSum = curMax

        # Update minimum subarray ending here.
        curMin = curMin + x if curMin + x < x else x
        if curMin < minSum:
            minSum = curMin

        # Keep running total for the wrap-around case.
        total += x

    # If all values are negative, the best circular subarray is the max single element.
    if maxSum < 0:
        return maxSum

    # Compare normal max subarray and wrap-around subarray.
    return maxSum if maxSum > total - minSum else total - minSum


# Read input numbers from the user.
nums = list(map(int, input("Enter array elements: ").split()))

# Compute the maximum circular subarray sum.
maxSumSubarray = maxSubarraySumCircular(nums)
print(maxSumSubarray)