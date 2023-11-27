import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def first_correlation():
    # Два вектора - число автомобилей
    var1 = np.array([80, 98, 75, 91, 78])
    var2 = np.array([100, 82, 105, 89, 102])

    # Расчет коэффициента корреляции
    np.corrcoef(var1, var2)[0,1]

    # Диаграмма рассеивания 
    plt.grid(True)
    plt.title("Диаграмма рассеяния", fontsize = 20)
    plt.xlabel("Число машин припаркованных на улице")
    plt.ylabel("Число машин припаркованных в гараже")
    plt.scatter(var1, var2, marker='o', color='crimson')

def second_task():
    # Выгрузка данных
    data_2015 = pd.read_csv("csv/2015.csv")

    # Чтение данных
    data_2015.head()

    # Проверка на наличие пропущенных значений
    for column in data_2015.columns:
        missing = np.mean(data_2015[column].isna()*100)
        #print(f"{column} : {round(missing,1)}%")

    # Статистика по данным
    data_2015.describe()

    # Построение матрицы корреляции по одной целевой переменной
    #corr_matrix = data_2015.corr().Happiness_Score.to_frame().round(2)
   
    # Модель LinearRegression
    model = LinearRegression()

    # Переменные для модели
    x = data_2015[['Economy (GDP per Capita)']]
    y = data_2015['Happiness_Score']
    x = np.array(x, type(float))
    y = np.array(y, type(float))

    # Коэффициенты сдвига и наклона
    model.fit(x,y)
    #print(model.coef_, model.intercept_)
    
    # Построение модели с линией регрессии
    model_a = model.coef_[0]
    model_b = model.intercept_

    model_y_sk = model_a * x + model_b
    
    fig = plt.figure(figsize=(10, 6))
    plt.plot(x, model_y_sk, linewidth=2, color = 'r', label=f'linear_model = {model_a:.2f}x + {model_b:.2f}')
    plt.scatter(x, y, alpha=0.7)
    plt.grid()
    plt.xlabel('Economy (GDP per Capita)')
    plt.ylabel('Happiness Score')
    plt.legend(prop={'size': 16})

    # Нахождение MSE
    print(np.square(np.subtract(model_y_sk, y)).mean())

def third_task():
    # Предобработка данных
    data = pd.read_csv('csv/insurance.csv')
    data.head()
    for column in data.columns:
        missing = np.mean(data[column].isna()*100)
        #print(f"{column} : {round(missing,1)}%")
    data.describe()

    # Уникальные значения регионов
    data.region.unique()

    # Группируем данные индекса массы тела по региону
    frame = pd.DataFrame({'region':data['region'], 'bmi':data['bmi']})
    groups = frame.groupby('region').groups

    southwest = data['bmi'][groups['southwest']]
    southeast = data['bmi'][groups['southeast']]
    northwest = data['bmi'][groups['northwest']]
    northeast = data['bmi'][groups['northeast']]

    # Выполняем однофакторный ANOVA тест
    stats.f_oneway(southwest, southeast, northwest, northeast)

    # Выполняем ондофакторный ANOVA тест с помощью библиотеки statsmodel
    model = ols('bmi ~ region', data = frame).fit()
    anova_result = sm.stats.anova_lm(model, typ = 2)

    # Перебираем все пары
    regions = ['southwest', 'southeast', 'northwest', 'northeast']
    region_pairs = []
    for region1 in range(4):
        for region2 in range(region1 + 1, 4):
            region_pairs.append((regions[region1], regions[region2]))
    
    # t-test
    for region1, region2 in region_pairs:
        print(region1, region2)
        print(stats.ttest_ind(data['bmi'][groups[region1]], data['bmi'][groups[region2]]))


    # Пост-хок тест Тьюки
    #tukey = pairwise_tukeyhsd(endog= data['bmi'], groups=data['region'], alpha= 0.05)
    #tukey.plot_simultaneous()
    #tukey.summary()

    # Двухфакторный ANOVA test
    model_second = ols('bmi ~ C(region) + C(sex) + C(region):C(sex)', data=data).fit()
    print(sm.stats.anova_lm(model_second, typ=2))

    # Пост-хок тест Тьюки
    data['combination'] = data.region + ' / ' + data.sex
    tukey_second = pairwise_tukeyhsd(endog= data['bmi'], groups=data['combination'], alpha=0.05)
    tukey_second.plot_simultaneous()
    tukey_second.summary()
    plt.show()


#first_correlation()
#second_task()
third_task()
