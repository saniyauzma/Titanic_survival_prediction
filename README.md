# Titanic Survival Prediction Project

This project predicts Titanic passenger survival using machine learning. It includes data cleaning, exploratory data analysis (EDA), model training, and an interactive Streamlit UI for predictions and filtering. Optional real-time prediction via Kafka is included as code (not runnable in this environment).

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
    ↓ (Optional)
Real-Time Predictions via Kafka Consumer
```

## Prerequisites

- Python 3.8+
- Libraries: pandas, scikit-learn, streamlit, joblib, matplotlib, seaborn

## Installation

1. Clone the repository: `git clone https://github.com/saniyauzma/Titanic_survival_prediction.git`
2. Navigate to the directory: `cd Titanic_survival_prediction`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

### Run EDA and Model Training
- Open `titanic_model_training.ipynb` in Jupyter Notebook.
- Run all cells to perform data loading, cleaning, EDA, model training, and evaluation.

### Run Interactive UI
- Execute: `streamlit run streamlit_app.py`
- Features: Filter predictions by passenger class, age, gender; sort results; input custom data for survival prediction.

### Optional: Real-Time Predictions (Code Only)
- Kafka consumer code (`consumer.py`) is provided for real-time predictions.
- Docker setup (`Dockerfile`, `docker-compose.yml`) is included but not runnable due to environment limitations.
- To run locally (if Docker is available): `docker-compose up`

## Dataset

- **Original**: `train.csv` and `test.csv` (download from [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)).
- **Cleaned**: `cleaned_train.csv`, `cleaned_test.csv` (preprocessed versions with handled missing values, encoded features).
- **Featured**: featured_train.csv, featured_test.csv (Final versions with engineered features like Title, FamilySize, and IsAlone, ready for model input).

## Files

- `titanic_model_training.ipynb`: Jupyter notebook with EDA, model training, and evaluation.
- `EDA_Report.md`: Detailed EDA insights and visualizations.
- `streamlit_app.py`: Interactive Streamlit application.
- `consumer.py`: Kafka consumer for real-time predictions.
- `Dockerfile` & `docker-compose.yml`: Docker configuration for Kafka setup.
- `titanic_model.pkl` & `scaler.pkl`: Serialized trained model and data scaler.
- `cleaned_train.csv` & `cleaned_test.csv`: Processed datasets.
- `requirements.txt`: Python dependencies.

## Model Details

- **Algorithm**: Gradient Boosting
- **Performance**: Accuracy ~83% on test set, with precision, recall, and F1-score metrics.
- **Features**: Passenger class, age, gender, fare, embarked port, etc.

## GitHub Repository

- **URL**: https://github.com/saniyauzma/Titanic_survival_prediction
- Repository includes all code, datasets, and documentation.

## Video Demo

**Video Link**: https://youtu.be/UjmtuXEgXNA


## Submission Checklist

- [x] Cleaned dataset
- [x] EDA report
- [x] Trained model
- [x] Interactive UI
- [x] GitHub repository
- [x] Video demo 
- [x] Optional: Real-time system (code provided)

