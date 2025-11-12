# Sneaker Price Elasticity — Insights Report
## Overview

This project explores sneaker resale market dynamics by analyzing StockX data from Adidas and Air Jordan models.
The main goal was to model how sneaker resale prices vary across sizes and time since release, and to quantify the price elasticity using regression techniques.

## Data Summary

Collected and cleaned transaction data for four popular models:

- adidas Yeezy Boost 350 V2 Core Black White
- adidas Yeezy Boost 350 V2 Zebra
- Jordan 1 Retro Chicago (2015)
- Jordan 1 Retro UNC

After cleaning, the dataset contained:

~2,000 total sales across all models

Columns: Retail price, Sale price, Sneaker size, Brand, Color, Release date, Date of sale

Outliers and rare sizes (fewer than 10 sales) were removed using an interquartile range (IQR) filter, which reduced noise by ~40–60% depending on the model.

## Feature Engineering

To prepare for modeling:

- Sale prices were log-transformed to stabilize variance
- New feature days_since_release was created to measure resale aging effects
- Brand and color were one-hot encoded
- All numerical variables were standardized using StandardScaler

Final model features included:
Retail_Price, Sneaker_Size, days_since_release, Brand_*, Color_*

## Modeling

We compared three linear regression models:

- Ordinary Least Squares (Linear)
- Ridge Regression (L2 regularization)
- Lasso Regression (L1 regularization)

## Key Insights

- Strong Predictive Power: All three regressions achieved R² > 0.91, suggesting a strong linear relationship between the chosen features and resale price.
- Retail Price Impact: Retail price is a major predictor, with resale prices typically scaling above retail for limited-release models.
- Size Premiums: Smaller and rarer sizes (US 4–6) often exhibited higher resale medians before cleaning, but much of this premium was noise-driven.
- Brand & Color Effects: Encoded features showed that Jordan models tend to maintain slightly higher resale value stability than Adidas Yeezys.
- Time Decay: The days_since_release feature had a small but negative coefficient — suggesting resale prices slowly decline after release.

## Business Application

These results can guide:
- Resellers: Optimize which sizes to stock and when to sell.
- Retailers: Estimate post-release value retention.
- Market analysts: Quantify hype decay and resale lifecycle across brands.

## Future work could involve:

- Adding cross-platform data for comparison
- Testing nonlinear models 
- Predicting elasticity directly (percentage change in price vs. retail price or supply metrics)

## Conclusion

The sneaker resale market exhibits consistent, measurable relationships between retail price, size, and time since release.
A simple linear framework can already capture 90%+ of the variation in resale value — proving that even a basic elasticity model can deliver powerful business insights.