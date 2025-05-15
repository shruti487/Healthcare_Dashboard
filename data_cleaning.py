import pandas as pd

# Absolute paths
input_path = r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Data\raw_data.csv"
output_path = r"C:\Users\HP\OneDrive\Desktop\Data_Science_project\HealthCare_Dashboard_Project\HealthCare-Dashboard-Project\Data\cleaned_data.csv"

try:
    # Load data without header (since first row appears to be data)
    raw_data = pd.read_csv(input_path, header=None)
    
    # Assign proper column names based on your data structure
    column_names = [
        'Name',
        'Age',
        'Gender',
        'Blood_Type',
        'Medical Condition',
        'Billing Amount',
        'Medication',
        'Test_Result',

    ]
    
    raw_data.columns = column_names
    
    # Select only relevant columns (ignore empty Unnamed columns)
    relevant_cols = [col for col in column_names if not col.startswith('Unnamed')]
    raw_data = raw_data[relevant_cols]
    
    # Define key columns for cleaning
    key_columns = ['Age', 'Gender', 'Medical Condition', 'Billing Amount']
    
    # Clean data
    cleaned_data = raw_data.dropna(subset=key_columns)
    cleaned_data = cleaned_data.drop_duplicates()
    
    # Convert numeric fields
    cleaned_data['Age'] = pd.to_numeric(cleaned_data['Age'], errors='coerce')
    cleaned_data['Billing Amount'] = pd.to_numeric(cleaned_data['Billing Amount'], errors='coerce')
    
    # Filter valid ranges
    cleaned_data = cleaned_data[cleaned_data['Age'].between(0, 120)]
    cleaned_data = cleaned_data[cleaned_data['Billing Amount'] > 0]  # Remove negative costs
    
    # Save cleaned data
    cleaned_data.to_csv(output_path, index=False)
    
    print(f"Success! Cleaned {len(raw_data)} rows → {len(cleaned_data)} rows")
    print(f"Saved to: {output_path}")
    
except Exception as e:
    print(f"Error: {str(e)}")
    print("Please check:")
    print("1. The CSV file structure matches expected format")
    print("2. The file isn't corrupted")
    print("3. You have permission to access the files")