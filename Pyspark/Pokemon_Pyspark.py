import kagglehub
import pyspark

# Download latest version
path = kagglehub.dataset_download("navtiw/pokemon")

print("Path to dataset files:", path)

