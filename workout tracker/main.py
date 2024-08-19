import requests
from datetime import datetime
import os
API_KEY = os.environ["ENV_NIX_APP_KEY"]
API_ID = os.environ["ENV_NIX_APP_ID"]
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {"x-app-id":API_ID,
           "x-app-key":API_KEY
           }
parameters = {
    "query":input("What exercise did you do today? "),
    "gender":"female",
    "height_cm":151,
    "weight_kg":38,
    "age":16
}
response = requests.post(url=API_ENDPOINT,json=parameters,headers=headers)
result=response.json()

today = datetime.now()
sheety_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]
for exercise in result["exercises"]:
    sheety_inputs = {
        "workout":{
            "date":today.strftime("%d/%m/%Y"),
            "time":datetime.now().strftime("%X"),
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
sheet_header={
    "Authorization": F"Bearer {os.environ["ENV_SHEETY_TOKEN"]}"}
sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, headers=sheet_header)



