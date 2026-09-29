def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - 1
    
    while right - left >= k:
        if abs((arr[left]) - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1
            
        a = [-1] * k
        for i in range(0, k):
            a[i] = arr[left + i]
        
        return a

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("k: "))
x = int(input("x: "))

ra = findClosestElements(arr, k ,x)
print(f"Closest Elements: {ra}")