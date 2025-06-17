import pandas as pd
import numpy as np
import os


print("Current working directory:", os.getcwd())
try:
	df = pd.read_csv(r'F:\Universty\4th Semester\Intro to Ds\Gold Price Archive 2010-2023 Dataset.csv')
except FileNotFoundError:
	print("Error: The file '.csv' was not found. Please check the file path and ensure the file exists in the directory above.")
	exit()


print("Initial Data Info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing values before Feature Engineering:")
print(df.isnull().sum())