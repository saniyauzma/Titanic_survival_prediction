# Titanic Dataset EDA Report

## Overview
This report provides an exploratory data analysis (EDA) of the Titanic dataset, focusing on survival prediction. The dataset includes passenger information such as age, gender, class, and fare.

## Key Insights
- **Survival Rate**: Approximately 38% of passengers survived.
- **Gender Impact**: Females had a higher survival rate (74%) compared to males (19%).
- **Class Impact**: First-class passengers had the highest survival rate (63%), followed by second (47%) and third (24%).
- **Age Distribution**: Most passengers were between 20-40 years old. Children under 10 had higher survival rates.
- **Fare Correlation**: Higher fare correlated with higher survival, linked to class.

## Visualizations

### 1. Survival by Gender
```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()
```
**Insight**: Females were prioritized during evacuation, leading to much higher survival.

### 2. Survival by Passenger Class
```python
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.show()
```
**Insight**: First-class passengers had better access to lifeboats, explaining the trend.

### 3. Age Distribution
```python
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()
```
**Insight**: Normal distribution with missing values; younger passengers had slightly higher survival.

### 4. Survival by Age and Class
```python
sns.boxplot(x='Pclass', y='Age', hue='Survived', data=df)
plt.title('Age vs Class by Survival')
plt.show()
```
**Insight**: Younger passengers in higher classes survived more.

### 5. Correlation Heatmap
```python
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlations')
plt.show()
```
**Insight**: Fare and class negatively correlated; survival positively with fare/class, negatively with age/SibSp.

## Data Preprocessing Summary
- Handled missing values: Age filled with median, Embarked with mode.
- Encoded categoricals: Sex (0/1), Embarked (0/1/2).
- Scaled features for modeling.

## Conclusion
EDA revealed strong correlations between survival and gender/class. These insights guided feature selection for the ML model.

*To create a PDF: Open this in Jupyter/Markdown viewer and export to PDF, or use tools like Pandoc.*