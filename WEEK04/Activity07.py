import pandas as pd

# Load the Iris dataset from the UCI Machine Learning Repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Define the column names for the dataset
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Load the dataset into a pandas DataFrame
df = pd.read_csv(url, header=None, names=columns)

# Remove any rows with missing values
df.dropna(inplace=True)

# Print the number of rows and columns in the dataset
print("Flower species in the dataset:")
print(df['species'].unique())