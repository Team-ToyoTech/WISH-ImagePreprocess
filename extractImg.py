import os
import shutil
import random
from tqdm import tqdm

def CopyRandomImages(srcFolder, dstFolder, percent=13):
    imgExts = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']

    files = [f for f in os.listdir(srcFolder)
             if os.path.splitext(f)[1].lower() in imgExts
             and os.path.isfile(os.path.join(srcFolder, f))]

    total = len(files)
    if total == 0:
        print("이미지 파일이 없습니다.")
        return

    count = max(1, round(total * percent / 100))

    sampled = random.sample(files, count)

    os.makedirs(dstFolder, exist_ok=True)

    for f in tqdm(sampled, desc="이미지 복사 중", ncols=70):
        srcPath = os.path.join(srcFolder, f)
        dstPath = os.path.join(dstFolder, f)
        shutil.copy2(srcPath, dstPath)

    print(f"총 {total}장 중 {count}장({percent}%)을 복사 완료")

for i in range(0, 10):
    srcFolder = f'D:\\Machine Learning\\mnist_png\\training\\{i}'
    dstFolder = f'D:\\Machine Learning\\mnist_wish\\{i}'
    CopyRandomImages(srcFolder, dstFolder)

srcFolder = r'D:\Machine Learning\mnist_png\training\NaN'
dstFolder = r'D:\Machine Learning\mnist_wish\NaN'
CopyRandomImages(srcFolder, dstFolder)
