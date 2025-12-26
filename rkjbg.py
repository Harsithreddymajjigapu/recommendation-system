import os

# Get the path to the home directory
home = os.path.expanduser("~")
kaggle_path = os.path.join(home, ".cache", "kagglehub", "datasets")

print(f"Your datasets are here: {kaggle_path}")

# Optional: List what is inside
if os.path.exists(kaggle_path):
    print("Files found:", os.listdir(kaggle_path))
else:
    print("Folder does not exist yet.")