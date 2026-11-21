def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)


def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


n = int(input("Enter n (0 to 20): "))
if 0 <= n <= 20:
    print("Recursive factorial:", recursive_factorial(n))
    print("Iterative factorial:", iterative_factorial(n))
    print("Time Complexity: O(n) for both")
    print("Auxiliary Space: O(n) recursive, O(1) iterative")
else:
    print("Enter a value between 0 and 20.")