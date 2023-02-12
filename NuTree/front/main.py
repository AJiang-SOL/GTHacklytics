from APIs import FoodAPI, VisionAPI
from DB import Database
import os
from sqlalchemy import text


def main():
    pool = Database.pool()
    foodList=VisionAPI.vision()
    for food in foodList:
        nut=FoodAPI.FoodDataLookUp(food)
        string = "INSERT INTO table_nameVALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16});".format(nut.get("Protein"),
                                                                                                            nut.get("Carbohydrate, by difference"),
                                                                                                            nut.get("Fiber, total dietary"),
                                                                                                            nut.get("Cholesterol"),
                                                                                                            nut.get("Fatty acids, total trans"),
                                                                                                            nut.get("total saturated"),
                                                                                                            nut.get("Sugars, total including NLEA"),
                                                                                                            nut.get("Total lipid (fat)"),
                                                                                                            nut.get("Sodium, Na"),
                                                                                                            nut.get("Vitamin A, IU"),
                                                                                                            nut.get("Calcium, Ca"),
                                                                                                            nut.get("Potassium, K"),
                                                                                                            nut.get("Vitamin D (D2 + D3), International Units"),
                                                                                                            nut.get("Vitamin C, total ascorbic acid"),
                                                                                                            nut.get("Iron, Fe"),
                                                                                                            nut.get("Vitamin E"),
                                                                                                            nut.get("Vitamin B-12"))
        t= text(string)
        pool.execute(t)
        
        
    
    

main()
    
    
    
