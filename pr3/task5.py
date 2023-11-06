import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('csv/insurance.csv')
data.boxplot(column=['age', 'bmi', 'charges'])
plt.title('Box Plot for Age, BMI and Charges')
plt.ylabel('Value')
plt.show()
