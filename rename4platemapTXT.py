import os
import pandas as pd
from collections import defaultdict

def load_sample_names(csv_path):
    # Load the CSV file without headers or any superfluous data
    df = pd.read_csv(csv_path, header=None)
    # Flatten the DataFrame to a list
    return df.stack().tolist()

def generate_file_mapping(sample_names):
    sample_count = defaultdict(int)
    file_mapping = {}
    
    # Generate mapping with triplicate suffix
    for i, name in enumerate(sample_names):
        if pd.notna(name):
            sample_count[name] += 1
            new_name = f"{name}_{sample_count[name]}.txt"
            file_mapping[f"spectrum_{i}.txt"] = new_name
    return file_mapping

def rename_files(directory, file_mapping):
    files_in_directory = os.listdir(directory)
    for file in files_in_directory:
        if file in file_mapping:
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, file_mapping[file])
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")

# Path to the CSV file containing the plate map
csv_path = r"C:\Users\skl448\Desktop\phd\data\zooms\phd_data\phd_data_sjaelland\plate_map_odense_16042024.csv"
sample_names = load_sample_names(csv_path)  # Load and prepare sample names from CSV

# Directory where your files are stored
directory_path = r"C:\Users\skl448\Desktop\phd\data\zooms\phd_data\phd_data_sjaelland\second_run\.txt"
file_mapping = generate_file_mapping(sample_names)  # Generate the mapping from the sample names list

rename_files(directory_path, file_mapping)  # Rename the files in the specified directory
