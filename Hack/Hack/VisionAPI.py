import os
import io
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()
print(client)

Filename = "Stop_sign_light_red.svg.png"
Dir = "Data"

with io.open(os.path.join(Dir,Filename),'rb' ) as imageFile:
    content = imageFile.read()

image = types.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations
print(texts)
