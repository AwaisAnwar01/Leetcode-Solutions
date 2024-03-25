def fibonacci(n):
    if n <= 1:
        return n

    # Initialize an array to store Fibonacci numbers
    fib = [0] * (n + 1)
    fib[1] = 1

    # Compute Fibonacci numbers iteratively
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Example usage:
n = 8
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
