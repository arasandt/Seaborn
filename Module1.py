import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid", palette="bright") #style = {darkgrid, whitegrid, dark, white, ticks} #palette = deep, muted, pastel, bright, dark, and colorblind.

#Scatter Plot
iris = sns.load_dataset("iris")
#print(iris.head())
#sns.swarmplot(x="species", y="petal_length", data=iris)
#plt.show()

#iris = pd.melt(iris, "species", var_name="measurement") # "Melt" the dataset to "long-form" or "tidy" representation
#print(iris.head())
#sns.swarmplot(x="measurement", y="value", hue="species", palette=["r", "c", "y"], data=iris) # Draw a categorical scatterplot to show each observation, hue is to differentiate data points based on species
#plt.show()



#tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
#print(tips.head())
#sns.violinplot(x = "total_bill", data=tips) # box plot with density of variables

# Regression Plot
#tips = sns.load_dataset('tips')
#sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips, scatter_kws={"s": 200, "alpha": 0.5}) #, palette = 'bright')
#sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips, col='sex', scatter_kws={"s": 200, "alpha": 0.5}) # cols split into two or more graph based on the column value
# Plot tip as a function of toal bill across days

#g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species", truncate=True, size=5, data=iris) #truncate will truncate the regression line to the data point instead of end of plot/axis line. size is for the size of the plot.
# Use more informative axis labels than are provided by default
#g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")

#df = sns.load_dataset("anscombe")
#print(df.head())
#sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df, col_wrap=2, ci=None, palette="muted", size=4, scatter_kws={"s": 50, "alpha": 1}) #col_wrap wil wrap the plot canvas to number of subplots provided

#df = sns.load_dataset("titanic")
#print(df.head())
#pal = dict(male="#6495ED", female="#F08080") # Make a custom palette with gendered colors
# Show the survival proability as a function of age and sex
#g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df, palette='muted', y_jitter=.02, logistic=True) #y_jitter used for overlapping data
#g.set(xlim=(0, 80), ylim=(-.05, 1.05))


# Distribution Plot (Histogram)
#tips = sns.load_dataset('tips')
#sns.distplot(tips['total_bill'], bins=30, kde=False) #kde will remove the bell line on the histogram

# =============================================================================
# sns.set(style="white", palette="muted", color_codes=True)
# rs = np.random.RandomState(10) #randomnumber generating algo
# # Set up the matplotlib figure
# f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True) #2x2 and figsize is size of each subplot, sharex shares axis properties between subplot, the label of x axis will only be visible at the bottom
# sns.despine(left=True) # remove spines from plots
# # Generate a random univariate dataset
# d = rs.normal(size=100) # draw randon samples.
# print(d)
# # Plot a simple histogram with binsize determined automatically
# sns.distplot(d, kde=False, color="b", ax=axes[0, 0])
# # Plot a kernel density estimate and rug plot
# sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])
# # Plot a filled kernel density estimate
# sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0]) #kde_kws pass parm to the pyplot
# # Plot a historgram and kernel density estimate
# sns.distplot(d, color="m", ax=axes[1, 1])
# plt.setp(axes, yticks=[]) #set property of the yticks to be removed 
# plt.tight_layout() # decreases spaces between subplots
# =============================================================================

# =============================================================================
# #Joint Plot (scatter plot with histogram on x and y axis)
# tips = sns.load_dataset('tips')
# sns.jointplot(x= 'total_bill', y = 'tip', data=tips, kind='hex') # kind can have scatter, hex, regression
# 
# =============================================================================

# =============================================================================
# #pairplot (pairwise relationship, histogram and scatterplot )
# 
# #tips = sns.load_dataset('tips')
# #sns.pairplot(tips, hue='sex', palette='coolwarm') 
# sns.set(style="ticks")
# df = sns.load_dataset("iris")
# sns.pairplot(df, hue="species")
# =============================================================================

#barplot and factorplot

#tips = sns.load_dataset('tips')
#sns.barplot(x = 'sex', y='total_bill', data=tips)

#sns.set(style="white")
# Load the example planets dataset
#planets = sns.load_dataset("planets")
#print(planets.head())
#years = np.arange(2000, 2015) # Make a range of years to show categories with no observations
# Draw a count plot to show the number of planets discovered each year
#g = sns.factorplot(x="year", data=planets, kind="count", palette="BuPu", size=6, aspect=1.5, order=years) # order will order by the list on x axis, aspect is the width of the bar
#g.set_xticklabels(step=2) #step will provide label of the bar by skipping one bar, reduces clutter


sns.set(style="whitegrid")
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))
# Load the example car crash dataset
crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)
sns.set_color_codes("pastel") #how matplotlib handles shorthand color codes
sns.barplot(x="total", y="abbrev", data=crashes, label="Total", color="b") #label - x axis label (not legends)
# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="alcohol", y="abbrev", data=crashes, label="Alcohol-involved", color="b")
# Add a legend and informative axis label
#ax.legend(ncol=2, loc="lower right", frameon=True)
#ax.set(xlim=(0, 24), ylabel="",
#xlabel="Automobile collisions per billion miles")
sns.despine(left=True, bottom=True)









plt.show()