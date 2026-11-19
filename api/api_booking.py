import logging

import requests

from api.api_login import LoginApi
from config import BASE_URL


class BookingApi:
    def __init__(self):
        self.booking_url = BASE_URL + "/booking"

    def create_booking(self, data):
        try:
            resp = requests.post(self.booking_url, json=data)
            logging.info("create booking success")
        except Exception as e:
            logging.error("create booking error")
        return resp


    def update_booking(self, booking_id, data, token):
        try:
            resp = requests.put(f"{self.booking_url}/{booking_id}", json=data, cookies={"token": token})
            logging.info("update_booking success")
        except Exception as e:
            logging.error("update_booking error")
        return resp

    def delete_booking(self, booking_id, token):
        try:
            resp = requests.delete(f"{self.booking_url}/{booking_id}", cookies={"token": token})
            logging.info("delete booking success")
        except Exception as e:
            logging.error("delete booking error")
        return resp



if __name__ == '__main__':
    booking = BookingApi()
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    resp = booking.create_booking(data)
    print(resp.json())
    print(resp.status_code)
    booking_id = resp.json()["bookingid"]
    data_token = {'username': 'admin', 'password': 'password123'}
    token = LoginApi().get_token(data_token).json()["token"]
    data["firstname"] = "Jims"
    resp = booking.update_booking(booking_id, data, token)
    print(resp.json())
    resp = booking.delete_booking(booking_id, token)
    print(resp.status_code)