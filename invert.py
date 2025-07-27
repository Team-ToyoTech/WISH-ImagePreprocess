from pathlib import Path
from PIL import Image, ImageOps
from tqdm import tqdm

def InvertImageColor(inputFilePath, outputFilePath):
    image = Image.open(inputFilePath)

    if image.mode == 'RGBA':
        r, g, b, a = image.split()
        rgbImage = Image.merge('RGB', (r, g, b))
        invertedRgb = ImageOps.invert(rgbImage)
        r2, g2, b2 = invertedRgb.split()
        resultImage = Image.merge('RGBA', (r2, g2, b2, a))
    elif image.mode == 'RGB':
        resultImage = ImageOps.invert(image)
    else:
        rgbImage = image.convert('RGB')
        resultImage = ImageOps.invert(rgbImage)

    resultImage.save(outputFilePath)

def InvertAllImagesInFolder(inputFolderPath, outputFolderPath):
    inputFolder = Path(inputFolderPath)
    outputFolder = Path(outputFolderPath)
    outputFolder.mkdir(parents=True, exist_ok=True)

    imageExtensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']

    for file in tqdm(inputFolder.iterdir(), desc="image invert", ncols=70):
        if (
            file.is_file() and
            file.suffix.lower() in imageExtensions
        ):
            outputFile = outputFolder / file.name
            InvertImageColor(str(file), str(outputFile))

for i in range(10):
    inputFolder = f"D:\\Machine Learning\\mnist_origin\\training\\{i}"
    outputFolder = f"D:\\Machine Learning\\mnist_invert\\{i}"
    InvertAllImagesInFolder(inputFolder, outputFolder)

inputFolder = "D:\\Machine Learning\\mnist_origin\\training\\NaN"
outputFolder = "D:\\Machine Learning\\mnist_invert\\NaN"
InvertAllImagesInFolder(inputFolder, outputFolder)