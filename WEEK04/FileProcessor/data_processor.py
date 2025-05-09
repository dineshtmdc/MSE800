import pandas as pd
import math 


class DataProcessor:
    
    def __init__(self, file_path):

        self.file_path = file_path
        self.data = None

    def load_data(self):

        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith('.txt'):         
            self.data = pd.read_csv(self.file_path, header=None, names=["Line"])
        else:
            raise ValueError("Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())

    # calculate sin and cos to given value
    def calculate_sin_and_cos(value):
        print( f'sin value of {value}  : {math.sin(value)}')
        print( f'cos value of {value}: {math.cos(value)}')
    
    # calculate area of circle with given radius
    def calculate_daimiter_circle(radius):
        print( f'the area of circle with radius{radius} is {math.pi * radius**2}')
     
        
        

