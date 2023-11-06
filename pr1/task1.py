import math


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_rectangle_area(length, width):
    return length * width


def calculate_circle_area(radius):
    return math.pi * radius ** 2


def main():
    shapes = ["Треугольник", "Прямоугольник", "Круг"]
    areas = {}

    for shape in shapes:
        if shape == "Треугольник":
            base = float(input("Введите длину основания треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            areas[shape] = calculate_triangle_area(base, height)
        elif shape == "Прямоугольник":
            length = float(input("Введите длину прямоугольника: "))
            width = float(input("Введите ширину прямоугольника: "))
            areas[shape] = calculate_rectangle_area(length, width)
        elif shape == "Круг":
            radius = float(input("Введите радиус круга: "))
            areas[shape] = calculate_circle_area(radius)

    print("Площади фигур: ")
    for shape, area in areas.items():
        print(f"{shape}: {area}")


if __name__ == "__main__":
    main()
