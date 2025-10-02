**💻 Laptop Price Prediction**

This project predicts laptop prices based on hardware and software specifications using machine learning pipelines. It covers the full data science workflow, from data cleaning to model deployment.

📌 Project Overview

**Goal**: Estimate laptop prices using structured features such as RAM, CPU/GPU brand, storage type, screen quality, and manufacturer.

**Audience**: Tech buyers, retailers, and data science learners seeking price benchmarking and predictive modeling.



1️⃣ Data Cleaning
- Removed duplicates and handled missing values
- Standardized inconsistent entries in `OS`, and `brand` names
- Filtered out corrupted or irrelevant records

2️⃣ Data Preprocessing
- One-Hot Encoding for categorical features: `Company`, `TypeName`, `Cpu Brand`, `Gpu Brand`, `OS`
- StandardScaler applied to numerical features: `Ram`, `Weight`, `HDD`, `SSD`, `PPI`
- Binary conversion for `Touchscreen` and `IPS` flags

### 3️⃣ Exploratory Data Analysis (EDA)
- Visualized price distributions and feature correlations
- Compared brand-wise pricing trends
- Identified key features affecting laptop prices: RAM, CPU/GPU brand, SSD/HDD, PPI, Brand

### 4️⃣ Feature Engineering
- Computed Pixels Per Inch (PPI) from screen resolution and size 
- Extracted CPU/GPU brand from full processor names
- Created binary indicators for touchscreen and IPS display

### 5️⃣ Feature Selection
- Selected features that have a strong correlation with price and reduce redundancy.
- Used domain knowledge and correlation heatmaps to choose top predictors:
- 
```python
cat_cols = ['Company', 'TypeName', 'Cpu Brand', 'Gpu Brand', 'OS']
num_cols = ['Ram', 'Weight', 'Touchscreen', 'IPS', 'PPI', 'HDD', 'SSD']
```

6️⃣ Model Building with Data Pipelines

- Built pipelines using ColumnTransformer for preprocessing and model training in a single step.
  
  Models tested:
- 1.Linear Regression
- 2.Random Forest Regressor
- 3.XGBoost Regressor
  
  Evaluated models using MSE, RMSE, and R² Score.

7️⃣ Model Deployment
- Saved the best-performing pipeline using pickle for future predictions
- Built a Streamlit web app for real-time price prediction based on user input

Tech Stack:
- Programming: Python (Pandas, NumPy, Scikit-learn, XGBoost)
- Visualization: Matplotlib, Seaborn
- Deployment: Streamlit
- Serialization: Pickle

📊 Key Takeaways
- RAM, CPU/GPU, storage type, and display quality are major drivers of laptop prices
- Pipeline-based workflows make preprocessing, training, and predictions
- The deployed app enables real-world usage for estimating laptop prices effectively

🚀 Future Enhancements
- Integrate web scraping for real-time price updates
- Add SHAP or LIME for model interpretability
- Extend app to include tablet and desktop price prediction
- Deploy via cloud platforms (e.g., Heroku, Azure)



