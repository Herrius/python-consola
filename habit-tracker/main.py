
import requests

pixela_endpoint="https://pixe.la/v1/users"
TOKEN="eyJ1c2VybmFtZSI6ImhhcnJpdXMiLCJhZ3JlZVRlcm1zT2ZTZXJ2aWNlIjoieWVzIiwibm90TWlub3IiOiJ5ZXMifQ"
USERNAME="harrius"
user_params={
    "token":TOKEN,
    "username": "harrius",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
# User registe through method post
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":"meditation0",
    "name":"Meditation Graph",
    "unit":"min",
    "type":"int",
    "color":"ajisai",
    "timezone":"America/Lima"
}

headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

check_habit_config={
    "date":"20220714",
    "quantity":"10"
}
check_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

response=requests.post(url=check_endpoint,json=check_habit_config,headers=headers)
print(response.text)
