import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt



# Read datas
#print(os.listdir("./input"))

median_house_hold_in_come = pd.read_csv('./input/MedianHouseholdIncome2015.csv', encoding="windows-1252")
percentage_people_below_poverty_level = pd.read_csv('./input/PercentagePeopleBelowPovertyLevel.csv', encoding="windows-1252")
percent_over_25_completed_highSchool = pd.read_csv('./input/PercentOver25CompletedHighSchool.csv', encoding="windows-1252")
share_race_city = pd.read_csv('./input/ShareRaceByCity.csv', encoding="windows-1252")
kill = pd.read_csv('./input/PoliceKillingsUS.csv', encoding="windows-1252")

# =============================================================================
# print(median_house_hold_in_come.head())
# print(percentage_people_below_poverty_level.head())
# print(percent_over_25_completed_highSchool.head())
# print(share_race_city.head())
# print(kill.head())
# 
# =============================================================================

# =============================================================================
# percentage_people_below_poverty_level['poverty_rate'].replace('-','0.0',inplace=True)
# percentage_people_below_poverty_level['poverty_rate'] = percentage_people_below_poverty_level['poverty_rate'].astype(float)
# datax = pd.pivot_table(percentage_people_below_poverty_level, values='poverty_rate', index =['Geographic Area'], aggfunc=np.mean)
# datax['state'] = datax.index
# datax = datax.sort_values(by=['poverty_rate'], ascending=False)
# #print(datax)
# f, ax = plt.subplots(figsize=(15, 10))
# sns.barplot(x='state', y='poverty_rate', data=datax)
# ax.set_xticklabels(datax['state'], rotation=45)
# ax.set_ylabel('Poverty Rate')
# ax.set_xlabel('States')
# ax.set_title('Poverty Rate Given States')
# 
# 
# =============================================================================

# =============================================================================
# vnames = list(kill['name'])
# vnamedict={}
# for i in vnames:
#     for j in i.split():
#         x = vnamedict.get(j,0)
#         vnamedict[j] = x + 1
# #print(vnamedict)
# vnames = pd.DataFrame.from_dict(vnamedict,orient='index',columns=['Count'])
# vnames['Name'] = vnames.index
# vnames = vnames.reset_index(drop=True)
# vnames = vnames[vnames != 'TK'].dropna()
# vnames = vnames.sort_values(by=['Count'],ascending=False)
# f, ax = plt.subplots(figsize=(15, 10))
# sns.barplot(x='Name', y='Count', data=vnames.head(15))
# ax.set_ylabel('Frequency')
# ax.set_xlabel('Name or Surname of killed people')
# ax.set_title('Most common 15 Name or Surname of killed people')
# 
# =============================================================================

# =============================================================================
# percent_over_25_completed_highSchool['percent_completed_hs'].replace('-','0.0',inplace=True)
# percent_over_25_completed_highSchool['percent_completed_hs'] = percent_over_25_completed_highSchool['percent_completed_hs'].astype(float)
# datax = pd.pivot_table(percent_over_25_completed_highSchool, values='percent_completed_hs', index =['Geographic Area'], aggfunc=np.mean)
# datax['state'] = datax.index
# datax = datax.sort_values(by=['percent_completed_hs'], ascending=True)
# print(datax)
# f, ax = plt.subplots(figsize=(15, 10))
# sns.barplot(x='state', y='percent_completed_hs', data=datax)
# ax.set_xticklabels(datax['state'], rotation=90)
# ax.set(xlabel='States', ylabel='High School Graduate Rate',title = "Percentage of Given State's Population Above 25 that Has Graduated High School")
# =============================================================================


# =============================================================================
# print(share_race_city.head(10))
# 
# share_race_city['share_white'].replace('(X)','0.0',inplace=True)
# share_race_city['share_white'] = share_race_city['share_white'].astype(float)
# share_race_city['share_black'].replace('(X)','0.0',inplace=True)
# share_race_city['share_black'] = share_race_city['share_black'].astype(float)
# share_race_city['share_native_american'].replace('(X)','0.0',inplace=True)
# share_race_city['share_native_american'] = share_race_city['share_native_american'].astype(float)
# share_race_city['share_asian'].replace('(X)','0.0',inplace=True)
# share_race_city['share_asian'] = share_race_city['share_asian'].astype(float)
# share_race_city['share_hispanic'].replace('(X)','0.0',inplace=True)
# share_race_city['share_hispanic'] = share_race_city['share_hispanic'].astype(float)
# 
# datax = pd.pivot_table(share_race_city, values=['share_white', 'share_black','share_native_american', 'share_asian', 'share_hispanic'], index =['Geographic area'], aggfunc=np.mean)
# datax['state'] = datax.index
# datax = datax.sort_values(by=['state'], ascending=True)
# f, ax = plt.subplots(figsize=(10, 13))
# sns.barplot(x='share_white', y='state', data=datax, color='b', label="White", alpha = 0.75)
# sns.barplot(x='share_black', y='state', data=datax, color='r', label="Black", alpha = 0.75)
# sns.barplot(x='share_native_american', y='state', data=datax, color='Gold', label="Native America", alpha = 0.75)
# sns.barplot(x='share_asian', y='state', data=datax, color='g', label="Asian", alpha = 0.75)
# sns.barplot(x='share_hispanic', y='state', data=datax, color='c', label="Hispanic", alpha = 0.75)
# ax.legend(loc="upper right", frameon=True)
# ax.set(xlabel='Percentage of Races', ylabel='States',title = "Percentage of State's Population According to Races ")
#         
# =============================================================================

# =============================================================================
# 
# percent_over_25_completed_highSchool['percent_completed_hs'].replace('-','0.0',inplace=True)
# percent_over_25_completed_highSchool['percent_completed_hs'] = percent_over_25_completed_highSchool['percent_completed_hs'].astype(float)
# datax = pd.pivot_table(percent_over_25_completed_highSchool, values='percent_completed_hs', index =['Geographic Area'], aggfunc=np.mean)
# datax['percent_completed_hs'] = datax['percent_completed_hs'] / max(datax['percent_completed_hs'])
# #print(datax.head())
# 
# percentage_people_below_poverty_level['poverty_rate'].replace('-','0.0',inplace=True)
# percentage_people_below_poverty_level['poverty_rate'] = percentage_people_below_poverty_level['poverty_rate'].astype(float)
# datay = pd.pivot_table(percentage_people_below_poverty_level, values='poverty_rate', index =['Geographic Area'], aggfunc=np.mean)
# datay['poverty_rate'] = datay['poverty_rate'] / max(datay['poverty_rate'])
# #print(datay.head())
# 
# data = pd.merge(datax, datay, left_index=True, right_index=True)
# data['state'] = datax.index
# data.sort_values(by=['poverty_rate'],inplace=True)
# #print(data.head())
# f, ax = plt.subplots(figsize=(15, 10))
# sns.pointplot(x='state',y='percent_completed_hs',data=data, color='r')
# sns.pointplot(x='state',y='poverty_rate',data=data, color='g')
# ax.legend(loc="lower right", frameon=True)
# ax.set(xlabel='States', ylabel='Values',title = "High School Graduate  VS  Poverty Rate")
# 
# sns.jointplot(data['poverty_rate'], data['percent_completed_hs'], kind="kde", size=7)
# sns.jointplot(data['poverty_rate'], data['percent_completed_hs'], size=7, ratio=3, color='r')
#         
# =============================================================================

sns.swarmplot(x="gender", y="age",hue="manner_of_death", data=kill)
print('Hello World!!')