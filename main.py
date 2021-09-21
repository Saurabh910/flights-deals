from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

# SHEETY MANAGER
AUTH =
SHEETY_ENDPOINT =

headers = {
    "Authorization": f"Bearer {AUTH}"
}

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row["iataCode"] == "":
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if destination["lowestPrice"] >= flight:
        notification_manager = NotificationManager()
        notification_manager.send_message(destination["city"], ORIGIN_CITY_IATA, flight)
