import pandas as pd
from scipy import stats

# Загрузка данных из файла
df = pd.read_csv('csv/bmi.csv')

# Создание двух выборок: northwest и southwest
bmi_northwest = df[df['region'] == 'northwest']['bmi']
bmi_southwest = df[df['region'] == 'southwest']['bmi']

# Проверка выборок на нормальность с использованием критерия Шапиро-Уилка
shapiro_stat_nw, shapiro_pvalue_nw = stats.shapiro(bmi_northwest)
shapiro_stat_sw, shapiro_pvalue_sw = stats.shapiro(bmi_southwest)

print(f"Shapiro-Wilk Test for Northwest BMI (p-value): {shapiro_pvalue_nw}")
print(f"Shapiro-Wilk Test for Southwest BMI (p-value): {shapiro_pvalue_sw}")

# Проверка гомогенности дисперсии с использованием критерия Бартлетта
bartlett_stat, bartlett_pvalue = stats.bartlett(bmi_northwest,bmi_southwest)
print(f"Bartlett's Test for Homogenetity of Variances (p-value): {bartlett_pvalue}")

# Применение t-критерия Стьюдента для сравнения средних значений выборок
if shapiro_pvalue_nw > 0.05 and shapiro_pvalue_sw > 0.05 and bartlett_pvalue > 0.05:
    t_stat, t_pvalue = stats.ttest_ind(bmi_northwest,bmi_southwest)
    print(f"t-критерий Стьюдента (p-value): {t_pvalue}")

    if t_pvalue < 0.05:
        print("Средние значения различаются (отвергаем нулевую гипотезу)")
    else:
        print("Средние значения схожи (не отвергаем нулевую гипотезу)")
else:
    print("Условия для применения t-критерия не выполняются (невозможно провести анализ)")
