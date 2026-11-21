n = int(input("Enter number of items: "))
items = []
for i in range(n):
    value, weight = map(float, input(f"Enter value and weight of item {i + 1}: ").split())
    if weight <= 0:
        raise ValueError("Weight must be positive")
    items.append((value, weight, value / weight))

capacity = float(input("Enter knapsack capacity: "))
items.sort(key=lambda item: item[2], reverse=True)
total_value = 0.0

for value, weight, ratio in items:
    if capacity <= 0:
        break
    taken = min(capacity, weight)
    total_value += taken * ratio
    capacity -= taken

print(f"Maximum value: {total_value:.2f}")
print("Time Complexity: O(n log n)")
