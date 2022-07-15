import requests
import datetime
import os
GENDER = 'male'
WEIGHT_KG = 50
HEIGHT_CM = 1.65
AGE = 25

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY_NUTRIMIX']

excercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
header_url = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}
exercise_text = input("Tell me which exercises you did: ")

excercise_url = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=excercise_endpoint,
                         headers=header_url, json=excercise_url)
data = response.json()

sheety_endpoint = f"https://api.sheety.co/{os.environ['API_KEY_SHEET']}/copiaDeMyWorkouts/workouts"
date=datetime.datetime.now().strftime('%d/%m/%Y')
hour=datetime.datetime.now().strftime('%H:%M:%S')
sheet_header={
    "Authorization": "Basic ZW5yaXF1ZTpqciU0bTNjJnk="
}
for info in data['exercises']:
    sheet_inputs  = {
        "workout": {
            "date": date,
            "time": hour,
            "exercise": info['name'].title(),
            "duration": f"{info['duration_min']}",
            "calories": info['nf_calories']
        }
    }
    response_sheety=requests.post(sheety_endpoint,json=sheet_inputs,headers=sheet_header)
    print(response_sheety.text)
