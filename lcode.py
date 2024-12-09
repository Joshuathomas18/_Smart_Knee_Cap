import pandas as pd
import random

# Load the synthetic dataset
synthetic_file_path = "C:/Users/User/Downloads/synthetic_dataset_responses.xlsx"  # Replace with your actual file path
synthetic_df = pd.read_excel(synthetic_file_path)

# Modify the 'Sports Activity' column to select only one random option
synthetic_df["Sports Activity"] = synthetic_df["Sports Activity"].apply(lambda x: random.choice(x.split(";")))

# Save the modified dataset to a new file
modified_file_path = "path_to_modified_synthetic_dataset.xlsx"  # Replace with your desired output path
synthetic_df.to_excel(modified_file_path, index=False)

print(f"Modified dataset saved at: {modified_file_path}")
