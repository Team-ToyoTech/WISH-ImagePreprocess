from pathlib import Path
from PIL import Image
import random
import numpy as np

def MakeWhiteTransparent(image):
    image = image.convert("RGBA")
    arr = np.array(image)
    mask = (arr[..., :3] == [255, 255, 255]).all(axis=-1)
    arr[mask, 3] = 0
    return Image.fromarray(arr)

def ComposeOverlayImages(
    baseImagePath, overlayFolderPath, outputFolderPath, numRandom=9
):
    scaleFactors = [1.0, 1.25, 1.5, 2.0, 2.5, 3.0]
    rotations = [0, -15, 15]
    overlayFolder = Path(overlayFolderPath)
    outputFolder = Path(outputFolderPath)
    outputFolder.mkdir(parents=True, exist_ok=True)

    baseImage = Image.open(baseImagePath).convert('RGBA')
    baseWidth, baseHeight = baseImage.size

    imageExtensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']

    overlayFiles = [f for f in overlayFolder.iterdir() if f.is_file() and f.suffix.lower() in imageExtensions]
    totalFiles = len(overlayFiles)

    cnt = 0

    for idx, overlayFile in enumerate(overlayFiles, 1):
        print(f"{idx}/{totalFiles}")

        overlayImageOrigin = Image.open(overlayFile)
        overlayImageOrigin = MakeWhiteTransparent(overlayImageOrigin)
        overlayName = overlayFile.stem
        for scale in scaleFactors:
            overlayWidth = int(overlayImageOrigin.width * scale)
            overlayHeight = int(overlayImageOrigin.height * scale)
            if overlayWidth > baseWidth or overlayHeight > baseHeight:
                continue
            overlayImageScaled = overlayImageOrigin.resize((overlayWidth, overlayHeight), Image.LANCZOS)

            for angle in rotations:
                overlayImageRotated = overlayImageScaled.rotate(angle, expand=True)
                rotatedWidth, rotatedHeight = overlayImageRotated.size
                if rotatedWidth > baseWidth or rotatedHeight > baseHeight:
                    continue

                positions = []
                centerX = (baseWidth - rotatedWidth) // 2
                centerY = (baseHeight - rotatedHeight) // 2
                positions.append( (centerX, centerY) )

                used = set()
                used.add( (centerX, centerY) )
                while len(positions) < numRandom + 1:
                    randX = random.randint(0, baseWidth - rotatedWidth)
                    randY = random.randint(0, baseHeight - rotatedHeight)
                    if (randX, randY) not in used:
                        positions.append( (randX, randY) )
                        used.add( (randX, randY) )

                for posX, posY in positions:
                    resultImage = baseImage.copy()
                    resultImage.alpha_composite(overlayImageRotated, (posX, posY))
                    resultFileName = (
                        f"{overlayName}_scale{scale:.2f}_rot{angle}_at{posX}_{posY}.png"
                    )
                    cnt += 1
                    resultFilePath = outputFolder / resultFileName
                    resultImage.save(resultFilePath)

    print(cnt)


baseImagePath = r'D:\Machine Learning\mnist_png\training\NaN\0.png'
overlayFolderPath = r'D:\Machine Learning\mnist_png\training\9_invert'
outputFolderPath = r'D:\Machine Learning\mnist_png\training\9_new'
ComposeOverlayImages(baseImagePath, overlayFolderPath, outputFolderPath)
