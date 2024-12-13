#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd
import matplotlib.pyplot as plt


# In[95]:


avocado_df = pd.read_csv('../dataset/avocado_df.csv')


# In[96]:


avocado_df.info()


# In[97]:


avocado_df.describe()


# In[98]:


avocado_df.count()


# In[99]:


unique_values = avocado_df.nunique()
unique_values


# In[100]:


print(avocado_df['Geography'].unique())


# In[101]:


avocado_df.head()


# In[102]:


cities = ['Albany', 'Atlanta', 'Boise', 'Boston', 'Charlotte', 'Chicago', 'Columbus', 
          'Denver', 'Detroit', 'Grand Rapids', 'Houston', 'Indianapolis', 'Jacksonville', 
          'Las Vegas', 'Los Angeles', 'Louisville', 'Nashville', 'New York', 'Orlando', 
          'Philadelphia', 'Pittsburgh', 'Providence', 'Portland', 'Roanoke', 'Sacramento', 
          'San Diego', 'San Francisco', 'Seattle', 'Spokane', 'St. Louis', 'Syracuse', 
          'Tampa', 'Toledo', 'Wichita']

regions = ['Baltimore/Washington', 'Birmingham/Montgomery', 'Buffalo/Rochester', 
           'Cincinnati/Dayton', 'Dallas/Ft. Worth', 'Harrisburg/Scranton', 
           'Hartford/Springfield', 'Miami/Ft. Lauderdale', 'New Orleans/Mobile', 
           'Northern New England', 'Peoria/Springfield', 'Phoenix/Tucson', 
           'Raleigh/Greensboro', 'Richmond/Norfolk', 'South Carolina', 'West Tex/New Mexico']

greaterregions = ['California', 'Great Lakes', 'Midsouth', 'Northeast', 'Plains', 
                  'South Central', 'Southeast', 'West']


# In[103]:


filtered_df_greaterregions = avocado_df[avocado_df['Geography'].isin(greaterregions)]

filtered_df_greaterregions.head()


# In[104]:


file_paths = ['../dataset/Volume Hass Avocado Board Suppliers 2022.csv',
              '../dataset/Volume Hass Avocado Board Suppliers 2023.csv',
              '../dataset/Volume Hass Avocado Board Suppliers 2024.csv',
              '../dataset/Volume Hass Avocado Board Suppliers 2025 (projection).csv']

suppliers_df = pd.concat([pd.read_csv(file) for file in file_paths])

suppliers_df.to_csv('../dataset/merged_suppliers.csv', index=False)

print(suppliers_df.info())


# In[105]:


#Univardiado


# In[106]:


#Bivariado

#Trimestre vs Total Volumne (venta)
#Regiones vs Total volumen (venta)
#Trimestre vs AVG precio


# In[107]:


import pandas as pd
import matplotlib.pyplot as plt

avocado_df = pd.read_csv('../dataset/avocado_df.csv')

cities = ['Albany', 'Atlanta', 'Boise', 'Boston', 'Charlotte', 'Chicago', 'Columbus', 
          'Denver', 'Detroit', 'Grand Rapids', 'Houston', 'Indianapolis', 'Jacksonville', 
          'Las Vegas', 'Los Angeles', 'Louisville', 'Nashville', 'New York', 'Orlando', 
          'Philadelphia', 'Pittsburgh', 'Providence', 'Portland', 'Roanoke', 'Sacramento', 
          'San Diego', 'San Francisco', 'Seattle', 'Spokane', 'St. Louis', 'Syracuse', 
          'Tampa', 'Toledo', 'Wichita']

regions = ['Baltimore/Washington', 'Birmingham/Montgomery', 'Buffalo/Rochester', 
           'Cincinnati/Dayton', 'Dallas/Ft. Worth', 'Harrisburg/Scranton', 
           'Hartford/Springfield', 'Miami/Ft. Lauderdale', 'New Orleans/Mobile', 
           'Northern New England', 'Peoria/Springfield', 'Phoenix/Tucson', 
           'Raleigh/Greensboro', 'Richmond/Norfolk', 'South Carolina', 'West Tex/New Mexico']

greaterregions = ['California', 'Great Lakes', 'Midsouth', 'Northeast', 'Plains', 
                  'South Central', 'Southeast', 'West']

filtered_df_greaterregions = avocado_df[avocado_df['Geography'].isin(greaterregions)]


# In[108]:


filtered_df_greaterregions.head()


# In[109]:


import pandas as pd
import matplotlib.pyplot as plt

filtered_df_greaterregions['Current Year Week Ending'] = pd.to_datetime(filtered_df_greaterregions['Current Year Week Ending'])

filtered_df_greaterregions['Quarter'] = filtered_df_greaterregions['Current Year Week Ending'].dt.to_period('Q')

quarterly_mean = filtered_df_greaterregions.groupby('Quarter')['Total Bulk and Bags Units'].mean()

plt.figure(figsize=(10, 6))
quarterly_mean.plot(kind='bar')
plt.xlabel('Trimestre')
plt.ylabel('Media del total de unidades a granel y en sacos (lb)')
plt.title('Grandes regiones: Media del total de unidades a granel y en sacos (lb) por Trimestre')
plt.show()


# In[110]:


# Group by "Geography" and calculate the mean of "Total Bulk and Bags Units"
geography_mean = filtered_df_greaterregions.groupby('Geography')['Total Bulk and Bags Units'].mean()

# Plot the data
plt.figure(figsize=(12, 8))
geography_mean.plot(kind='bar')
plt.xlabel('Grandes regiones')
plt.ylabel('Media del total de unidades a granel y en sacos (lb)')
plt.title('Media del total de unidades a granel y en sacos (lb) por Grandes regiones')
plt.xticks(rotation=45)
plt.show()


# In[111]:


quarterly_mean = filtered_df_greaterregions.groupby('Quarter')['ASP Current Year'].mean()

plt.figure(figsize=(10, 6))
quarterly_mean.plot(kind='bar')
plt.xlabel('Trimestre')
plt.ylabel('Precio medio de venta año en curso')
plt.title('Grandes regiones: Media del precio medio de venta año en curso por Trimestre')
plt.show()


# In[112]:


# Sort the DataFrame by "Current Year Week Ending", "Geography", and "Type"
filtered_df_greaterregions = filtered_df_greaterregions.sort_values(by=['Current Year Week Ending', 'Geography', 'Type'])

# Filter the DataFrame to include only rows where Geography is "California" and Type is "Organic"
california_organic_df = filtered_df_greaterregions[(filtered_df_greaterregions['Geography'] == 'California') & (filtered_df_greaterregions['Type'] == 'Organic')]
# Filter the DataFrame to include only rows where Geography is "California" and Type is "Conventional"
california_conventional_df = filtered_df_greaterregions[(filtered_df_greaterregions['Geography'] == 'California') & (filtered_df_greaterregions['Type'] == 'Conventional')]

# Calculate the percentage change for Total Bulk and Bags Units and ASP Current Year
california_organic_df['Pct_Change_Units'] = california_organic_df['Total Bulk and Bags Units'].pct_change()
california_organic_df['Pct_Change_Price'] = california_organic_df['ASP Current Year'].pct_change()

california_conventional_df['Pct_Change_Units'] = california_conventional_df['Total Bulk and Bags Units'].pct_change()
california_conventional_df['Pct_Change_Price'] = california_conventional_df['ASP Current Year'].pct_change()

# Calculate the price elasticity of demand
california_organic_df['Elasticity'] = california_organic_df['Pct_Change_Units'] / california_organic_df['Pct_Change_Price']

california_conventional_df['Elasticity'] = california_conventional_df['Pct_Change_Units'] / california_conventional_df['Pct_Change_Price']

# Merge california_organic_df and california_conventional_df
california_df = pd.concat([california_organic_df, california_conventional_df])

# Save the merged dataframe to a new CSV file
california_df.to_csv('../dataset/california_df.csv', index=False)


# In[113]:


california_df.head()


# | **Holiday**          | **Date**                                     | **2021**                       | **2022**                       | **2023**                       | **2024**                       |
# |-----------------------|----------------------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
# | **Big Game**         | Varies (Typically first Sunday in February)  | 07/02/2021| 13/02/2022 | 12/02/2023 | 11/02/2024 |
# | **Valentine’s Day**  | February 14                                  | | | | |
# | **St. Patrick’s Day**| March 17                                    
# | **Easter**           | Varies (Between March 22 and April 25-Sunday)| 04/04/2021 | 17/04/2022 | 09/04/2023  | 31/03/2024 |
# | **Cinco de Mayo**    | May 5                                        | | | | |
# | **Memorial Day**     | Last Monday in May                           | 31/05/2021 | 30/05/2022 | 29/05/2024 | 27/05/2024 |
# | **Father’s Day**     | Third Sunday in June                         | 20/06/2021 | 19/06/2022 | 18/06/2023 | 16/06/2024 |
# | **Independence Day** | July 4                                       | | | | |
# | **Labor Day**        | First Monday in September                    | 06/09/2021 | 05/09/2022 | 04/09/2023 | 02/09/2024 |
# | **Halloween**        | October 31                                   | | | | |
# | **Thanksgiving**     | Fourth Thursday in November                  | 25/11/2021 | 24/11/2022 | 23/11/2023 | 28/11/2024 |
# | **Christmas**        | December 25                                  | | | | |
# | **New Year’s Eve**   | December 31                                  | | | | |

# In[114]:


weekly_elasticity_california_organic = california_organic_df[['Current Year Week Ending', 'Elasticity']]
weekly_elasticity_california_conventional = california_conventional_df[['Current Year Week Ending', 'Elasticity']]

weekly_elasticity_california_organic_2021 = weekly_elasticity_california_organic[weekly_elasticity_california_organic['Current Year Week Ending'].dt.year == 2021]
weekly_elasticity_california_conventional_2021 = weekly_elasticity_california_conventional[weekly_elasticity_california_conventional['Current Year Week Ending'].dt.year == 2021]

highlight_dates_2021 = ['2021-02-07', '2021-02-14', '2021-03-17', '2021-04-04', '2021-05-05', '2021-05-31', '2021-06-20', '2021-07-04', '2021-09-06', '2021-10-31', '2021-11-25', '2021-12-25', '2021-12-31']
highlight_labels_2021 = ['Big Game', 'Valentine’s Day', 'St. Patrick’s Day', 'Easter', 'Cinco de Mayo', 'Memorial Day', 'Father’s Day', 'Independence Day', 'Labor Day', 'Halloween', 'Thanksgiving', 'Christmas', 'New Year’s Eve']

plt.figure(figsize=(10, 6))
ax = weekly_elasticity_california_organic_2021.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Organic')
weekly_elasticity_california_conventional_2021.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Conventional', ax=ax)
plt.xlabel('Semana')
plt.ylabel('Elasticidad de la demanda respecto al precio')
plt.title('Elasticidad de la demanda respecto al precio por semana para aguacates en California (2021)')
plt.legend()
plt.grid(True)

# Set custom x-ticks
highlight_dates_dt = pd.to_datetime(highlight_dates_2021)
ax.set_xticks(highlight_dates_dt)
ax.set_xticklabels(highlight_labels_2021, rotation=90)

plt.show()


# In[115]:


weekly_elasticity_california_organic_2022 = weekly_elasticity_california_organic[weekly_elasticity_california_organic['Current Year Week Ending'].dt.year == 2022]
weekly_elasticity_california_conventional_2022 = weekly_elasticity_california_conventional[weekly_elasticity_california_conventional['Current Year Week Ending'].dt.year == 2022]

highlight_dates_2022 = ['2022-02-14', '2022-03-17', '2022-04-17', '2022-05-05', '2022-05-30', '2022-06-19', '2022-07-04', '2022-09-05', '2022-10-31', '2022-11-24', '2022-12-25', '2022-12-31']
highlight_labels_2022 = ['Big Game (02-13) & \nValentine’s Day (02-14)', 'St. Patrick’s Day', 'Easter', 'Cinco de Mayo', 'Memorial Day', 'Father’s Day', 'Independence Day', 'Labor Day', 'Halloween', 'Thanksgiving', 'Christmas', 'New Year’s Eve']

plt.figure(figsize=(10, 6))
ax = weekly_elasticity_california_organic_2022.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Organic')
weekly_elasticity_california_conventional_2022.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Conventional', ax=ax)
plt.xlabel('Semana')
plt.ylabel('Elasticidad de la demanda respecto al precio')
plt.title('Elasticidad de la demanda respecto al precio por semana para aguacates en California (2022)')
plt.legend()
plt.grid(True)

# Set custom x-ticks
highlight_dates_dt = pd.to_datetime(highlight_dates_2022)
ax.set_xticks(highlight_dates_dt)
ax.set_xticklabels(highlight_labels_2022, rotation=90)

plt.show()


# In[116]:


weekly_elasticity_california_organic_2023 = weekly_elasticity_california_organic[weekly_elasticity_california_organic['Current Year Week Ending'].dt.year == 2023]
weekly_elasticity_california_conventional_2023 = weekly_elasticity_california_conventional[weekly_elasticity_california_conventional['Current Year Week Ending'].dt.year == 2023]

highlight_dates_2023 = ['2023-02-14', '2023-03-17', '2023-04-09', '2023-05-05', '2023-05-29', '2023-06-18', '2023-07-04', '2023-09-04', '2023-10-31', '2023-11-23', '2023-12-25', '2023-12-31']
highlight_labels_2023 = ['Big Game (02-12) & \nValentine’s Day (02-14)', 'St. Patrick’s Day', 'Easter', 'Cinco de Mayo', 'Memorial Day', 'Father’s Day', 'Independence Day', 'Labor Day', 'Halloween', 'Thanksgiving', 'Christmas', 'New Year’s Eve']

plt.figure(figsize=(10, 6))
ax = weekly_elasticity_california_organic_2023.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Organic')
weekly_elasticity_california_conventional_2023.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Conventional', ax=ax)
plt.xlabel('Semana')
plt.ylabel('Elasticidad de la demanda respecto al precio')
plt.title('Elasticidad de la demanda respecto al precio por semana para aguacates en California (2023)')
plt.legend()
plt.grid(True)

# Set custom x-ticks
highlight_dates_dt = pd.to_datetime(highlight_dates_2023)
ax.set_xticks(highlight_dates_dt)
ax.set_xticklabels(highlight_labels_2023, rotation=90)

plt.show()


# In[117]:


weekly_elasticity_california_organic_2024 = weekly_elasticity_california_organic[weekly_elasticity_california_organic['Current Year Week Ending'].dt.year == 2024]
weekly_elasticity_california_conventional_2024 = weekly_elasticity_california_conventional[weekly_elasticity_california_conventional['Current Year Week Ending'].dt.year == 2024]

highlight_dates_2024 = ['2024-02-14', '2024-03-17', '2024-03-31', '2024-05-05', '2024-05-27', '2024-06-16', '2024-07-04', '2024-09-02', '2024-10-31', '2024-11-28', '2024-12-25', '2024-12-31']
highlight_labels_2024 = ['Big Game (02-11) & \nValentine’s Day (02-14)', 'St. Patrick’s Day', 'Easter', 'Cinco de Mayo', 'Memorial Day', 'Father’s Day', 'Independence Day', 'Labor Day', 'Halloween', 'Thanksgiving', 'Christmas', 'New Year’s Eve']

plt.figure(figsize=(10, 6))
ax = weekly_elasticity_california_organic_2024.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Organic')
weekly_elasticity_california_conventional_2024.set_index('Current Year Week Ending')['Elasticity'].plot(kind='line', marker='o', label='Conventional', ax=ax)
plt.xlabel('Semana')
plt.ylabel('Elasticidad de la demanda respecto al precio')
plt.title('Elasticidad de la demanda respecto al precio por semana para aguacates en California (2024)')
plt.legend()
plt.grid(True)

# Set custom x-ticks
highlight_dates_dt = pd.to_datetime(highlight_dates_2024)
ax.set_xticks(highlight_dates_dt)
ax.set_xticklabels(highlight_labels_2024, rotation=90)

plt.show()

