import logging
import requests
from config import BASE_URL


class LoginApi:
    def __init__(self):
        # 登录地址
        self.login_url = BASE_URL + "/auth"

    def get_token(self, data):
        # 打印日志
        logging.info(f"正在请求登录接口: {self.login_url}, 参数: {data}")
        try:
            resp = requests.post(self.login_url, json=data)
            logging.info(f"登录响应结果状态码: {resp.status_code}")
        except Exception as e:
            logging.error("登录响应结果获取失败")
        return resp


if __name__ == '__main__':
    login = LoginApi()
    data = {'username': 'admin', 'password': 'password123'}
    resp = login.get_token(data)
    print(resp.json())
    print(resp.status_code)