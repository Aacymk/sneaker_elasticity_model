# Sneaker Price Elasticity Analysis
## Quantifying resale market dynamics across sneaker models using StockX data

## Project Overview

This project explores how resale prices for popular sneakers change with respect to size, brand, and time since release.
Using StockX sales data from Adidas and Air Jordan models, the goal was to estimate price elasticity — how sensitive resale prices are to market factors — through statistical modeling and machine learning.

Applied a structured data science pipeline to:

- Clean and normalize raw sneaker transaction data
- Engineer key predictive features
- Model and evaluate price elasticity using regression techniques
- Generate actionable business insights for resellers and analysts

## Data Cleaning

Performed in '01_clean.ipynb'

- Removed rare sizes (< 10 sales per size)
- Filtered outliers using IQR (10th–90th percentile)
- Normalized sale price formatting (converted "$200" → 200.0)
- Converted date columns to datetime
- Reduced statistical noise by up to 60%

## Feature Engineering

Performed in '02_features.ipynb'

- Added days_since_release as a measure of sneaker age
- Applied one-hot encoding for Brand and Color
- Standardized numerical variables with StandardScaler
- Split data into:
- - X_features.csv (inputs)
- - y_target.csv (log-transformed sale prices)

## Modeling

Performed in '03_model.ipynb'

Compared three linear regression methods to model log resale price:

| Model | R² | RMSE |
| :------- | :------: | -------: |
| Linear | 0.927 | 0.134 |
| Ridge | 0.927 | 0.134 |
| Lasso | 0.916 | 0.144 |

All models captured over 91% of variance, proving strong linear relationships between retail price, size, and time since release.

## Key Insights

- Smaller or rare sizes (US 4–6) often command higher resale premiums.
- Jordan models show more price stability over time than Yeezys.
- Time since release correlates negatively with resale price — indicating gradual hype decay.
- Retail price remains a strong baseline predictor of resale value.

## Future Work

- Integrate other websites resale data for cross-platform analysis
- Expand to newer/more model releases
- Incorporate nonlinear models 
- Model price elasticity explicitly using percent-change formulas

## Author

Donovan Aus
Mathematics Major & Aspiring Data Analyst
University of Maryland, College Park.

Focus: Predictive modeling, econometrics, and financial data analytics
