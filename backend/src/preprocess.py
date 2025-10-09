import os
import shutil
import random
import glob

"""
This script prepares the raw image data for the multi-class flower classification task.
It takes all subdirectories from the raw data folder, splits the images into
a training and a testing set, and copies them into a processed data structure.
"""

# --- 1. Define Paths ---
# Use __file__ to be independent of where the script is run from
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(project_root, 'data', 'raw')
PROCESSED_DATA_DIR = os.path.join(project_root, 'data', 'processed')

# --- 2. Clean Up and Prepare Directories ---
print(f"Cleaning up old directory: {PROCESSED_DATA_DIR}")
if os.path.exists(PROCESSED_DATA_DIR):
    shutil.rmtree(PROCESSED_DATA_DIR)

print("Creating new directory structure...")
train_dir = os.path.join(PROCESSED_DATA_DIR, 'train')
test_dir = os.path.join(PROCESSED_DATA_DIR, 'test')
os.makedirs(train_dir)
os.makedirs(test_dir)


# --- 3. Discover Classes and Copy Data ---
# Dynamically find all subdirectories in the raw data folder (e.g., 'roses', 'tulips')
class_names = [d for d in os.listdir(RAW_DATA_DIR) if os.path.isdir(os.path.join(RAW_DATA_DIR, d))]
print(f"Found {len(class_names)} classes: {class_names}")

split_ratio = 0.8  # 80% for training, 20% for testing

for class_name in class_names:
    print(f"\n--- Processing class: {class_name} ---")
    
    # Create class subdirectories in train and test folders
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Get all image files for the current class
    source_dir = os.path.join(RAW_DATA_DIR, class_name)
    all_files = glob.glob(os.path.join(source_dir, '*.jpg')) # Use glob to get all .jpg files
    
    # Shuffle and split the files
    random.shuffle(all_files)
    split_point = int(len(all_files) * split_ratio)
    train_files = all_files[:split_point]
    test_files = all_files[split_point:]

    # Copy files
    print(f"Copying {len(train_files)} training images...")
    for file_path in train_files:
        shutil.copy(file_path, os.path.join(train_dir, class_name))
        
    print(f"Copying {len(test_files)} testing images...")
    for file_path in test_files:
        shutil.copy(file_path, os.path.join(test_dir, class_name))

print("\nData preprocessing complete!")
