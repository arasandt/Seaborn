import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid", palette="bright") #style = {darkgrid, whitegrid, dark, white, ticks} #palette = deep, muted, pastel, bright, dark, and colorblind.

# =============================================================================
# #Scatter Plot
# iris = sns.load_dataset("iris")
# #print(iris.head())
# #sns.swarmplot(x="species", y="petal_length", data=iris)
# #plt.show()
# 
# #iris = pd.melt(iris, "species", var_name="measurement") # "Melt" the dataset to "long-form" or "tidy" representation
# #print(iris.head())
# #sns.swarmplot(x="measurement", y="value", hue="species", palette=["r", "c", "y"], data=iris) # Draw a categorical scatterplot to show each observation, hue is to differentiate data points based on species
# #plt.show()
# 
# =============================================================================


# =============================================================================
# #Voilin Plot (# box plot with density of variables)
# 
# #tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
# #print(tips.head())
# #sns.violinplot(x = 'day', y = "total_bill", data=tips,palette='rainbow') 
# 
# 
# #rs = np.random.RandomState(0)
# #n, p = 40, 8 #40 size with 8 elements each
# #d = rs.normal(0, 2, (n, p))
# #d += np.log(np.arange(1, p + 1)) * -5 + 10
# # Use cubehelix to get a custom sequential palette
# #pal = sns.cubehelix_palette(p, rot=-.5, dark=.3) #generates heatmap palette rot=rotation aournd hue wheel. dark = intensity of the darkest color in palette
# 
# # Show each distribution with both violins and points
# #sns.violinplot(data=d, palette=pal, inner="points") # inner = how to represent the polt inside the voilin
# 
# sns.set(style="whitegrid")
# # Load the example dataset of brain network correlations
# df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)
# # Pull out a specific subset of networks
# used_networks = [1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17]
# used_columns = (df.columns.get_level_values("network").astype(int).isin(used_networks)) #astype converts string index to int index
# df = df.loc[:, used_columns] #slice the axis based on boolean value. used_columns should be of same size
# # Compute the correlation matrix and average over networks
# corr_df = df.corr().groupby(level="network").mean()
# corr_df.index = corr_df.index.astype(int)
# corr_df = corr_df.sort_index().T # T for transpose
# #print(corr_df)
# # Set up the matplotlib figure
# f, ax = plt.subplots(figsize=(11, 6))
# # Draw a violinplot with a narrower bandwidth than the default
# sns.violinplot(data=corr_df, palette="Set3" , bw=.2, cut=1 , linewidth=1) #bw is {‘scott’, ‘silverman’, float} narrow bw de-smoothes the voilin density graph, cut trims the trails on the data, linewidth is the width of the elements or border
# # Finalize the figure
# ax.set(ylim=(-.7, 1.05))
# sns.despine(left=True, bottom=True) #remove the lines because desping acts only on top and right spines
# 
# =============================================================================
# =============================================================================
# # Regression Plot
# #tips = sns.load_dataset('tips')
# #sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips, scatter_kws={"s": 200, "alpha": 0.5}) #, palette = 'bright')
# #sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips, col='sex', scatter_kws={"s": 200, "alpha": 0.5}) # cols split into two or more graph based on the column value
# # Plot tip as a function of toal bill across days
# 
# #g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species", truncate=True, size=5, data=iris) #truncate will truncate the regression line to the data point instead of end of plot/axis line. size is for the size of the plot.
# # Use more informative axis labels than are provided by default
# #g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
# 
# #df = sns.load_dataset("anscombe")
# #print(df.head())
# #sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df, col_wrap=2, ci=None, palette="muted", size=4, scatter_kws={"s": 50, "alpha": 1}) #col_wrap wil wrap the plot canvas to number of subplots provided
# 
# #df = sns.load_dataset("titanic")
# #print(df.head())
# #pal = dict(male="#6495ED", female="#F08080") # Make a custom palette with gendered colors
# # Show the survival proability as a function of age and sex
# #g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df, palette='muted', y_jitter=.02, logistic=True) #y_jitter used for overlapping data
# #g.set(xlim=(0, 80), ylim=(-.05, 1.05))
# =============================================================================


# =============================================================================
# # Distribution Plot (Histogram)
# #tips = sns.load_dataset('tips')
# #sns.distplot(tips['total_bill'], bins=30, kde=False) #kde will remove the bell line on the histogram
# =============================================================================

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

# =============================================================================
# #barplot and factorplot
# 
# #tips = sns.load_dataset('tips')
# #sns.barplot(x = 'sex', y='total_bill', data=tips)
# 
# #sns.set(style="white")
# # Load the example planets dataset
# #planets = sns.load_dataset("planets")
# #print(planets.head())
# #years = np.arange(2000, 2015) # Make a range of years to show categories with no observations
# # Draw a count plot to show the number of planets discovered each year
# #g = sns.factorplot(x="year", data=planets, kind="count", palette="BuPu", size=6, aspect=1.5, order=years) # order will order by the list on x axis, aspect is the width of the bar
# #g.set_xticklabels(step=2) #step will provide label of the bar by skipping one bar, reduces clutter
# 
# 
# sns.set(style="whitegrid")
# # Initialize the matplotlib figure
# f, ax = plt.subplots(figsize=(6, 15))
# # Load the example car crash dataset
# crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)
# #print(crashes.head())
# sns.set_color_codes("pastel") #how matplotlib handles shorthand color codes
# sns.barplot(x="total", y="abbrev", data=crashes, label="Total", color="b") #label - x axis label (not legends)
# # Plot the crashes where alcohol was involved
# sns.set_color_codes("muted")
# sns.barplot(x="alcohol", y="abbrev", data=crashes, label="Alcohol-involved", color="b")
# # Add a legend and informative axis label
# ax.legend(ncol=2, loc="lower right", frameon=True) #ncol tell how many legends are there in the bar to show in a single row. frameon givs border to the legend
# ax.set(xlim=(0, 24), ylabel="", xlabel="Automobile collisions per billion miles")
# sns.despine(left=True, bottom=True)
# 
# =============================================================================

# =============================================================================
# #count plot (count the number of items in a df)
# tips = sns.load_dataset('tips')
# sns.countplot(x = 'sex', data = tips)
# 
# =============================================================================

# =============================================================================
# #box plot (plot for median, mean, mod, high, low, outliers)
# #tips = sns.load_dataset('tips')
# #sns.boxplot(x = 'day', y='total_bill', hue='smoker', data=tips, palette='rainbow')
# 
# sns.set(style="ticks")
# # Initialize the figure with a logarithmic x axis
# f, ax = plt.subplots(figsize=(7, 6))
# ax.set_xscale("log")
# planets = sns.load_dataset("planets")
# # Plot the orbital period with horizontal boxes
# sns.boxplot(x="distance", y="method", data=planets, palette="rainbow", whis=np.inf) #whis removes the outlier beyond whiskers on the plot
# # Add in points to show each observation
# sns.swarmplot(x="distance", y="method", data=planets, size=2, color="0.5", linewidth=0) #color goes from 0=black to 1=white, so inbetween its grey. linewidth= 0 removes the circle around the elements 
# # Tweak the visual presentation
# ax.xaxis.grid(True)
# ax.set(ylabel="")
# sns.despine(trim=True, left=True)
# =============================================================================

# =============================================================================
# 
# #Heat Plot
# 
# #flights = sns.load_dataset('flights')
# #pvflights = flights.pivot_table(values='passengers', index='month', columns='year') #index gives row
# #sns.heatmap(pvflights, linecolor='white', linewidths=1, cmap='Greens', annot=False) #linecolor gives border for each heat box and linewidths gives the size #cmap = YlGnBu, coolwarm,BuPu, Greens, Blues and annot= fills the heatbox with values
# 
# #flights_long = sns.load_dataset("flights")
# #flights = flights_long.pivot("month", "year", "passengers") #index, column, value
# # Draw a heatmap with the numeric values in each cell
# #f, ax = plt.subplots(figsize=(9, 6))
# #sns.heatmap(flights, annot=True, fmt="d", linewidths=1)#, ax=ax) #fmt formats the boxvalue to decimal , ax  tell which subplot to draw
# 
# 
# from string import ascii_letters
# sns.set(style="white")
# # Generate a large random dataset
# rs = np.random.RandomState(33) #33 is the seed
# 
# d = pd.DataFrame(data=rs.normal(size=(100, 26)),columns=list(ascii_letters[26:])) #ascii_letters contains lower case and then upper case letters a-z
# corr = d.corr()
# # Generate a mask for the upper triangle
# mask = np.zeros_like(corr, dtype=np.bool) #give corr return same type of array. dtype used to change arr to bool
# mask[np.triu_indices_from(mask)] = True #triu_indices_from gets upper index - does not count indexes incrementally
# print(mask)
# # Set up the matplotlib figure
# f, ax = plt.subplots(figsize=(11, 9))
# # Generate a custom diverging colormap
# cmap = sns.diverging_palette(220, 10, as_cmap=True) # as_cmap to set return value as colormap object, 220 & 10 are hues
# # Draw the heatmap with the mask and correct aspect ratio
# sns.heatmap(corr, cmap=cmap, linewidths=.5, square=True, center=0, vmax=0.3,cbar_kws={"shrink": .5}, mask=mask) #square = sq the axes for boxes are sqaure, center not sure what it does but it gives contrast if 0, vmax = max value of the plot data, cbar_kws shrink reduces the size(length) of the color bar at the right, mask data not shown when its true
# 
# 
# =============================================================================


plt.show()