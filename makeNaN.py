from PIL import Image, ImageDraw
import os
import random
import math
from tqdm import tqdm

def DrawShortEdgeLines(image, lineCount, lineLengthRange=(5, 40), edgeMarginRatio=0.1):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    marginX = int(width * edgeMarginRatio)
    marginY = int(height * edgeMarginRatio)
    for _ in range(lineCount):
        edge = random.randint(0, 3)
        lineLength = random.randint(*lineLengthRange)
        angle = random.uniform(0, 2 * math.pi)
        color = (0, 0, 0)

        if edge == 0:
            x = random.randint(0, width-1)
            if x < marginX:
                x = random.randint(0, marginX)
            elif x > width - marginX:
                x = random.randint(width - marginX, width-1)
            y = 0
        elif edge == 1:
            x = random.randint(0, width-1)
            if x < marginX:
                x = random.randint(0, marginX)
            elif x > width - marginX:
                x = random.randint(width - marginX, width-1)
            y = height - 1
        elif edge == 2:
            x = 0
            y = random.randint(0, height-1)
            if y < marginY:
                y = random.randint(0, marginY)
            elif y > height - marginY:
                y = random.randint(height - marginY, height-1)
        elif edge == 3:
            x = width - 1
            y = random.randint(0, height-1)
            if y < marginY:
                y = random.randint(0, marginY)
            elif y > height - marginY:
                y = random.randint(height - marginY, height-1)
        x2 = int(round(x + lineLength * math.cos(angle)))
        y2 = int(round(y + lineLength * math.sin(angle)))
        x2 = max(0, min(width - 1, x2))
        y2 = max(0, min(height - 1, y2))
        draw.line((x, y, x2, y2), fill=color, width=2)

def GenerateMultiImages(baseImagePath, outputFolder, repeatCount=175000):
    os.makedirs(outputFolder, exist_ok=True)
    baseImage = Image.open(baseImagePath).convert("RGBA")
    for i in tqdm(range(1, repeatCount + 1)):
        for lineCount in [1, 2, 3]:
            newImg = baseImage.copy()
            DrawShortEdgeLines(newImg, lineCount, lineLengthRange=(5, 30), edgeMarginRatio=0.1)
            filename = f"edge_lines_{lineCount}_{i:06}.png"
            newImg.save(os.path.join(outputFolder, filename))

baseImagePath = r'D:\Machine Learning\mnist_origin\training\NaN\NaN.png'
outputFolder = r'D:\Machine Learning\mnist_2m\NaN'
GenerateMultiImages(baseImagePath, outputFolder, 189000)
