import pandas as pd
from scipy import stats

data = pd.read_csv('csv/insurance.csv')
confidence_level = 0.95
charges_mean = data['charges'].mean()
charges_std = data['charges'].std()
charges_n = len(data['charges'])
margin_of_error = stats.norm.ppf((1 + confidence_level)/2)*(charges_std/(charges_n**0.5))

charges_ci = (charges_mean - margin_of_error, charges_mean + margin_of_error)
print(f'95% Confidence Interval for Charges: {charges_ci}')

confidence_level = 0.99
margin_of_error = stats.norm.ppf((1 + confidence_level)/2)*(charges_std/(charges_n**0.5))

charges_ci = (charges_mean - margin_of_error, charges_mean + margin_of_error)
print(f'99% Confidence Interval for Charges: {charges_ci}')

bmi_mean = data['bmi'].mean()
bmi_std = data['bmi'].std()
bmi_n = len(data['bmi'])
margin_of_error = stats.norm.ppf((1 + confidence_level)/2)*(bmi_std/(bmi_n**0.5))

bmi_ci = (bmi_mean - margin_of_error, bmi_mean + margin_of_error)
print(f'99% Confidence Interval for BMI: {bmi_ci}')
