import requests
import pandas as pd


Key = "api_key=D6wjedhcjFFtV4r82fBcDyGlw3xmddocXdVFrAkl"
base = 'https://api.nal.usda.gov/fdc/v1/foods/search?query='
additional = "&dataType=&pageSize=5&pageNumber=1&sortBy=dataType.keyword&sortOrder=asc&"

lookupTable = {"Protein", "Carbohydrate, by difference", "Fiber, total dietary", "Cholesterol",
               "Fatty acids, total trans", "total saturated", "Sugars, total including NLEA",
               "Total lipid (fat)","Sodium, Na","Vitamin A, IU","Calcium, Ca", "Potassium, K",
               "Vitamin D (D2 + D3), International Units", "Vitamin C, total ascorbic acid",
               "Iron, Fe", "Vitamin E" ,"Vitamin B-12"}



def FoodDataLookUp(food: str):
    dic = {}
    edit = food.replace(" ","%20")
    apiRequest = base + edit + additional + Key
    response = requests.get(apiRequest).json()
    if not response: return None
    df = pd.json_normalize(response,'foods')
    for food in df['foodNutrients']:
        if food != []:
            for nutrient in food:
                if nutrient['nutrientName'] in lookupTable:
                    dic[nutrient['nutrientName']] = nutrient['value']
            break
    print(dic)
    return dic
    

FoodDataLookUp()
    