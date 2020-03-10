# 文章发布-审核-查看流程
import logging
import time

import pytest

from api import FactoryApi


# 定义测试类
from app import MP_HEADER, MIS_HEADER, APP_HEADER, basic_loger
from utils.utils_toos import utils_toos, data_read


class TestPbEmQyAritcle:
    aricle_title = None
    aricle_id = None

    # 定义测试方法
    @pytest.mark.parametrize("mobile,code,status_code,message",
                             data_read("./data/data.json"))
    def test_mp_login(self,mobile,code,status_code,message):
        # 定义测试数据
        mobile = mobile
        code = code
        # 调用登陆的方法
        mp_login_response = FactoryApi.mp_login.test_mp_login(mobile, code)
        print("自媒体登陆结果返回信息为:", mp_login_response.json())
        logging.info("登录成功了={}".format(mp_login_response))
        # 获取实际结果进行断言
        # assert mp_login_response.status_code == 201
        # assert mp_login_response.json().get("message") == "OK"
        assert utils_toos(mp_login_response,status_code,message)
        # 获取登陆后的token并存储
        mp_token = mp_login_response.json().get("data").get("token")
        print("自媒体登陆后返回token={}".format(mp_token))
        # 给mp后续头部信息添加登陆后键值对
        MP_HEADER["Authorization"] = "Bearer " + mp_token
        print("登陆后基础配置的头部信息为=", MP_HEADER)
    # 自媒体-- 发布文章测试法
    def test_aricle(self):
        # 1，定义测试数据，每一组数据代表的就是一种测试情况
        self.aricle_title = "一定可以，相信自已"
        content = "加油"
        channel_id = 1
        # 2.调用测试法：执行对应业务的求接口方法
        pb_al_response = FactoryApi.pub_lish_aritcle.test_pb_aritcle(
            self.aricle_title,content,channel_id)
        # 3. 断言
        assert pb_al_response.status_code == 201
        # 提取 id 的值
        TestPbEmQyAritcle.aricle_id = pb_al_response.json().get("data").get("id")
        print("发布文章的id:",self.aricle_id)


    # 后台管理系统—登陆
    def test_mis_login(self):

        # 1.定义测试数据
        account = "testid"
        password = "testpwd123"
        # 2.调用测试方法
        mis_login = FactoryApi.aeminst_series.test_mis_login(account,password)
        print("后台登录结果",mis_login.json())
        # 获取测试结果
        status_code = mis_login.status_code
        msg = mis_login.json().get("message")
        # 断言
        assert status_code ==201
        assert  msg =="OK"
        # 4.获取关联数据
        mis_token = mis_login.json().get("data").get("token")
        MIS_HEADER["Authorization"] = "Bearer " + mis_token
    # 查询文章
    def test_quire_article(self):
        # 1,测试数据
        aricle_title = self.aricle_title
        channel = "html"
        # 2，调用测试方法
        result_qiery = FactoryApi.mis.test_inquire_article(aricle_title,channel)
        print("后台登录结果", result_qiery.json())
        # 3，获取测试后的结果
        status_code = result_qiery.status_code
        msg = result_qiery.json().get("message")
        # 4，断言
        assert status_code == 200
        assert msg == "OK"
    #  审核文章
    def test_audit_articl(self):
        # 测试数据
        article_ids =TestPbEmQyAritcle.aricle_id # 审核的内容 数据
        print(article_ids)
        status = 2  # 选择2表示文章退审核
        # 调用测试方法
        result_data = FactoryApi.mis.test_audit_article(article_ids, status)
        print("审核文章的结果", result_data.json())
        # 获取测试后的结果
        status_code = result_data.status_code
        msg = result_data.json().get("message")
        # 断言
        assert  status_code == 201
        assert  msg == "OK"

    #  APP 测试用例
    def test_app_login(self):
        # 数据
        mobile = "13911111111"
        code = "246810"
        # 测试用例
        app_result = FactoryApi.app_login.test_app_login(mobile,code)
        print("审核文章的结果", app_result.json())
        # 获取测试后的结果
        status_code = app_result.status_code
        msg = app_result.json().get("message")
        # 断言
        assert status_code == 201
        assert msg == "OK"
        # 提取 token
        app_token = app_result.json().get("data").get("token")
        APP_HEADER["Authorization"] = "Bearer " + app_token
    # 获取频道下的新闻
    def test_chnnel_news_aritcle(self):
        # 定义测试数据
        channel_id = 1
        time_stamp = int(time.time() * 1000)
        print("时间")
        with_top = 1
        logging.info("频道名称为={}".format(channel_id))
        # 执行测试用例
        result_news= FactoryApi.chnnel_new_coome.test_chnnel_news(channel_id,time_stamp,with_top)
        print("获取频道下的新闻",result_news.json())
        # 获取测试响应的数据
        status_code = result_news.status_code
        msg = result_news.json().get("message")
        # 进行断言
        assert status_code == 200
        assert msg == "OK"

