import requests
import json


app_id_01 = "925f7b82"
app_key_01 = "36e76867b08c6842fb530f8c1c851693"


app_id_02 = "a0427f25"
app_key_02 = "e3d448df6e8b3b07b0bd556064aaddf0"

def food_search(food, cuisine, mealType):
    url = f"https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id_02}&app_key={app_key_02}"

    querystring = {"cuisineType": cuisine or None, "q": food, "mealType": mealType, "imageSize": "REGULAR"}
    
    response = requests.request("GET", url, params=querystring)
    if response.status_code == 200:        
        if "next" in response.json()["_links"]:
            next_page = response.json()["_links"]["next"]["href"]
        else:
            next_page = False
        # next_page = response.json()["_links"]["next"]["href"]
        res = response.json()["hits"]
        return res, next_page

    else:
        print(response.status_code)
        return None
    
def recipe_next(url):
    response = requests.request("GET", url).json()
    next_page = response["_links"]["next"]["href"]
    res = response["hits"]
    
    return res, next_page
    

def get_recipe_detail(recipe_link):
    # url = f"https://api.edamam.com/api/recipes/v2/{recipe_id}?type=public&app_id=925f7b82&app_key=36e76867b08c6842fb530f8c1c851693"
    print()
    print()
    print(recipe_link)
    print()
    print()
    response = requests.get(recipe_link).json()
    # print(json.dumps(response, indent=4))
    
    # res = response["hits"]
    return response


def add_recipe_to_personal_menu(recipe_id):
    url = f"https://api.edamam.com/api/recipes/v2/{recipe_id}?type=public&app_id={app_id_02}&app_key={app_key_02}"
    response = requests.get(url).json()
    
    return response