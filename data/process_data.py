import pandas as pd
import os

# Set the folder path
data_folder = 'data'

# List of CSV files
files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

# Empty list to collect dataframes
dfs = []

# Read and process each file
for file in files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)

    # Filter only Pink Morsels
    df = df[df['product'] == 'pink morsel']

    # Calculate sales
    df['sales'] = df['quantity'] * df['price']

    # Keep only the required columns
    df = df[['sales', 'date', 'region']]

    dfs.append(df)

# Combine all into one
final_df = pd.concat(dfs)

# Save to a new CSV file
final_df.to_csv('formatted_sales_data.csv', index=False)

print("✅ Data cleaned and saved to formatted_sales_data.csv")

