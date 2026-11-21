def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = list(map(int, input("Enter sorted elements separated by spaces: ").split()))
target = int(input("Enter element to search: "))
index = binary_search(arr, target)
if index == -1:
    print("Element not found")
else:
    print("Element found at index", index)
print("Time Complexity: O(log n)")
print("Auxiliary Space: O(1)")