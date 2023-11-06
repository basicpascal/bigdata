import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('csv/insurance.csv')
data.hist(figsize=(12, 8))
plt.show()
