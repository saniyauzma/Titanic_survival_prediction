import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load('titanic_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load dataset for filtering
df = pd.read_csv('cleaned_train.csv')

# Map Sex to strings for display
df['Sex'] = df['Sex'].map({0: 'male', 1: 'female'})

st.title("Titanic Survival Predictor")

st.sidebar.header("Filters")
pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
min_age = st.sidebar.slider("Min Age", 0, 100, 0)
max_age = st.sidebar.slider("Max Age", 0, 100, 100)
sex = st.sidebar.selectbox("Sex", ["All", "male", "female"])

# Apply filters
filtered_df = df.copy()
if pclass:
    filtered_df = filtered_df[filtered_df['Pclass'] == pclass]
filtered_df = filtered_df[(filtered_df['Age'] >= min_age) & (filtered_df['Age'] <= max_age)]
if sex != "All":
    filtered_df = filtered_df[filtered_df['Sex'] == sex]

# Sort by Age
filtered_df = filtered_df.sort_values(by='Age')

st.subheader("Filtered Passengers")
st.dataframe(filtered_df[['Pclass', 'Sex', 'Age', 'Survived']].head(10))

st.subheader("Survival Prediction")
st.write("Enter passenger details for prediction:")

pclass_pred = st.selectbox("Class", [1, 2, 3], key="pred_class")
sex_pred = st.selectbox("Sex", ["male", "female"], key="pred_sex")
age_pred = st.slider("Age", 0, 100, 25)
sibsp_pred = st.number_input("Siblings/Spouses", 0, 10, 0)
parch_pred = st.number_input("Parents/Children", 0, 10, 0)
fare_pred = st.number_input("Fare", 0.0, 500.0, 10.0)
embarked_pred = st.selectbox("Embarked", ["S", "C", "Q"])

# Preprocess input
input_data = pd.DataFrame([{
    'Pclass': pclass_pred,
    'Sex': 1 if sex_pred == 'male' else 0,
    'Age': age_pred,
    'SibSp': sibsp_pred,
    'Parch': parch_pred,
    'Fare': fare_pred,
    'Embarked': {'S': 0, 'C': 1, 'Q': 2}[embarked_pred]
}])

X_scaled = scaler.transform(input_data)
prediction = model.predict(X_scaled)[0]
prob = model.predict_proba(X_scaled)[0][1]

st.write(f"Prediction: {'Survived' if prediction == 1 else 'Perished'}")
st.write(f"Survival Probability: {prob:.2f}")