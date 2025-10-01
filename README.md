💻 Laptop Price Prediction

This project predicts laptop prices based on hardware and software specifications using machine learning pipelines. It covers the full data science workflow, from data cleaning to model deployment.

📌 Project Overview
The goal is to help users, retailers, and tech enthusiasts estimate the market value of laptops based on features like RAM, CPU, GPU, storage, screen type, and brand.


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
- Computed Pixels Per Inch (PPI) from screen resolution and size for representation
- Extracted CPU/GPU brand from full processor names
- Created binary indicators for touchscreen and IPS display

### 5️⃣ Feature Selection
- Selected features that have a strong correlation with price and reduce redundancy.
- Used domain knowledge and correlation heatmaps to choose top predictors:
'''python
cat_cols = ['Company', 'TypeName', 'Cpu Brand', 'Gpu Brand', 'OS']
num_cols = ['Ram', 'Weight', 'Touchscreen', 'IPS', 'PPI', 'HDD', 'SSD']
'''
