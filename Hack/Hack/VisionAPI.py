import os
import io
from google.cloud import vision
from google.cloud.vision_v1 import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()

Filename = "receipt_example_2.svg.png"
Dir = "Data"

with io.open(os.path.join(Dir, Filename), 'rb') as imageFile:
    content = imageFile.read()

image = types.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations

# for text in texts:
    # if text.description.isalpha(): 
fullText = '\n"{}"'.format(texts[0].description).split("\n")
foodList = []

for word in fullText:
    temp = word.replace(" ","")
    if temp.isalpha() and len(word)>2:
        foodList.append(word)

print(foodList)
