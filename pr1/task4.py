def generate_sequence(N):
    sequence = []
    for i in range(1, N + 1):
        sequence.extend([i] * i)
    return sequence


def main():
    N = int(input("Введите положительное целое число N: "))
    if N < 0:
        print("Ошибка: N должно быть положительным целым числом")
        return

    result = generate_sequence(N)
    print(*result[:N])


if __name__ == "__main__":
    main()
