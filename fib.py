def Fib(n):
    if n < 0:
        print("Positive numbers please")
    elif n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
print("Fibonacci numbers: ")
for i in range(1,10):
    print(Fib(i), end=" ")