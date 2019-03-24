# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'}, inplace=True)
data.head(10)
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', (np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')))

#print(data.columns)
better_event = data['Better_Event'].value_counts().index[0]

#better_event = data.groupby(['Country_Name'])['Better_Event'].value_counts()

print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries.index[-1], inplace=True)

def top_ten(df,column):
    country_list = []
    country_list = df.nlargest(10, column)['Country_Name']
    return country_list.tolist()

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = list(set(top_10_summer).intersection(set(top_10_winter)).intersection(set(top_10)))


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer')
winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter')
top_df.plot(kind='bar',x='Country_Name',y='Total_Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']

max_summer = summer_df['Golden_Ratio'].idxmax()

summer_max_ratio = summer_df.ix[max_summer]['Golden_Ratio']
summer_country_gold = summer_df.ix[max_summer]['Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

max_winter = winter_df['Golden_Ratio'].idxmax()

winter_max_ratio = winter_df.ix[max_winter]['Golden_Ratio']
winter_country_gold = winter_df.ix[max_winter]['Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

max_winter = top_df['Golden_Ratio'].idxmax()

top_max_ratio = top_df.ix[max_winter]['Golden_Ratio']
top_country_gold = top_df.ix[max_winter]['Country_Name']


# --------------
#Code starts here
data_1 = data.drop(data.index[-1])

data_1['Total_Points'] = (data_1['Gold_Total'] * 3) + (data_1['Silver_Total'] * 2) + data_1['Bronze_Total']

max_point = data_1['Total_Points'].idxmax()

most_points = data_1.ix[max_point]['Total_Points']
best_country = data_1.ix[max_point]['Country_Name']

print('Best Country ', best_country, ' with points ', most_points)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)


