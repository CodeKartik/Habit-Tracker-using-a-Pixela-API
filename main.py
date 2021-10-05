import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "your_user_name"
TOKEN = "Your_API_key"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a user account and make your own api key in pixel

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

# Create a graph for habit tracking using a post request to pixel API

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hr",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
response.raise_for_status()
print(response.text)


# Create a pixel in the graph for habit tracking using a post request to pixel API

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? : "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
response.raise_for_status()
print(response.text)


# Update your pixel data if you need using a put request for the API

update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_pixel_data = {
    "quantity": "3.2",
}
response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
response.raise_for_status()
print(response.text)


# Finally you can delete a data from graph using a delete request as follows

delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
