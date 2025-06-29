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


## 📅 Day 7 — Comparing Air Quality: Waterloo vs Birmingham
Today, I stepped into environmental data analysis using real-time air quality readings from OpenAQ.

🛠️ **What I Did:**
- Collected NO₂ data from two UK cities: Waterloo and Birmingham
- Processed and cleaned timestamped pollutant readings
- Visualized daily NO₂ trends to compare urban air quality

 🧰 **Tools Used:**
- pandas
- seaborn
- datetime parsing

📊 **Insight:**

Waterloo consistently showed higher NO₂ levels than Birmingham across the recorded days, a possible signal of traffic or industrial density.

📁 [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_7_air_quality.ipynb)

## 📅 Day 8 — Exploring Correlation Between Weather and NO₂ Levels

In this project, I investigated whether weather conditions (like temperature, humidity, and wind speed) influence NO₂ pollution levels in Birmingham, UK.

🔍 **Objectiv**
Merge hourly air quality data (NO₂) with local weather data and analyze potential correlations between weather variables and pollution levels.

🛠 **Tools & Libraries**

- pandas for data manipulation

- matplotlib & seaborn for visualization

- Visual Crossing for weather data

- OpenAQ for air quality data

📈 **Methodology**

- Filtered NO₂ values from the broader pollutant dataset

- Joined with hourly weather readings via timestamp

- Visualized correlations using a heatmap

💡 **Key Insight**

Despite expectations, there was no strong correlation found between NO₂ levels and any of the following:

- Temperature

- Humidity

- Wind Speed

This suggests that within a short time window (June 1–17), weather might not be the dominant factor influencing NO₂ pollution in this region.

**Takeaway**

Data science is not only about confirming assumptions, it’s about testing hypotheses. Even when the result is “no significant relationship,” that’s valuable insight for guiding future research.

📁 [Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_8_air_quality.ipynb)

## 📅 Day 9 — Understanding Central Tendency in Data

🔍 **What I Explored**

Today, I focused on **measures of central tendency** — the foundations of understanding any dataset:

- **Mean** (Average)
- **Median** (Middle value)
- **Mode** (Most frequent value — discussed, but not used here due to continuous data)

📌 **Why It Matters**

Choosing the right average is crucial:

🧠 *In a neighborhood where Bill Gates lives, the mean income will be misleadingly high. But the median tells a more realistic story.*

This concept applies to many real-world scenarios especially in datasets with **extreme values or outliers**, like:
- Air pollution levels
- House prices
- Salaries

📊 **Key Takeaways**

- Mean is sensitive to outliers  
- Median provides a more robust measure for skewed data  
- Mode is most helpful with categorical or discrete variables

## 📅 Day 10: Fake Job Post Detection (NLP + Classification)

Today, I explored a real-world dataset of job postings to build a machine learning model that can identify potentially fake listings.

🧠 **Objective**
Detect fraudulent job postings using natural language processing and classification techniques.

🛠️ **Tools Used**
- Python
- pandas, NumPy
- scikit-learn
- TF-IDF Vectorization
- Logistic Regression

🔍 **What I Did**
- Cleaned the dataset and focused on key text-based features (title, description, etc.)
- Applied TF-IDF to extract meaningful patterns from text
- Trained a Logistic Regression model to classify job postings

📈 **Results**
- **Accuracy**: 96%
- **Precision (fake)**: 98%
- **Recall (fake)**: 31%
- **F1-score (fake)**: 47%

⚠️ **Key Insight**
While the model performs well on accuracy, it struggles with recall for detecting fake job listings — meaning it misses many fraudulent cases. This is due to **class imbalance** (most job listings are legitimate).

🔄 **Next Steps**
- Improve recall using techniques like:
  - Resampling (SMOTE, undersampling)
  - Adjusting class weights
  - Trying different models (Random Forest, XGBoost)
- Tune hyperparameters and expand feature set

[Code](https://github.com/abir171915/100-Days-Of-Data-Science-and-Machine-Learning/blob/main/day_10_fake_jobs.ipynb)

## 📅 Day 13: PCA
In this notebook, I explored Principal Component Analysis (PCA) — a powerful tool for dimensionality reduction. My goal was to simplify a dataset with multiple 
numerical features into just two principal components to better understand the underlying structure and relationships between classes.

**Tools Used**
- Python
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

🔍 **What I Did**
- Standardized the numerical dataset
- Applied PCA to reduce the feature space from high dimensions to 2 components
- Plotted the results to visualize class distributions
- Analyzed the explained variance ratio to understand how much information is retained by the components

**Key Learnings**
- PCA helps to reduce complexity without losing much information
- It transforms correlated features into a new set of uncorrelated axes (principal components)
- Great for visualizing data and spotting patterns in high-dimensional space
- PCA is unsupervised, so it doesn’t rely on labels




