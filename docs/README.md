# Sales Generation & Growth Analysis
### Scaling Revenue Intelligence to 150,000 Transactions

**Project Theme:** *"Growth is a choice made in the data."*

This repository is a **High-Scale Sales Strategy Hub**. It uses a vast, multi-table dataset to perform a "Growth Engine" analysis—identifying revenue levers, marketing ROI, and **Predictive Profitability** using Deep Learning.

---

## 🏗️ Project Architecture
Designed for scalability and strategic depth:

```text
Sales_Generation_Analysis/
├── models/
│   └── sales_predictor_v1.h5  <-- The Trained Neural Network (ML Asset)
├── data/
│   └── sales_growth_master.csv     <-- Unified Master Discovery File (150k rows).
├── notebooks/
│   ├── sales_growth_discovery.ipynb <-- ROI & Portfolio Matrix
│   └── ml_model_verification.ipynb  <-- ML Testing & Prediction Results
└── scripts/
    ├── generate_growth_data.py      <-- The 150,000 Row Simulator.
    ├── util_build_sales_master.py   <-- The Unified Builder.
    └── train_growth_model.py        <-- Keras Neural Network Trainer.
```

---

## 🔍 The Growth Strategy
We move beyond basic revenue counting to solve the **"Scale Problem"**:

### 1. Marketing ROI Radar (The "Ad Spend" Efficiency)
Analyzing 5 distinct marketing channels (Instagram, Google, Referral, Affiliate, Email) to identify the highest "Net Profit" generators.

### 2. Product Portfolio Matrix (Stars vs. Dogs)
Using the 150,000 transactions to map category volume against profit margin. This identifies which items are "Cash Cows" and which are "Loss Leaders."

### 3. Predictive Profitability (Deep Learning)
We’ve trained a **TensorFlow/Keras** Neural Network (saved as `sales_predictor_v1.h5`) to estimate the **Net Profit** of any transaction based on operational inputs. This allows for real-time order flagging and profit forecasting.

## 🛠️ Performance Tech
- **High-Performance Simulation**: [`generate_growth_data.py`](file:///e:/Data%20Analysis%20Project/Sales_Generation_Analysis/scripts/generate_growth_data.py) uses **Vectorized NumPy** logic to generate 150,000 records with ROI metrics in seconds.
- **Deep Learning Export**: Includes a full ML training pipeline and a serialized `.h5` model for external deployment.

---
*Vibing with growth. Build the engine.*
