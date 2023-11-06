from scipy.stats import chisquare

observed_values = [97, 98, 109, 95, 97, 104]
chi2, p_value = chisquare(observed_values)

# Вывод результата
print(f"Статистика хи-квадрата: {chi2}")
print(f"P-значение: {p_value}")
if p_value > 0.05:
    print("Является")
else:
    print("Не является")
