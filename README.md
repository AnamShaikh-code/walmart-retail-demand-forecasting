# Walmart Retail Demand Forecasting

A machine learning project for predicting Walmart weekly retail sales using historical store and department information.

## Project Overview

This project develops a machine learning model to predict weekly sales for Walmart stores.

The project includes:

- Data preparation and exploratory analysis
- Time-based train-validation split
- Comparison of multiple regression models
- Random Forest model development
- Final model training
- Test-set prediction
- Streamlit-based prediction application

## Models Compared

The following regression models were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

Random Forest produced the strongest validation results among the tested models.

## Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | $14,157.10 | $21,094.53 | 0.0906 |
| Decision Tree | $2,979.08 | $6,706.32 | 0.9081 |
| Random Forest | $2,628.64 | $5,390.73 | 0.9406 |

The Random Forest model achieved an R² of **0.9406**, explaining approximately 94.06% of the variation in the validation data.

## Final Random Forest Model

The final model uses:

- `n_estimators = 50`
- `max_depth = 15`
- `min_samples_leaf = 5`
- `random_state = 42`
- `n_jobs = -1`

## Streamlit Application

The project includes a Streamlit application that allows users to enter selected store information and receive a predicted weekly sales value.

### User Inputs

- Store
- Department
- Week
- Store Size
- Store Type
- Holiday status

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- VS Code

## Project Structure
walmart-retail-demand-forecasting/
│
├── app.py
├── final_rf_model.pkl
├── 07_Model_Comparison.ipynb
├── 08_Final_Model_Test_Prediction.ipynb
└── README.md
