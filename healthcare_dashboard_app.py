# Scripts/healthcare_dashboard_app.py

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

# Paths
cleaned_data_path = r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Data\cleaned_data.csv"
feature_img_path = r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Visualizations\images\feature_importance.png"
conf_img_path = r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Visualizations\images\confusion_matrix.png"
pbix_note = r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\PowerBI\Healthcare_Dashboard.pbix"

# -----------------------------------------
# 1. Title and Description
# -----------------------------------------
st.title("🏥 Healthcare Dashboard")
st.markdown("""
This interactive app visualizes data analysis and machine learning predictions related to medical conditions.  
Built with **Power BI**, **Python**, and **XGBoost**.
""")

# -----------------------------------------
# 2. Load Data
# -----------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(cleaned_data_path)
    return df

df = load_data()

# -----------------------------------------
# 3. Data Preview
# -----------------------------------------
st.subheader("🧾 Sample Data")
st.dataframe(df.head())

# -----------------------------------------
# 4. Medical Condition Distribution
# -----------------------------------------
st.subheader("📊 Medical Condition Distribution")

if 'Medical Condition' in df.columns:
    st.bar_chart(df['Medical Condition'].value_counts())
else:
    st.warning("The 'medical_condition' column is not found in the dataset.")

# -----------------------------------------
# 5. Model Performance (if already trained)
# -----------------------------------------
st.subheader("🤖 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Feature Importance")
    if os.path.exists(feature_img_path):
        st.image(Image.open(feature_img_path), use_column_width=True)
    else:
        st.warning("Feature importance image not found. Run `data_analysis.py` first.")

with col2:
    st.markdown("### Confusion Matrix")
    if os.path.exists(conf_img_path):
        st.image(Image.open(conf_img_path), use_column_width=True)
    else:
        st.warning("Confusion matrix image not found. Run `data_analysis.py` first.")

# -----------------------------------------
# 6. Power BI Dashboard Reference
# -----------------------------------------
st.subheader("📌 Power BI Dashboard")

st.markdown(f"""
If you're running this locally, open the Power BI dashboard manually from:  
**`{pbix_note}`**

Or upload your dashboard to [Power BI Service](https://app.powerbi.com/) and embed a public link here!
""")

# Optional: embed Power BI URL if you have it published
# st.components.v1.iframe("https://app.powerbi.com/view?r=YOUR_PUBLIC_LINK", height=600)

# -----------------------------------------
# 7. Footer
# -----------------------------------------
st.markdown("---")
st.caption("Built for the Healthcare Dashboard Project © 2025")
