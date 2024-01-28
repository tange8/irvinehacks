"""
app.py

This one file is all you need to start off with your FastAPI server!
"""

from typing import Optional

import uvicorn
import requests
from fastapi import FastAPI, status


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
@app.get("/mealplanner")

def show_meal_plans():

    url = "https://production.suggestic.com/graphql"

    payload = "{\"query\":\"{\\n  mealPlan {\\n    day\\n    date(useDatetime: false)\\n    calories\\n    meals {\\n      id\\n      calories\\n      meal\\n      numOfServings\\n      recipe {\\n        name\\n        numberOfServings\\n        nutrientsPerServing {\\n          calories\\n        }\\n      }\\n    }\\n  }\\n}\\n\"}"
    headers = {
        "User-Agent": "insomnia/8.6.0",
        "Content-Type": "application/json",
        "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
        "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.content)
    return response.text

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
