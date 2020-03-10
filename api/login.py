import requests
from app import MP_BASE_URL, MP_HEADER, MIS_HEADER


# 自媒体
class MpLogin:

    def __init__(self):
        # 自媒体登陆的请求地址
        self.mp_login_url = MP_BASE_URL + "/mp/v1_0/authorizations"

    # 登陆的测试方法
    def test_mp_login(self, mobile, code):
        # 定义数据
        params = {"mobile": mobile, "code": code}
        # 执行请求
        return requests.post(url=self.mp_login_url, json=params,
                             headers=MP_HEADER)

# 后台管理系统
class AdministSeries:
    # 登录接口
    def __init__(self):
        self.administ_series = MP_BASE_URL + "/mis/v1_0/authorizations"
    # 登陆的测试方法
    def test_mis_login(self,account,password):
        params= {"account":account,"password":password}
        return  requests.post(url=self.administ_series,json=params,headers=MIS_HEADER)

# APP
class App():
    def __init__(self):
        self.app = MP_BASE_URL + "/app/v1_0/authorizations"
    # 登陆的测试方法
    def test_app_login(self,mobile,code):
        params = {"mobile": mobile, "code": code}
        return  requests.post(url=self.app,json=params,headers=MP_HEADER)
















