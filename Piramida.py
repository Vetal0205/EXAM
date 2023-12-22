def pyramid_number(n):
    if n < 0:
        raise ValueError("Вхідне значення не може бути негативним")
    return n * (n + 1) * (n + 2) // 6

n = 5
print("Беслюбняк Віталій Сергійович МІТ-31")
print(f"Pyramid number for n={n} is {pyramid_number(n)}")
