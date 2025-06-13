def generate_fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Get number of terms from user
terms = int(input("Enter the number of terms: "))
result = generate_fibonacci(terms)

print("Fibonacci Series:")
print(result)