from api.api_login import LoginApi
from config import BASE_DIR
from util.read_file_tools import read_json


class TestLogin:
    def setup_class(self):
        self.login_api = LoginApi()

    def test_get_token(self):
        data = read_json(BASE_DIR + "/data/login.json")
        resp = self.login_api.get_token(data)
        assert resp.status_code == 200
        assert "token" in resp.json()