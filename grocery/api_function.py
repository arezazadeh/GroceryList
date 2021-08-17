import requests


def food_search(food, cuisine):
    url = "https://api.edamam.com/api/recipes/v2?type=public&app_id=925f7b82&app_key=36e76867b08c6842fb530f8c1c851693"

    querystring = {"cuisineType": cuisine or None, "q": food, "imageSize": "REGULAR"}
    
    response = requests.request("GET", url, params=querystring).json()
    
    res = response["hits"]
    return res
    
    # for food in res:
    #     recipe = food["recipe"]
    #     image = recipe["image"]
    #     ing = recipe["ingredientLines"]
    #     if "cuisineType" in recipe:
    #         cuisineType = recipe["cuisineType"]
    #     else:
    #         cuisineType = "Not Specified"
    #     # print(cuisineType, recipe["label"], recipe["url"], image)
    #     recipe_id = recipe["uri"].split("#")[1]
