# 100-Days-Of-Data-Science-and-Machine-Learning
Day-wise hands-on learning in Data Science and ML

This repository tracks my 100-day journey through data science and machine learning projects.

## Day 1: UK Room Rent Analysis
Analyzed average room rent across UK regions (2022–2023) using pandas, matplotlib, and KNN imputation.

- [Original dataset](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/privaterentalmarketsummarystatisticsinengland)
- Tools: Python, pandas, matplotlib, sklearn
- Key Insight: London had the highest average rent (£757), North East the lowest (£416)
- [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_1_rent_analysis.ipynb)


## Follow the Journey
Each day I'll upload a new project or notebook here.

## 📅 Day 2: City of London, Why So Expensive???

Analyze 1-bedroom rental prices across local authorities in England and identify the most and least expensive areas.

### 🛠️ Tools Used
- pandas
- matplotlib
- seaborn

### 🔍 Key Highlights
- **City of London** shows an average rent of **£2,150/month**
- In contrast, most other local authorities average **£700–£800/month**
- This difference isn't an outlier statistically — it's a **true regional variation**

### 📊 Visuals
- Horizontal bar chart of top 10 most expensive areas
- Horizontal bar chart of 10 least expensive areas


🔗 [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_2_rent_analysis.ipynb)

## 📅 Day 3 — Predicting Rent Based on Distance from London
Objective:
Explore how the average rent in UK Local Authorities correlates with their geographic distance from Central London.

### 🛠️ What I Did:
- Cleaned and prepared VOA 1-bedroom rental dataset

- Merged it with LA centroid coordinates

- Computed haversine distance from Central London (lon = -0.092009, lat = 51.51469)

- Trained a 3rd-degree Polynomial Regression to predict mean rent

### 📊 Visualization:
- Scatter plot showing rent vs. distance from London

- Regression curve highlighting the non-linear relationship

### 📈 Model Performance:
- Train R² Score: 0.7588

- Test R² Score: 0.7126

🔗 [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_3_rent_analysis.ipynb)

## 📅 Day 4: Rent Affordability Analysis

In this analysis, I introduced an **Affordability Score** for rental data in England using the formula:
Affordability Score = Median Rent / Lower Quartile Rent

🔎 **Why it matters**:  
This score helps identify how affordable housing is across different areas, the lower the score, the more balanced and accessible the rental market might be.

📌 **Key Insights**:
- High scores indicate a wide rent gap, potentially tough for low-income renters.
- Low scores point to areas with more uniform pricing.

📊 Visualizations include:
- Top 10 least affordable areas
- Top 10 most affordable areas

🔗 [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_4_rent_analysis.ipynb)

## 📅 Day 5: Budget-Based Distance Prediction
🎯 Objective: Given a user's rental budget, estimate how far from Central London they would likely need to live based on historical 1-bedroom rent data.

🛠️ **What I Did**:

- Inverted the rent prediction model: instead of predicting rent, we predict distance from London using user-provided budget.

- Trained a Polynomial Regression (degree=3) model using historical VOA rental data and calculated distances via the Haversine formula.

- Used the model to predict how far (in km) a budget would take you from London.

📊 **Visualization**:

- Scatter plot of rent vs. distance with a regression curve.

- Budget-to-distance interactive input planned for app version.

📈 Model Performance:

- Train R² Score: ~0.70

- Test R² Score: ~0.77


💡 **Use Case**:
This model could help relocating individuals estimate affordable zones within commuting range of London.

🔗 [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_5_rent_analysis.ipynb)

## 📅 Day 6 — "Can I Afford to Live Near London?" 🏡
Inspired by a comment from a friend, I built a simple Streamlit app that helps users find affordable areas near London based on their rent budget.

💡 **Idea**
*"If someone wants to live close to London within a specific budget, which areas should they look at?"*

🛠️ **What the App Does**
- Takes user input for monthly rent budget 💸

- Uses a trained regression model to estimate how far from London they can live

- Filters and recommends local authorities within that distance

- Displays a simple bar chart of suggestions

🧰 Tools Used
- pandas
- matplotlib 
- scikit-learn
- geopandas
- Streamlit


🔗 [Live app](https://100-days-of-data-science-and-machine-learning-rkq8ox3xpnnrezyc.streamlit.app/)

📁 [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/can_i_afford(app).py)

