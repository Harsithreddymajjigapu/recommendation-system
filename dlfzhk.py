# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path =  r"C:\Users\majji\.cache\kagglehub\datasets"

# Load the latest version
print("Downloading data...")
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "brijbhushannanda1979/bigmart-sales-data",
  "Train.csv",
)

print("First 5 records:", df.head())


# 4. Save the dataframe to your specific folder
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")