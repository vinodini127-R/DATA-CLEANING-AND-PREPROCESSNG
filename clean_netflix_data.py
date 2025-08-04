
import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Show basic info
print("Initial Data:")
print(df.info())

# Handle missing values
df = df.copy()  # safe copy to suppress warnings
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Listed')

df.dropna(subset=['date_added'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize country names
df['country'] = df['country'].str.strip().str.lower()

# Convert date to datetime
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='mixed', errors='coerce')


# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Show cleaned info
print("\nCleaned Data:")
print(df.info())

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("✅ Dataset cleaned and saved as netflix_cleaned.csv.")
