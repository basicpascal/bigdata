def main():
    numbers = []

    while True:
        try:
            num = float(input("Введите число (для завершения введите 0): "))
        except ValueError:
            print("Ошибка: введите корректное число")
            continue

        numbers.append(num)
        if sum(numbers) == 0:
            break

    sum_of_squares = sum(x ** 2 for x in numbers)
    print(f"Сумма квадратов введенных чисел: {sum_of_squares}")


if __name__ == "__main__":
    main()
