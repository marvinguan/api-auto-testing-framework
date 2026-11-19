import json

from config import BASE_DIR


# 读取json文件
def read_json(file):  # 1 usage
    # 1、打开json文件
    with open(file, "r", encoding="utf-8") as f:
        # 2、加载json
        json_list = json.load(f)
    # print(json_list)
    # 注意返回结果
    return json_list

if __name__ == '__main__':
    print(read_json(BASE_DIR + "/data/login.json"))