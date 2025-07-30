import os
import random
from tqdm import tqdm

def rename_files_to_random_numbers(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    used_numbers = set()
    for filename in tqdm(files):
        ext = os.path.splitext(filename)[1]
        while True:
            rand_num = random.randint(100000, 999999)
            new_name = f"{rand_num}{ext}"
            if new_name not in used_numbers and not os.path.exists(os.path.join(folder_path, new_name)):
                used_numbers.add(new_name)
                break
        os.rename(
            os.path.join(folder_path, filename),
            os.path.join(folder_path, new_name)
        )
        #print(f"{filename} -> {new_name}")

for i in range(10):
    filePath = f"D:\\Machine Learning\\3-0to6-2\\{i}"
    rename_files_to_random_numbers(filePath)

filePath = "D:\\Machine Learning\\3-0to6-2\\NaN"
rename_files_to_random_numbers(filePath)