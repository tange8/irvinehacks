import requests

url = "https://production.suggestic.com/graphql"

payload = "{\"query\":\"{\\n  mealPlan {\\n    day\\n    date(useDatetime: false)\\n    calories\\n    meals {\\n      id\\n      calories\\n      meal\\n      numOfServings\\n      recipe {\\n        name\\n        numberOfServings\\n        nutrientsPerServing {\\n          calories\\n        }\\n      }\\n    }\\n  }\\n}\\n\"}"
headers = {
    "User-Agent": "insomnia/8.6.0",
    "Content-Type": "application/json",
    "sg-user": "93cd96ab-0693-4382-9355-9285eb065bf0",
    "Authorization": "Token e022ada161fee90d3f32f6ad37bbb1eaf1cf64b1"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)