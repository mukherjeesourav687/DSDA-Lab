# Get the dimensions of the dataset
print(f"Dataset Shape: {df.shape}")
# View the first 5 rows
print(df.head())
# Statistical summary of all attributes
print(df.describe())
# Breakdown by class variable
print(df['species'].value_counts())
