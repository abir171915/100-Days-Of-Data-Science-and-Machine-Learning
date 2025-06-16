#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import streamlit as st


# In[3]:


gdf = gpd.read_file("data/LAD_Dec_2021_England.geojson")


# In[5]:


gdf['lon'] = gdf.geometry.centroid.x
gdf['lat'] = gdf.geometry.centroid.y


# In[11]:


file_path = "data/privaterentalmarketstatistics231220.xls"


# In[13]:


df = pd.read_excel(file_path, sheet_name="Table2.3", skiprows=6)


# In[15]:


df = df.iloc[1:357].reset_index(drop=True)


# In[17]:


df_clean = df.drop(columns=['Unnamed: 0'], errors='ignore')


# In[19]:


df_clean = df_clean.rename(columns={"Area Code1": "Area Code", "LA Code1": "LA Code"})


# In[21]:


df_clean = df_clean[df_clean["LA Code"].notna()].reset_index(drop=True)


# In[25]:


df_sorted = df_clean.sort_values("Mean", ascending=False)


# In[29]:


df_merged = df_clean.merge(gdf[['LAD21CD', 'lon', 'lat']], left_on='Area Code', right_on='LAD21CD', how='left')


# In[35]:


df_merged = df_merged.dropna(subset=['lon', 'lat']).reset_index(drop=True)


# In[41]:


from haversine import haversine


# In[42]:


london_coord = (51.51469, -0.092009)


# In[45]:


df_merged['distance_to_london_km'] = df_merged.apply(
    lambda row: haversine((row['lat'], row['lon']), london_coord), axis = 1
)


# In[49]:


X = df_merged[['Mean']]
Y = df_merged[['distance_to_london_km']]


# In[51]:


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)


# In[57]:


poly = PolynomialFeatures(degree = 3)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)


# In[59]:


model = LinearRegression()
model.fit(x_train_poly, y_train)


# In[61]:


y_pred = model.predict(x_test_poly)


# In[63]:


x_range = np.linspace(X.min(), X.max(), 300)
x_range_poly = poly.transform(x_range)

y_range_pred = model.predict(x_range_poly)

plt.figure(figsize=(10, 6))
plt.scatter(X, Y, label='Actual')

plt.plot(x_range, y_range_pred, color='red', linewidth=2, label='Polynomial Regression')

plt.xlabel("Rent (£)")
plt.ylabel("Distance from London (km)")
plt.title("Polynomial Regression: Distance from London vs. Rent")
plt.legend()
plt.tight_layout()
plt.show()


# In[65]:


y_train_pred = model.predict(x_train_poly)
y_test_pred = model.predict(x_test_poly)


# In[67]:


train_score = r2_score(y_train, y_train_pred)
test_score = r2_score(y_test, y_test_pred)


# In[73]:


df_merged['Median'] = pd.to_numeric(df_merged['Median'], errors='coerce')
df_merged['Lower quartile'] = pd.to_numeric(df_merged['Lower quartile'], errors='coerce')


# In[75]:


rent_budget = 850


# In[77]:


budget_input = np.array([[rent_budget]])
budget_input_poly = poly.transform(budget_input)
predicted_distance = model.predict(budget_input_poly)[0][0]
print(f"Predicted distance: {predicted_distance:.2f} km")


# In[79]:


tolerance = 10  # km
suggestions = df_merged[
    (df_merged['distance_to_london_km'] >= predicted_distance - tolerance) &
    (df_merged['distance_to_london_km'] <= predicted_distance + tolerance) &
    (df_merged['Mean'] <= rent_budget)
][['Area', 'Mean', 'distance_to_london_km']].sort_values(by='Mean')


# In[84]:


st.title("🏡 Can I Afford to Live Here?")
st.markdown("Enter your budget and see recommended areas near London.")


# In[86]:


budget = st.number_input("Enter your monthly rent budget (£):", value=750)
max_distance = st.slider("Maximum distance from London (km):", 0, 150, 100)


# In[90]:


filtered = df_merged[
    (df_merged["Mean"] <= budget) & 
    (df_merged["distance_to_london_km"] <= max_distance)
].sort_values("Mean")


# In[92]:


st.subheader("🔍 Recommended Areas:")
st.dataframe(filtered[["Area", "Mean", "distance_to_london_km"]])


# In[ ]:




