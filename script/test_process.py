import pytest
from api.api_login import LoginApi
from api.api_booking import BookingApi
from config import BASE_DIR
from util.read_file_tools import read_json


class TestProcess:

    @pytest.fixture(scope="class")
    def token(self):
        login_api = LoginApi()
        data = read_json(BASE_DIR + "/data/login.json")
        res = login_api.get_token(data)
        return res.json()["token"]

    def test_booking_lifecycle(self, token):
        booking_api = BookingApi()
        # 1. 创建订单
        data = {
            "firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-05"}
        }
        create_res = booking_api.create_booking(data)
        assert create_res.status_code == 200
        booking_id = create_res.json()["bookingid"]

        # 2. 修改订单
        data["firstname"] = "UpdatedName"
        update_res = booking_api.update_booking(booking_id, data, token)
        assert update_res.status_code == 200
        assert update_res.json()["firstname"] == "UpdatedName"

        # 3. 删除订单
        del_res = booking_api.delete_booking(booking_id, token)
        assert del_res.status_code == 201