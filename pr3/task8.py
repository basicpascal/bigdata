import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kstest, probplot

data = pd.read_csv('csv/insurance.csv')

# KS-тест
bmi_ks_stat, bmi_ks_p = kstest(data['bmi'], 'norm')
charges_ks_stat, charges_ks_p = kstest(data['charges'], 'norm')

print(f'KS-test for BMI: p-value = {bmi_ks_p}')
print(f'KS-test for Charges: p-value = {charges_ks_p}')

# q-q plot
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
probplot(data['bmi'], dist='norm', plot=plt)
plt.title('Q-Q Plot for BMI')

plt.subplot(1, 2, 2)
probplot(data['charges'], dist='norm', plot=plt)
plt.title('Q-Q Plot for Charges')
plt.show()
