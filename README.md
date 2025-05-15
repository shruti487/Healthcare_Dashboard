

# 🏥 HealthCare Dashboard Project

A Data Science project focused on building a predictive analytics dashboard using real-world healthcare data. The goal is to clean, analyze, visualize, and model the data to predict patient diagnoses, uncover feature importance, and provide actionable insights for hospitals and healthcare providers.

---

## 📌 Project Objective

To develop an end-to-end data science pipeline that:

* 🧹 Cleans and preprocesses healthcare data
* 📊 Visualizes key metrics and distributions
* 🤖 Trains a machine learning model to **predict patient diagnosis**
* 📈 Analyzes feature importance and model performance
* 📂 Integrates visualizations for decision-making support (can be extended to Power BI)

---

## 🗂️ Project Structure

```
HealthCare-Dashboard-Project/
│
├── Data/
│   └── cleaned_data.csv                # Final dataset used for training
│
├── Scripts/
│   └── data_analysis.py               # ML analysis and visualizations
│
├── Visualizations/
│   └── images/
│       ├── feature_importance.png     # Saved plot of feature importances
│       └── confusion_matrix.png       # Confusion matrix of predictions
│
├── Docs/
│   └── README.md                      # Project description & usage
│
└── requirements.txt                   # Python dependencies
```

---

## ⚙️ Implementation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/HealthCare-Dashboard-Project.git
cd HealthCare-Dashboard-Project
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Data

Ensure `cleaned_data.csv` exists in the `/Data` folder. This dataset should include columns like:

* `Age`
* `Gender`
* `Cost`
* `Diagnosis`
* Any other relevant patient or hospital info

### 5. Run Analysis

```bash
python Scripts/data_analysis.py
```

This will:

* Train a classification model (Random Forest or XGBoost)
* Evaluate accuracy, precision, recall
* Plot feature importance
* Generate and save a confusion matrix

---

## 📈 Output Examples

| Output                     | File                                            |
| -------------------------- | ----------------------------------------------- |
| 🔍 Feature Importance Plot | `/Visualizations/images/feature_importance.png` |
| ✅ Confusion Matrix         | `/Visualizations/images/confusion_matrix.png`   |
| 🧠 Model Accuracy & Report | Printed in terminal                             |

---

## 🤖 Machine Learning Model

* **Type**: Multiclass Classification
* **Models Used**: `RandomForestClassifier` (optionally XGBoost)
* **Target Variable**: `Diagnosis`
* **Metrics Evaluated**: Accuracy, Precision, Recall, F1-Score

---

## 🚀 Future Enhancements

* Integrate with **Power BI** for a dynamic dashboard
* Add **web UI using Flask or Streamlit**
* Enable **real-time patient data input**
* Improve prediction accuracy using deep learning
* Add **alert/notification system** for critical conditions

---

## 🧠 Learnings & Skills Applied

* Data Cleaning & Label Encoding
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training and Evaluation
* Data Visualization with Seaborn/Matplotlib
* Python Automation
* Imbalanced Data Handling

---

## 📚 Requirements

* Python 3.7+
* pandas, numpy, matplotlib, seaborn
* scikit-learn
* xgboost (optional)
* imbalanced-learn (for SMOTE)

