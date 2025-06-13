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

