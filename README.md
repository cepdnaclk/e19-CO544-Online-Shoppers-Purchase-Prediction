## Predicting Online Shoppers' Purchasing Prediction Using Machine Learning
https://shoppers-purchasing-prediction.df.r.appspot.com

## Project Description
This project leverages data analytics and machine learning techniques to predict the purchasing intentions of online shoppers. By analyzing factors such as browsing history, demographics, past purchase behavior, and interaction data, the project aims to forecast whether a user visiting an e-commerce website or app is likely to make a purchase.

## Table of Contents
- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Oversampling](#oversampling)
- [Model Building](#model-building)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Work](#future-work)

## Introduction
The rapid growth of e-commerce has led to an increased focus on understanding consumer behavior to enhance user experience and boost sales. Predicting whether a visitor will make a purchase is crucial for tailoring marketing efforts and personalizing recommendations. This project addresses the need for accurate and reliable methods to forecast purchasing intentions, enabling businesses to optimize their strategies and increase revenue.

## Data Collection
Data was aggregated from various sources on the internet, including web logs, user profiles, and transaction records. The dataset includes user browsing history, demographic information, past purchase behavior, session duration, and interaction data.

## Data Preprocessing
The dataset was preprocessed to ensure quality and consistency:
- Data was cleaned and normalized.
- Categorical features were encoded.
- No missing values were present in the dataset.

## Oversampling
To address class imbalance issues, oversampling techniques were applied to balance the dataset.

## Model Building
Several classification models were trained, including:
- Logistic Regression
- Decision Trees
- Random Forests
- Gradient Boosting

## Model Evaluation
Models were evaluated using metrics such as:
- Accuracy
- Precision
- Recall
- F1 Score

## Results
- Logistic Regression: 75% accuracy, 72% precision, 68% recall
- Random Forest: 82% accuracy, 80% precision, 78% recall
- Gradient Boosting: 85% accuracy, 83% precision, 81% recall
- Gradient Boosting model achieved the best AUC-ROC score of 0.87

## Conclusion
The project demonstrated that machine learning models can effectively predict online shoppers' purchasing intentions. The Gradient Boosting model showed the highest accuracy and reliability. These predictions can enhance personalized marketing, improve user experience, and increase conversion rates.

## Future Work
- Explore deep learning techniques
- Incorporate additional features like real-time clickstream data
- Implement real-time prediction capabilities
