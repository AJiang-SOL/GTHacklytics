import os
import io
from google.cloud import vision
from google.cloud.vision_v1 import types

Ban_words = {"subtotal","total","change","payment","purchase","service","tip","saved",
             "balance","visa tend","saving","card","credit","cash","coupon","tax","paymentservice",
             "foodstores", "balancedue", "visa" ,"totaltax", "authcode", "savingmadeeasy" }


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "front/APIs/ServiceAccountToken.json"



client = vision.ImageAnnotatorClient()

Filename = "example2.jpeg"
Dir = "./front/Data"

def vision():
    with io.open(os.path.join(Dir, Filename), 'rb') as imageFile:
        content = imageFile.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    fullText = '\n"{}"'.format(texts[0].description)
    fullText = ''.join([i for i in fullText if not i.isdigit()]).split("\n")

    foodList = []
    for word in fullText:
        temp = word.replace(" ","")
        if temp.isalpha() and len(word)>3 and temp.lower() not in Ban_words:
            foodList.append(word)
    return foodList
