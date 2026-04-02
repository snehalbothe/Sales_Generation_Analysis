import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import os

# NOTE: This script assumes tensorflow and h5py are installed.
# If not, it will fail on the final export step.
try:
    import tensorflow as tf
    from tensorflow.keras import layers, models
    HAS_TF = True
except ImportError:
    HAS_TF = False
    print("Warning: TensorFlow not found. Building pre-processing pipeline anyway.")

# 1. Load Data
df = pd.read_csv("../data/sales_growth_master.csv")
print(f"Loaded {len(df)} records for training...")

# 2. Define Features & Target
# Using operational and behavioral columns
df['Order_Month'] = pd.to_datetime(df['Order_Date']).dt.month
num_features = ["Quantity", "Discount_Pct", "Base_Cost", "Unit_Price", "Order_Month"]
cat_features = ["Category", "Ad_Source", "Segment"]
target = "Net_Profit"

X = df[num_features + cat_features]
y = df[target]

# 3. Preprocessing Pipeline
# Creating a transformer for both numeric (scaling) and categorical (one-hot) features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ])

X_processed = preprocessor.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

# 4. Deep Learning Model (Keras)
if HAS_TF:
    print("Initializing Neural Network...")
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dropout(0.2),
        layers.Dense(32, activation='relu'),
        layers.Dense(1) # Linear output for Net_Profit regression
    ])

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    print("Training started (10 Epochs)...")
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1, verbose=1)

    # 5. Export to .h5 format
    if not os.path.exists("../models"):
        os.makedirs("../models")
        
    model_path = "../models/sales_predictor_v1.h5"
    model.save(model_path)
    print(f"Model exported successfully to '{model_path}'")
else:
    print("Skip training: TensorFlow is not available in the current environment yet.")
    print("Please install via 'pip install tensorflow h5py' first.")
