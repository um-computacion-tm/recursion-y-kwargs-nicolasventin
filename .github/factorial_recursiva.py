def factorial(valor):
    if valor in (0, 1):
        return 1
    return valor * factorial(valor -1)