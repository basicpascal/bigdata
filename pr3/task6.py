import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('csv/insurance.csv')
sample_means_charges = []
sample_means_bmi = []
sample_size = 30 # Размер выборки

for _ in range(300):
    sample_charges = np.random.choice(data['charges'], size=sample_size)
    sample_bmi = np.random.choice(data['bmi'], size=sample_size)
    sample_means_charges.append(sample_charges.mean())
    sample_means_bmi.append(sample_bmi.mean())

plt.hist(sample_means_charges, bins=30, alpha=0.5, label='Sample Means Charges')
plt.axvline(np.mean(sample_means_charges), color='red', linestyle='dashed', linewidth=2, label=f'Mean Sample Means Charges: {np.mean(sample_means_charges):.2f}')
plt.axvline(np.std(sample_means_charges), color='green', linestyle='dashed', linewidth=2, label=f'Std Sample Means Charges: {np.mean(sample_means_charges):.2f}')
plt.legend()
plt.title('Sampling Distribution of Charges')
plt.xlabel('Mean Charges')
plt.ylabel('Frequency')
plt.show()

plt.hist(sample_means_bmi, bins=30, alpha=0.5, label='Sample Means BMI')
plt.axvline(np.mean(sample_means_bmi), color='red', linestyle='dashed', linewidth=2, label=f'Mean Sample Means BMI: {np.mean(sample_means_bmi):.2f}')
plt.axvline(np.std(sample_means_bmi), color='green', linestyle='dashed', linewidth=2, label=f'Std Sample Means BMI: {np.mean(sample_means_bmi):.2f}')
plt.legend()
plt.title('Sampling Distribution of BMI')
plt.xlabel('Mean BMI')
plt.ylabel('Frequency')
plt.show()
