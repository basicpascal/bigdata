import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly.express.trendline_functions import ols
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats


def third_task():
    # Предобработка данных
    data = pd.read_csv('csv/insurance.csv')
    data.head()
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        # print(f"{column} : {round(missing, 1)}%")
    data.describe()

    # Уникальные значения регионов
    data.region.unique()

    # Группируем данные индекса массы тела по региону
    frame = pd.DataFrame({'region': data['region'], 'bmi': data['bmi']})
    groups = frame.groupby('region').groups

    southwest = data['bmi'][groups['southwest']]
    southeast = data['bmi'][groups['southeast']]
    northwest = data['bmi'][groups['northwest']]
    northeast = data['bmi'][groups['northeast']]

    # Выполняем однофакторный ANOVA тест
    stats.f_oneway(southwest, southeast, northwest, northeast)

    # Выполняем ондофакторный ANOVA тест с помощью библиотеки statsmodel
    # model = ols('bmi ~ region', data=frame).fit()
    # anova_result = sm.stats.anova_lm(model, typ=2)

    # Перебираем все пары
    regions = ['southwest', 'southeast', 'northwest', 'northeast']
    region_pairs = []
    for region1 in range(4):
        for region2 in range(region1 + 1, 4):
            region_pairs.append((regions[region1], regions[region2]))

    # t-test
    # for region1, region2 in region_pairs:
    #     print(region1, region2)
    #     print(stats.ttest_ind(data['bmi'][groups[region1]], data['bmi'][groups[region2]]))

    # Пост-хок тест Тьюки
    # tukey = pairwise_tukeyhsd(endog=data['bmi'], groups=data['region'], alpha=0.05)
    # tukey.plot_simultaneous()
    # tukey.summary()

    # Двухфакторный ANOVA test
    # model_second = ols('bmi ~ C(region) + C(sex) + C(region):C(sex)', data=data).fit()
    # print(sm.stats.anova_lm(model_second, typ=2))

    # Пост-хок тест Тьюки
    data['combination'] = data.region + ' / ' + data.sex
    tukey_second = pairwise_tukeyhsd(endog=data['bmi'], groups=data['combination'], alpha=0.05)
    tukey_second.plot_simultaneous()
    tukey_second.summary()
    plt.show()


third_task()
