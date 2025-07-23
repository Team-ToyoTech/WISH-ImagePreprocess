from pathlib import Path
from PIL import Image, ImageOps

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

    for file in inputFolder.iterdir():
        if (
            file.is_file() and
            file.suffix.lower() in imageExtensions
        ):
            outputFile = outputFolder / file.name
            InvertImageColor(str(file), str(outputFile))

inputFolder = r'D:\Machine Learning\mnist_png\training\9'
outputFolder = r'D:\Machine Learning\mnist_png\training\9_invert'
InvertAllImagesInFolder(inputFolder, outputFolder)
