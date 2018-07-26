import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#iris = sns.load_dataset("iris")
#sns.swarmplot(x="species", y="petal_length", data=iris)

#tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
#sns.violinplot(x = "total_bill", data=tips)

# Regression Plot

tips = sns.load_dataset('tips')
sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips, palette = 'bright')



plt.show()