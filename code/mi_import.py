#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy import interpolate
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.linear_model import ElasticNetCV


# In[2]:


# Load the avocado dataset
#file_path = '../dataset/Avocado_HassAvocadoBoard_20152023v1.0.1.csv'

file_path = ['../dataset/2021-plu-total-hab-data.csv',
              '../dataset/2022-plu-total-hab-data.csv',
              '../dataset/2023-plu-total-hab-data.csv',
              '../dataset/2024-plu-total-hab-data.csv']

merged_df = pd.concat([pd.read_csv(file) for file in file_path])

merged_df.to_csv('../dataset/merged_df.csv', index=False)

#avocado_df = pd.read_csv(file_path)


# In[3]:


print(merged_df.info())


# In[4]:


merged_df.describe()


# In[5]:


merged_df.count()


# In[6]:


unique_values = merged_df.nunique()
unique_values


# In[7]:


print(merged_df['Geography'].unique())


# In[8]:


merged_df.head()


# In[9]:


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


# In[10]:


filtered_df_greaterregions = merged_df[merged_df['Geography'].isin(greaterregions)]

filtered_df_greaterregions.head()


# In[11]:


file_paths = ['../dataset/Volume Hass Avocado Board Suppliers 2022.csv',
              '../dataset/Volume Hass Avocado Board Suppliers 2023.csv',
              '../dataset/Volume Hass Avocado Board Suppliers 2024.csv',
              '../dataset/Volume Hass Avocado Board Suppliers 2025 (projection).csv']

suppliers_df = pd.concat([pd.read_csv(file) for file in file_paths])

suppliers_df.to_csv('../dataset/merged_suppliers.csv', index=False)

print(suppliers_df.info())


# In[14]:


suppliers_df.head()


# In[12]:


# Agrupar por trimestres usando Grouper
merged_df['Current Year Week Ending'] = pd.to_datetime(merged_df['Current Year Week Ending'], errors='coerce')

# Agrupar por trimestres con Grouper
grouped = merged_df.groupby(pd.Grouper(key='Current Year Week Ending', freq='Q'))

# Mostrar los grupos
for period, group in grouped:
    print(f"Trimestre que termina en {period}:")
    print(group)


# In[13]:


# Filtrar los datos de Q4 de 2022 (octubre-diciembre) y Q4 de 2023
q4_2022 = merged_df[(merged_df['Current Year Week Ending'] >= '2022-10-01') & (merged_df['Current Year Week Ending'] <= '2022-12-31')]
q4_2023 = merged_df[(merged_df['Current Year Week Ending'] >= '2023-10-01') & (merged_df['Current Year Week Ending'] <= '2023-12-31')]

# Concatenar los dos trimestres para obtener el conjunto de datos
q4_data = pd.concat([q4_2022, q4_2023])

# Calcular la media de las columnas relevantes solo de Q4 de 2022 y Q4 de 2023
mean_values_q4 = q4_data.mean(numeric_only=True)

# Filtrar los datos del Q4 de 2024 donde hay valores faltantes
q4_2024_missing = merged_df[
    (merged_df['Current Year Week Ending'] >= '2024-10-01') & 
    (merged_df['Current Year Week Ending'] <= '2024-12-31') &
    merged_df.isnull().any(axis=1)
]

# Rellenar los valores faltantes de los datos de Q4 2024 con la media calculada
merged_df.loc[q4_2024_missing.index] = merged_df.loc[q4_2024_missing.index].fillna(mean_values_q4)

# Verificar si los valores faltantes han sido rellenados
missing_data_after = merged_df[
    (merged_df['Current Year Week Ending'] >= '2024-10-01') & 
    (merged_df['Current Year Week Ending'] <= '2024-12-31') &
    merged_df.isnull().any(axis=1)
]

print(f"Datos faltantes después del relleno:\n{missing_data_after}")

