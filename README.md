# Sales Generation Analysis

## Overview
This project involves forecasting and analyzing sales growth. It features a machine learning workflow to generate growth data, train models, and verify predictions.

## Structure
- `data/`: Real and generated sales data.
- `docs/`: Strategy docs.
- `models/`: Trained model binaries and weights.
- `notebooks/`:
  - `sales_growth_discovery.ipynb`: EDA and sales growth patterns.
  - `ml_model_verification.ipynb`: Verifying out-of-sample predictions.
- `scripts/`:
  - `download_real_data.py`: Downloads the required sales records.
  - `generate_growth_data.py`: Creates synthetic data or growth targets.
  - `util_build_sales_master.py`: Builds a unified sales master view.
  - `train_growth_model.py`: Automates the training process of the ML models.
