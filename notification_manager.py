from twilio.rest import Client

TWILIO_ACCOUNT_SID =
TWILIO_ACCOUNT_AUTH_TOKEN =


class NotificationManager:

    def send_message(self, destination_city, origin_city, price):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"Cheapest flight to {destination_city} from {origin_city} found for £{price}",
            from_=,
            to=
        )
        print(message.body)
