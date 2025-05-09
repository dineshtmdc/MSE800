import pandas as pd

# file path
file_path = 'D:\\ASSINGMENTS\\MSE800\\Activities\\WEEK04\\FileProcessor\\Data\\Sample_data_2.parquet'

# Load the Parquet file into a DataFrame
df = pd.read_parquet(file_path)

# Count the number of features (columns)
num_features = df.shape[1]

print(f"Number of features (columns): {num_features}")