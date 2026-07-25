# 🏗️ Concrete Compressive Strength Prediction

An end-to-end machine learning regression project that predicts the compressive strength of concrete based on its mix composition and curing age.

> 🚧 Project Status: In Progress
>
> The machine learning pipeline is complete. The next step is deploying the model with a simple Streamlit application.

---

## 📌 Project Overview

Concrete compressive strength is one of the most important indicators of structural quality. Laboratory testing requires curing specimens for several days before measuring their strength, making the process time-consuming and expensive.

This project develops a regression model capable of estimating compressive strength from the concrete mix design, allowing engineers to obtain preliminary strength estimates before laboratory testing.

---

# Business Understanding

## Business Problem

Concrete producers and engineers must determine whether a concrete mix will achieve the required compressive strength.

Traditional laboratory testing requires curing concrete for days or weeks, delaying decision-making during construction.

A predictive machine learning model can provide early strength estimation based solely on the mix composition.

---

## Business Objective

Develop a regression model capable of predicting concrete compressive strength with good accuracy.

The model should:

- Reduce preliminary testing time
- Assist engineers in evaluating mix designs
- Support faster decision-making
- Demonstrate an end-to-end machine learning workflow

---

## Analytical Questions

- Which concrete ingredients most influence compressive strength?
- How strongly does curing age affect strength?
- Can engineered features improve model performance?
- Which regression algorithm performs best?
- Does regularization improve model generalization?

---

# Project Workflow

```
Dataset
    │
    ▼
Business Understanding
    │
    ▼
Data Cleaning
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
Model Evaluation
    │
    ▼
Cross Validation
    │
    ▼
Model Saving
    │
    ▼
Streamlit Deployment (Coming Soon)
```

---

# Dataset

**Source**

UCI Machine Learning Repository

**Target**

- Compressive Strength (MPa)

**Features**

- Cement
- Blast Furnace Slag
- Fly Ash
- Water
- Superplasticizer
- Coarse Aggregate
- Fine Aggregate
- Age

---

# Project Structure

```
Concrete-Strength-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_business_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_modeling.ipynb
│
├── models/
│   └── random_forest.pkl
│
├── app/
│   └── app.py              # Coming Soon
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Data Cleaning

The dataset is already clean and requires minimal preprocessing.

Performed steps:

- Checked missing values
- Checked duplicated rows
- Removed duplicate observations
- Verified data types
- Verified numerical features

---

# Exploratory Data Analysis

## Data Quality

- Dataset contains **1005 observations**
- **9 numerical features**
- No missing values
- Duplicate rows removed
- Dataset is suitable for regression

---

## Univariate Analysis

- Most variables are slightly to moderately right-skewed.
- Blast Furnace Slag and Fly Ash contain many zero values because they are optional materials.
- Cement and aggregate variables show wide ranges, indicating different concrete mix designs.
- Compressive strength spans a broad range, making it appropriate for regression modeling.

---

## Bivariate Analysis

- Cement content shows a positive relationship with compressive strength.
- Age has a strong positive relationship with strength.
- Water content tends to reduce compressive strength.
- Supplementary cementitious materials exhibit weaker or nonlinear relationships.

---

## Outliers

Several variables contain outliers.

These values are considered realistic because they represent different concrete mix designs rather than measurement errors, so they are retained.

---

# Feature Engineering

Several domain knowledge features were created.

| New Feature | Description |
|-------------|-------------|
| Water Cement Ratio | Water / Cement |
| Total Binder | Cement + Slag + Fly Ash |
| Total Binder Ratio | Total Binder / Total Materials |
| Total Aggregate | Fine Aggregate + Coarse Aggregate |
| Fine Aggregate Ratio | Fine Aggregate / Total Aggregate |
| Coarse Aggregate Ratio | Coarse Aggregate / Total Aggregate |
| Cement Ratio | Cement / Total Binder |
| SCM | Blast Furnace Slag + Fly Ash |
| SCM Percentage | SCM / Total Binder |
| Log Age | log(1 + Age) |

---

# Modeling

Regression models evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor

---

# Model Evaluation

Evaluation metrics:

- MAE
- RMSE
- R² Score

Models were compared using:

- Hold-out test set
- Cross Validation

The best-performing model was selected based on its overall performance and generalization ability.

---

# Business Insights

Key findings from this project:

- Cement content is one of the strongest contributors to compressive strength.
- Longer curing age significantly increases concrete strength.
- Excessive water generally reduces compressive strength due to a higher water-cement ratio.
- Engineered features based on civil engineering knowledge improve model performance.
- Random Forest effectively captures nonlinear relationships between concrete ingredients and compressive strength.

Potential applications include:

- Preliminary concrete mix evaluation
- Decision support for engineers
- Educational demonstrations of machine learning in civil engineering
- Faster mix optimization before laboratory testing

---

# Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

# Current Progress

- ✅ Business Understanding
- ✅ Data Cleaning
- ✅ Exploratory Data Analysis
- ✅ Feature Engineering
- ✅ Model Training
- ✅ Model Comparison
- ✅ Cross Validation
- ✅ Model Saving
- ⏳ Streamlit Deployment
- ⏳ Final Documentation

---

# Future Improvements

- Deploy using Streamlit
- Add interactive prediction interface
- Perform hyperparameter tuning
- Add feature importance visualization
- Deploy online

---

## Author

Muhammad Rafly Husen Batubara

Civil Engineering Student | Aspiring Data Scientist