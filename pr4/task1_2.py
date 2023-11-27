import numpy as np
from matplotlib import pyplot as plt


def first_correlation():
    # Два вектора - число автомобилей
    var1 = np.array([80, 98, 75, 91, 78])
    var2 = np.array([100, 82, 105, 89, 102])

    # Расчет коэффициента корреляции
    print(np.corrcoef(var1, var2)[0, 1])

    # Диаграмма рассеивания
    plt.grid(True)
    plt.title("Диаграмма рассеяния", fontsize=20)
    plt.xlabel("Число машин припаркованных на улице")
    plt.ylabel("Число машин припаркованных в гараже")
    plt.scatter(var1, var2, marker='o', color='crimson')
    plt.show()


first_correlation()
