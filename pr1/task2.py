def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y


def floor_divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x // y


def absolute_value(x):
    return abs(x)


def power(x, y):
    return x ** y


def main():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, /, //, abs, pow): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation == '//':
        result = floor_divide(num1, num2)
    elif operation == 'abs':
        result = absolute_value(num1)
    elif operation == 'pow':
        result = power(num1, num2)
    else:
        result = "Ошибка: неверная операция"

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
