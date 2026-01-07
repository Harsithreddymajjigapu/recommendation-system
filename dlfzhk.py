import kagglehub
from kagglehub import KaggleDatasetAdapter
file_path =  r"C:\Users\majji\.cache\kagglehub\datasets"
print("Downloading data...")
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "brijbhushannanda1979/bigmart-sales-data",
  "Train.csv",
)
print("First 5 records:", df.head())
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")