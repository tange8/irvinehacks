"""
app.py

This one file is all you need to start off with your FastAPI server!
"""

from typing import Optional

import uvicorn
import requests
import ast
import json

from fastapi import FastAPI, status, Request
from pydantic import BaseModel, ValidationError, validate_call

class MealAttributes(BaseModel):
    breakfast_time: int
    lunch_time: int
    dinner_time: int
    snack_time: int


# Initializing and setting configurations for your FastAPI application is one
# of the first things you should do in your code.
app = FastAPI()


# The line starting with "@" is a Python decorator. For this tutorial, you
# don't need to know exactly how they work, but if you'd like to read more on
# them, see https://peps.python.org/pep-0318/.
#
# In short, the decorator declares the function it decorates as a FastAPI route
# with the path of the provided route. This line declares that a new GET route
# called "/" so that if you access "http://localhost:5000/", the below
# dictionary will be returned as a JSON response with the status code 200.
#
# For any other routes you declare, like the `/home` route below, you can access
# them at "http://localhost:5000/home". Because of this, we'll be omitting the
# domain portion for the sake of brevity.
@app.get("/")
def read_root():
    return "<div>HELLO IRVINE HACKS</div>"


@app.get("/home")
def home():
    return {"message": "This is the home page"}


# The routes that you specify can also be dynamic, which means that any path
# that follows the format `/items/[some integer]` is valid. When providing
# such path parameters, you'll need to follow this specific syntax and state
# the type of this argument.
#
# This path also includes an optional query parameter called "q". By accessing
# the URL "/items/123456?q=testparam", the JSON response:
#
# { "item_id": 123456, "q": "testparam" }
#
# will be returned. Note that if `item_id` isn't an integer, FastAPI will
# return a response containing an error statement instead of our result.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}




# TODO: Add POST route for demo
# @app.post("/generatemealplanner")
# def generate_meal_plan(prepTime: MealAttributes):
#     url = "https://production.suggestic.com/graphql"

#     payload = '"{\"query\":\"mutation($breakfast: Int, $dinner: Int, $snack: Int, $lunch: Int) {\\n  generateMealPlan (\\n     maxTimeMinutes:{\\n      breakfast:$breakfast,\\n      dinner:$dinner,\\n      snack:$snack,\\n      lunch:$lunch\\n    }\\n  ) \\n    {\\n    success\\n    message\\n  }\\n}\",\"variables\":\"{\\n\\t\\\"breakfast\\\":' +  str(prepTime.breakfast_time) + ',\\n\\t\\\"snack\\\":' + str(prepTime.snack_time) + ',\\n\\t\\\"lunch\\\":' + str(prepTime.lunch_time) + ',\\n\\t\\\"dinner\\\":' + str(prepTime.dinner_time) + '\\n}\"}"'
#     headers = {
#         "User-Agent": "insomnia/8.6.0",
#         "Content-Type": "application/json",
#         "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
#         "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
#     }

#     response = requests.request("POST", url, data=payload, headers=headers)
#     print(f'THIS IS FROM OUR GENERATE MEAL PLAN{response.text}')
 
#     return response.text

@app.get("/generate20")
def generate_20():


    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"mutation($breakfast: Int, $dinner: Int, $snack: Int, $lunch: Int) {\\n  generateMealPlan (\\n     maxTimeMinutes:{\\n      breakfast:$breakfast,\\n      dinner:$dinner,\\n      snack:$snack,\\n      lunch:$lunch\\n    }\\n  ) \\n    {\\n    success\\n    message\\n  }\\n}\",\"variables\":\"{\\n\\t\\\"breakfast\\\": 20,\\n\\t\\\"snack\\\": 20,\\n\\t\\\"lunch\\\": 20,\\n\\t\\\"dinner\\\": 20\\n}\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

@app.get("/generate10")
def generate_10():

    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"mutation($breakfast: Int, $dinner: Int, $snack: Int, $lunch: Int) {\\n  generateMealPlan (\\n     maxTimeMinutes:{\\n      breakfast:$breakfast,\\n      dinner:$dinner,\\n      snack:$snack,\\n      lunch:$lunch\\n    }\\n  ) \\n    {\\n    success\\n    message\\n  }\\n}\",\"variables\":\"{\\n\\t\\\"breakfast\\\": 10,\\n\\t\\\"snack\\\": 10,\\n\\t\\\"lunch\\\": 10,\\n\\t\\\"dinner\\\": 10\\n}\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

@app.get("/generate30")
def generate_30():
    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"mutation($breakfast: Int, $dinner: Int, $snack: Int, $lunch: Int) {\\n  generateMealPlan (\\n     maxTimeMinutes:{\\n      breakfast:$breakfast,\\n      dinner:$dinner,\\n      snack:$snack,\\n      lunch:$lunch\\n    }\\n  ) \\n    {\\n    success\\n    message\\n  }\\n}\",\"variables\":\"{\\n\\t\\\"breakfast\\\": 30,\\n\\t\\\"snack\\\": 30,\\n\\t\\\"lunch\\\": 30,\\n\\t\\\"dinner\\\": 30\\n}\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

@app.get("/generate40")
def generate_40():
    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"mutation($breakfast: Int, $dinner: Int, $snack: Int, $lunch: Int) {\\n  generateMealPlan (\\n     maxTimeMinutes:{\\n      breakfast:$breakfast,\\n      dinner:$dinner,\\n      snack:$snack,\\n      lunch:$lunch\\n    }\\n  ) \\n    {\\n    success\\n    message\\n  }\\n}\",\"variables\":\"{\\n\\t\\\"breakfast\\\": 40,\\n\\t\\\"snack\\\": 40,\\n\\t\\\"lunch\\\": 40,\\n\\t\\\"dinner\\\": 40\\n}\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

# @app.get("/generatemealplanner")
# async def generate_meal_plan(my_request: Request, items: MealAttributes):
#     url = "https://production.suggestic.com/graphql"
#     result = await my_request.json()
#     print(result)
#     payload = '"{\"query\":\"mutation($breakfast: Int, $dinner: Int, $snack: Int, $lunch: Int) {\\n  generateMealPlan (\\n     maxTimeMinutes:{\\n      breakfast:$breakfast,\\n      dinner:$dinner,\\n      snack:$snack,\\n      lunch:$lunch\\n    }\\n  ) \\n    {\\n    success\\n    message\\n  }\\n}\",\"variables\":\"{\\n\\t\\\"breakfast\\\":' +  str(result["breakfast_time"]) + ',\\n\\t\\\"snack\\\":' + str(result["snack_time"]) + ',\\n\\t\\\"lunch\\\":' + str(result["lunch_time"]) + ',\\n\\t\\\"dinner\\\":' + str(result["dinner_time"]) + '\\n}\"}"'
#     print(payload)
#     headers = {
#         "User-Agent": "insomnia/8.6.0",
#         "Content-Type": "application/json",
#         "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
#         "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
#     }

#     response = requests.request("POST", url, data=payload, headers=headers)
#     print(response.text)
#     # print(f'THIS IS FROM OUR GENERATE MEAL PLAN{response.text}')
 
#     return response.text


@app.get("/showrecipes")
async def only_show_recipe():
    

    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"{\\n  mealPlan {\\n\\n    meals {\\n    \\n      recipe {\\n\\t\\t\\t\\tid\\n      \\n      }\\n    }\\n  }\\n}\\n\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    response_text = response.text
    list_recipe_id = []
    list_responses = response.text.split('{')
    for string in list_responses:
        new_str = string.replace('"', '') 
        new_str = new_str.replace(',', '')
        new_str = new_str.replace('}}', '')
        if 'id' in new_str:
            if new_str[-2:] != '==':
                last_string = new_str.index('=')
                new_str = new_str[3:last_string+2]
                list_recipe_id.append(new_str)
            else:
                new_str = new_str[3:]
                list_recipe_id.append(new_str)
    for id in list_recipe_id:
        await get_recipe(id=id)
    # print(list_responses)
    return response_text

@app.get("/showmealplans")
async def show_meal_plans():
    final_dict = {}
    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"{\\n  mealPlan {\\n    day\\n    date(useDatetime: false)\\n    calories\\n    meals {\\n      id\\n      calories\\n      meal\\n      numOfServings\\n      recipe {\\n        name\\n\\t\\t\\t\\tid\\n        numberOfServings\\n        nutrientsPerServing {\\n          calories\\n        }\\n      }\\n    }\\n  }\\n}\\n\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    # print(f'THIS IS FROM OUR SHOW MEAL PLAN{response.text}')
    response_text = response.text.strip("\\")
    res = json.loads(response_text)
    if len(res) != 0 and len(res['data']['mealPlan']) != 0:
        first_day = (res['data']['mealPlan'][0])
        for meal in first_day['meals']:
            if 'breakfast' in meal.values():
                final_dict['breakfast'] = {'calories': meal['calories'], 'meal': meal['recipe']['name'], 'recipeId': meal['recipe']['id']}
            elif 'lunch' in meal.values():
                final_dict['lunch'] = {'calories': meal['calories'], 'meal': meal['recipe']['name'], 'recipeId': meal['recipe']['id']}
            elif 'dinner' in meal.values():
                final_dict['dinner'] = {'calories': meal['calories'], 'meal': meal['recipe']['name'], 'recipeId': meal['recipe']['id']}
            elif 'snack' in meal.values():
                final_dict['snack'] = {'calories': meal['calories'], 'meal': meal['recipe']['name'], 'recipeId': meal['recipe']['id']}
    recipe_dict = {}
    for i in final_dict:
        # print(final_dict[i]['recipeId'])
        recipe = await get_recipe(final_dict[i]['recipeId'])
        recipe_dict[i] = recipe
    # print(recipe_dict)
    # print(final_dict)
    return final_dict, recipe_dict

async def get_recipe(id: str):

    url = "https://production.suggestic.com/graphql"
    # id = "UmVjaXBlOjZjMDEyY2M3LWI1MjgtNDQ3Yy04Njc0LWE2MTUxZjI3ZjkxNA=="
    payload = "{\"query\":\"{\\n  recipe(id: \\\"UmVjaXBlOjZjMDEyY2M3LWI1MjgtNDQ3Yy04Njc0LWE2MTUxZjI3ZjkxNA==\\\") {\\n    databaseId\\n    totalTime\\n    totalTimeInSeconds\\n    name\\n    rating\\n    numberOfServings\\n    ingredientLines\\n    ingredients {\\n      name\\n    }\\n    language\\n    courses\\n    cuisines\\n    source {\\n      siteUrl\\n      displayName\\n      recipeUrl\\n    }\\n    mainImage\\n    isPremium\\n    isFeatured\\n    author\\n    authorAvatar\\n    ingredientsCount\\n    favoritesCount\\n    isUserFavorite\\n    inUserShoppingList\\n    weightInGrams\\n    servingWeight\\n    isLogged\\n    relativeCalories {\\n      carbs\\n      fat\\n      protein\\n      fat\\n    }\\n    instructions\\n    nutritionalInfo {\\n      calories\\n      protein\\n      carbs\\n      fat\\n      sugar\\n      fiber\\n      saturatedFat\\n      monounsaturatedFat\\n      polyunsaturatedFat\\n      transFat\\n      cholesterol\\n      sodium\\n      potassium\\n      vitaminA\\n      vitaminC\\n      calcium\\n      iron\\n      netcarbs\\n    }\\n  }\\n}\\n\"}"
    payload2= '"{\"query\":\"{\\n  recipe(id: \\\"' + id + '\\\") {\\n    databaseId\\n    totalTime\\n    totalTimeInSeconds\\n    name\\n    rating\\n    numberOfServings\\n    ingredientLines\\n    ingredients {\\n      name\\n    }\\n    language\\n    courses\\n    cuisines\\n    source {\\n      siteUrl\\n      displayName\\n      recipeUrl\\n    }\\n    mainImage\\n    isPremium\\n    isFeatured\\n    author\\n    authorAvatar\\n    ingredientsCount\\n    favoritesCount\\n    isUserFavorite\\n    inUserShoppingList\\n    weightInGrams\\n    servingWeight\\n    isLogged\\n    relativeCalories {\\n      carbs\\n      fat\\n      protein\\n      fat\\n    }\\n    instructions\\n    nutritionalInfo {\\n      calories\\n      protein\\n      carbs\\n      fat\\n      sugar\\n      fiber\\n      saturatedFat\\n      monounsaturatedFat\\n      polyunsaturatedFat\\n      transFat\\n      cholesterol\\n      sodium\\n      potassium\\n      vitaminA\\n      vitaminC\\n      calcium\\n      iron\\n      netcarbs\\n    }\\n  }\\n}\\n\"}"'
    payload2 = payload2[1:-1]
    # print(payload)
    # print(payload2)
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload2, headers=headers)
    response_text = response.text.strip("\\")
    response_text = response_text.strip("\\n")
    res = json.loads(response_text)
    sorted_dict = {}
    sorted_dict["name"] = res["data"]["recipe"]["name"]
    sorted_dict["ingredients"] = res["data"]["recipe"]["ingredientLines"]
    sorted_dict["image"] = res["data"]["recipe"]["mainImage"]
    sorted_dict["directions"] = res["data"]["recipe"]["instructions"]

    # print(sorted_dict)
    
    return sorted_dict

@app.get("/showsinglerecipe")
# def get_recipe(id: str):

#     url = "https://production.suggestic.com/graphql"
#     # id = "UmVjaXBlOjZjMDEyY2M3LWI1MjgtNDQ3Yy04Njc0LWE2MTUxZjI3ZjkxNA=="
#     payload = "{\"query\":\"{\\n  recipe(id: \\\"UmVjaXBlOjZjMDEyY2M3LWI1MjgtNDQ3Yy04Njc0LWE2MTUxZjI3ZjkxNA==\\\") {\\n    databaseId\\n    totalTime\\n    totalTimeInSeconds\\n    name\\n    rating\\n    numberOfServings\\n    ingredientLines\\n    ingredients {\\n      name\\n    }\\n    language\\n    courses\\n    cuisines\\n    source {\\n      siteUrl\\n      displayName\\n      recipeUrl\\n    }\\n    mainImage\\n    isPremium\\n    isFeatured\\n    author\\n    authorAvatar\\n    ingredientsCount\\n    favoritesCount\\n    isUserFavorite\\n    inUserShoppingList\\n    weightInGrams\\n    servingWeight\\n    isLogged\\n    relativeCalories {\\n      carbs\\n      fat\\n      protein\\n      fat\\n    }\\n    instructions\\n    nutritionalInfo {\\n      calories\\n      protein\\n      carbs\\n      fat\\n      sugar\\n      fiber\\n      saturatedFat\\n      monounsaturatedFat\\n      polyunsaturatedFat\\n      transFat\\n      cholesterol\\n      sodium\\n      potassium\\n      vitaminA\\n      vitaminC\\n      calcium\\n      iron\\n      netcarbs\\n    }\\n  }\\n}\\n\"}"
#     payload2= '"{\"query\":\"{\\n  recipe(id: \\\"' + id + '\\\") {\\n    databaseId\\n    totalTime\\n    totalTimeInSeconds\\n    name\\n    rating\\n    numberOfServings\\n    ingredientLines\\n    ingredients {\\n      name\\n    }\\n    language\\n    courses\\n    cuisines\\n    source {\\n      siteUrl\\n      displayName\\n      recipeUrl\\n    }\\n    mainImage\\n    isPremium\\n    isFeatured\\n    author\\n    authorAvatar\\n    ingredientsCount\\n    favoritesCount\\n    isUserFavorite\\n    inUserShoppingList\\n    weightInGrams\\n    servingWeight\\n    isLogged\\n    relativeCalories {\\n      carbs\\n      fat\\n      protein\\n      fat\\n    }\\n    instructions\\n    nutritionalInfo {\\n      calories\\n      protein\\n      carbs\\n      fat\\n      sugar\\n      fiber\\n      saturatedFat\\n      monounsaturatedFat\\n      polyunsaturatedFat\\n      transFat\\n      cholesterol\\n      sodium\\n      potassium\\n      vitaminA\\n      vitaminC\\n      calcium\\n      iron\\n      netcarbs\\n    }\\n  }\\n}\\n\"}"'
#     payload2 = payload2[1:-1]
#     print(payload)
#     print(payload2)
#     headers = {
#         "User-Agent": "insomnia/8.6.0",
#         "Content-Type": "application/json",
#         "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
#         "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
#     }

#     response = requests.request("POST", url, data=payload2, headers=headers)

#     return response.text

@app.get("/removemeal")
def remove_meal_plan():

    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"mutation {\\n  removeMealPlan {\\n    success\\n    message\\n  }\\n}\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
