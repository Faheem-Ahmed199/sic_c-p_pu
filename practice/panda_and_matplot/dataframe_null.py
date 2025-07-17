
# Checking for missing values in a DataFrame

# Explanation: Using isnull() to check for missing values and count occurrences
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
print(df)
print(df.isnull())  # Identifies missing values
print(df.isnull().sum())  # Counts missing values per column