import json


def utils_toos(requests_result, requests_code, requests_msg):
    status_code = requests_result.status_code
    msg = requests_result.json().get("message")
    # 进行断言
    if status_code == requests_code and msg == requests_msg:
        return True
    else:
        return False


def data_read(data_json):
    data_js = []
    with open(data_json, encoding="utf-8") as f:
        # 读取数据
        f_data = json.load(f)
        # 历所有的键值
        for case_data in f_data.values():
                #再历键值
                data_js.append(list(case_data.values()))  # 列表的形式
    print(data_js)
    return data_js

