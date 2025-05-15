# Imports
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier

sns.set_style("whitegrid")
print("XGBoost is installed and working!")

# Load Data
data_path = r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Data\cleaned_data.csv"
df = pd.read_csv(data_path)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df['name'] = df['name'].str.title()
df['gender'] = df['gender'].str.title()
df = df.dropna()

# Encode Target
le_target = LabelEncoder()
df['medical_condition_encoded'] = le_target.fit_transform(df['medical_condition'])

# 🔥 One-Hot Encoding of Categorical Features
cat_features = ['gender', 'blood_type', 'medication', 'test_result']
df_encoded = pd.get_dummies(df, columns=cat_features, drop_first=True)

# Features and Target
features = [col for col in df_encoded.columns if col not in ['name', 'medical_condition', 'medical_condition_encoded']]
X = df_encoded[features]
y = df_encoded['medical_condition_encoded']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# 🔥 Remove deprecated param and use better params
model = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1, eval_metric='mlogloss', random_state=42)
model.fit(X_train, y_train)

# Cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=cv)
print(f"\nAverage CV Accuracy: {np.mean(cv_scores):.2%}")

# Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2%}\n")

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=le_target.classes_))

# 🔥 Feature Importance (updated for seaborn warning)
feature_imp = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_imp.values, y=feature_imp.index, hue=feature_imp.index, palette="viridis", legend=False)
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.tight_layout()
plt.savefig(r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Visualizations\images\feature_importance.png")
plt.close()

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le_target.classes_,
            yticklabels=le_target.classes_)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig(r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Visualizations\images\confusion_matrix.png")
plt.close()

print("✅ All results saved to Visualizations folder!")
