def fibonacci(n):
    fibo = [0, 1]
    while fibo[-1] < n:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

def is_fibonacci(num):
    fibo = fibonacci(num)
    if num in fibo:
        return f"O número {num} pertence"
    else:
        return f"O número {num} não pertence"
    
numero = int(input("Informe um número: "))
print(is_fibonacci(numero))