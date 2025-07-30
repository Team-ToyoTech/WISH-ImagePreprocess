import os
from PIL import Image
from tqdm import tqdm

def rotate_images(filePath, outputPath):
    os.makedirs(outputPath, exist_ok=True)
    
    angles = [i * 0.5 for i in range(1, 11)]
    all_angles = angles + [-a for a in angles]
    
    extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
    
    for filename in tqdm(os.listdir(filePath)):
        if not filename.lower().endswith(extensions):
            continue
        img_path = os.path.join(filePath, filename)
        
        try:
            with Image.open(img_path) as img:
                for angle in all_angles:
                    rotated = img.rotate(angle, expand=True)
                    
                    name, ext = os.path.splitext(filename)
                    out_filename = f"{name}_rot{angle:+.1f}{ext}"
                    out_path = os.path.join(outputPath, out_filename)
                    
                    rotated.save(out_path)
            
            #print(f"Processed: {filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

for i in range(10):
    print(i, end = ' ')
    filePath = f"D:\\Machine Learning\\1-1to2-4\\{i}"
    outputPath = f"D:\\Machine Learning\\tmnist_data\\{i}"
    rotate_images(filePath, outputPath)

print("NaN", end = ' ')
filePath = "D:\\Machine Learning\\1-1to2-4\\NaN"
outputPath = "D:\\Machine Learning\\tmnist_data\\NaN"
rotate_images(filePath, outputPath)
