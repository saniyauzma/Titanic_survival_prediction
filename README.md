# Titanic Survival Prediction Project

This project predicts Titanic passenger survival using machine learning. It includes data cleaning, EDA, model training, and an interactive UI for predictions and filtering.

## Project Flow Diagram

```
Raw Data (train.csv, test.csv)
    ↓
Data Cleaning & Preprocessing
    ↓
Exploratory Data Analysis (EDA)
    ↓
Model Training (Logistic Regression)
    ↓
Model Evaluation & Saving
    ↓
Streamlit UI for Predictions & Filtering
```

## Prerequisites

- Python 3.8+
- Libraries: pandas, scikit-learn, streamlit, joblib

## Installation

1. Clone or download the repository.
2. Install dependencies: `pip install -r requirements.txt`

## Usage

### Run EDA and Model Training
- Open `titanic_model_training.ipynb` in Jupyter.
- Run cells for data loading, cleaning, EDA, training, and evaluation.

### Run Interactive UI
- `streamlit run streamlit_app.py`
- Filter by class, age, gender; sort results; make predictions.

## Dataset

- **Original**: `train.csv` and `test.csv` (not included; download from Kaggle).
- **Cleaned**: `cleaned_train.csv`, `cleaned_test.csv` (preprocessed versions with missing values handled).

## Files

- `titanic_model_training.ipynb`: EDA, model training, evaluation.
- `EDA_Report.md`: Detailed EDA insights and visualizations (convert to PDF for submission).
- `titanic_model.pkl`, `scaler.pkl`: Trained model and scaler.
- `streamlit_app.py`: Interactive UI.
- `cleaned_train.csv`, `cleaned_test.csv`: Processed datasets.
- `requirements.txt`: Dependencies.

## Model Details

- Algorithm: Logistic Regression
- Metrics: Accuracy ~82%, Precision/Recall/F1 included in notebook.

## GitHub Repository Setup

1. `git init`
2. `git add .`
3. `git commit -m "Initial commit"`
4. Create repo on GitHub, add remote, push.

## Video Demo

Record 5-10 min video: Intro, EDA walkthrough, model demo, Streamlit UI. Upload to YouTube/Vimeo, link here.

## GitHub Repository Setup

To create a clean, documented GitHub repo:
1. Initialize Git: `git init`
2. Add files: `git add .`
3. Commit: `git commit -m "Initial commit"`
4. Create repo on GitHub and push: `git remote add origin <url>` then `git push -u origin main`

