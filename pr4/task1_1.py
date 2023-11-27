import numpy as np


def first_correlation():
    # Два вектора - число автомобилей
    var1 = np.array([80, 98, 75, 91, 78])
    var2 = np.array([100, 82, 105, 89, 102])

    # Расчет коэффициента корреляции
    print(np.corrcoef(var1, var2)[0, 1])


first_correlation()
