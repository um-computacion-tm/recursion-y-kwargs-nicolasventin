def fibonacci(valor):
    if valor == 0:
        return 0
    if valor == 1:
        return 1
    return fibonacci(valor-1) + fibonacci(valor-2)