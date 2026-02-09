# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

- **Purpose:** educational repository at High School level to teach Machine Learning in Python.
- **Level:** Introductory
- **Requisites:** High school mathematics and statistics, some knowledge in coding, even Scratch language is allowed.
- **Target:** 15 year-old student that want to apply to very good colleges (like Stanford, Caltech or similar) for Computer Science
- **Example:** Used car prices forecasting

## Environment Setup

**Python Version:** 3.13.12

**Virtual Environment:**
```bash
# Activate the virtual environment
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac

# Install dependencies (if requirements.txt exists)
pip install pandas scikit-learn matplotlib jupyter ipykernel
```

**Running Jupyter Notebooks:**
```bash
# Start Jupyter from the project root
jupyter notebook

# Or run specific notebook
jupyter notebook notebooks/n1_python_for_scratchers.ipynb
```

## Project Structure

```
ML-for-used-car-prices/
├── data/                      # Training datasets (CSV/ZIP files)
│   ├── usedcarprices_sujayr_train.csv
│   └── ussalescars_juanmerino_train.zip
├── models/                    # Saved trained models (currently empty)
├── notebooks/                 # Educational Jupyter notebooks (numbered sequence)
│   ├── n1_python_for_scratchers.ipynb
│   ├── n2_data_transformation.ipynb
│   ├── n3_price_engine.ipynb
│   ├── n4_price_engine (our_data).ipynb
│   └── some_utilities.py     # Custom utility functions
├── catch-up/                  # Structured catch-up program (Sessions 1-4 notebooks + curriculum plan)
│   ├── catch-up.md            # Full 17-session curriculum plan
│   ├── session1-hello-python.ipynb
│   ├── session2-lists-and-loops.ipynb
│   ├── session3-dictionaries-and-functions.ipynb
│   └── session4-libraries-and-pandas.ipynb
└── .venv/                     # Python virtual environment
```

## Learning Progression

### Catch-Up Program (`catch-up/`)

A structured 17-session program (see `catch-up/catch-up.md`) designed to bring a Scratch-only programmer up to ML proficiency. Sessions 1-4 have dedicated notebooks; sessions 5+ reference the main `notebooks/` folder. Each session notebook has guided code sections followed by car-themed challenges for the student to complete.

### Main Notebooks (`notebooks/`)

The notebooks follow a deliberate educational sequence:

1. **n1_python_for_scratchers.ipynb**: Introduces Python basics (variables, lists, imports) to Scratch users
2. **n2_data_transformation.ipynb**: Covers data preprocessing with pandas, focusing on one-hot encoding
3. **n3_price_engine.ipynb**: Demonstrates basic ML workflow with LinearRegression on simple dataset
4. **n4_price_engine (our_data).ipynb**: Works with real-world used car datasets (in progress)

## Key Architecture Patterns

### One-Hot Encoding

The project includes a custom implementation of one-hot encoding in [some_utilities.py](notebooks/some_utilities.py) to teach the concept. The `get_dummies()` function demonstrates how pandas' `pd.get_dummies()` works under the hood.

**Usage:**
```python
from some_utilities import get_dummies

# Custom implementation (for learning)
encoded = get_dummies(car_brands, 'brand')

# Pandas implementation (for production)
df_encoded = pd.get_dummies(df, columns=['brand'])
```

### ML Workflow Pattern

The notebooks follow this standard workflow:

1. **Load data** with pandas
2. **Encode categorical features** (brand, status, model) using one-hot encoding
3. **Split data** into train/test sets using `train_test_split()`
4. **Train model** with LinearRegression (or other sklearn models)
5. **Evaluate** using `mean_absolute_error`
6. **Predict** on custom input

### Data Preprocessing Considerations (n4 notebook)

When working with the real dataset (`ussalescars_juanmerino_train.zip`):

- **Missing values**: Present in Mileage, Dealer, and Price columns
- **Categorical features**:
  - `Brand` (62 unique) - use one-hot encoding
  - `Status` (3 unique) - use one-hot encoding
  - `Model` (642 unique) - too many for one-hot, requires alternative approach
  - `Dealer` (11,475 unique) - likely not useful as feature
- **Outliers**: Price ranges from $1 to $8M - need filtering/review
- **Year range**: 1959-2024 - check distribution for old cars

## Common Development Tasks

**Working with notebooks:**
```python
# Read CSV data
data = pd.read_csv("../data/usedcarprices_sujayr_train.csv")

# Read ZIP compressed data
data = pd.read_csv("../data/ussalescars_juanmerino_train.zip")

# Standard imports used across notebooks
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
```

**Feature Engineering Pattern:**
```python
# Separate features (X) and target (y)
X = df_encoded.drop('price', axis=1)  # Features
y = df_encoded['price']                # Target

# Split data (80/20 common split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

## Educational Context

This is a **teaching project** designed for beginners. Code should:

- Include clear comments explaining what each step does
- Use descriptive variable names
- Prioritize readability over optimization
- Include print statements to show progress and results
- Demonstrate concepts explicitly rather than using advanced shortcuts.
