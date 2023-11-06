import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('csv/insurance.csv')
mean_bmi = data['bmi'].mean()
median_bmi = data['bmi'].median()
std_bmi = data['bmi'].std()

mean_charges = data['charges'].mean()
median_charges = data['charges'].median()
std_charges = data['charges'].std()

plt.hist(data['bmi'], bins=30, alpha=0.5, label='BMI')
plt.axvline(mean_bmi, color='red', linestyle='dashed', linewidth=2, label=f'Mean BMI: {mean_bmi:.2f}')
plt.axvline(median_bmi, color='green', linestyle='dashed', linewidth=2, label=f'Median BMI: {median_bmi:.2f}')
plt.axvline(mean_bmi + std_bmi, color='orange', linestyle='dashed', linewidth=2, label=f'Std BMI: {std_bmi:.2f}')
plt.legend()
plt.title('BMI Distribution')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()

plt.hist(data['charges'], bins=30, alpha=0.5, label='Charges')
plt.axvline(mean_charges, color='red', linestyle='dashed', linewidth=2, label=f'Mean Charges: {mean_charges:.2f}')
plt.axvline(median_charges, color='green', linestyle='dashed', linewidth=2,
            label=f'Median Charges: {median_charges:.2f}')
plt.axvline(mean_charges + std_charges, color='orange', linestyle='dashed', linewidth=2,
            label=f'Std Charges: {std_charges:.2f}')
plt.legend()
plt.title('Charges Distribution')
plt.xlabel('Charges')
plt.ylabel('Frequency')
plt.show()
