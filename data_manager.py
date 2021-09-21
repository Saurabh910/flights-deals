import requests

SHEETY_PRICES_ENDPOINT =
AUTH =
headers = {
    "Authorization": f"Bearer {AUTH}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            response = requests.put(url=put_endpoint, json=new_data, headers=headers)
