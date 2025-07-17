import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)
print(df['Name'])  # Access column using dictionary-style indexing
print(df.Age)      # Access column using dot notation