"""
文章相关的API  专门封登录的模块
"""
import requests

from app import MP_BASE_URL, MP_HEADER, MIS_HEADER, APP_BASE_URL, APP_HEADER


# 自媒体
class PublishAritcle:

    def __init__(self):
        # 发布文章的请求地址
        self.pb_aritcle_url = MP_BASE_URL + "/mp/v1_0/articles"

    # 发布文章接口方法
    def test_pb_aritcle(self, title, content, channel_id):
        # 定义测试数据
        params = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "images": []}}
        # 调用POST接口
        return requests.post(url=self.pb_aritcle_url, json=params, headers=MP_HEADER)
# 后台系统管理
class Mis:
    def __init__(self):
        # 查询文章  # 审核文章
        self.query_Posts_url = MP_BASE_URL + "/mis/v1_0/articles"

    def test_inquire_article(self,title,channel):
        inquirt_article = {"title":title,"channel":channel}
        return requests.get(url=self.query_Posts_url,params=inquirt_article,headers=MIS_HEADER)
    # 审核文章
    def test_audit_article(self,article_ids,status):
        # 1,数据
        data_json = {"article_ids":article_ids, "status":status}
        return requests.put(url=self.query_Posts_url,json = data_json,headers=MIS_HEADER)

# app 接口 频道新闻推荐
class NewsChnnel:
    def __init__(self):
        self.chnnel_news_url = APP_BASE_URL + "/app/v1_1/articles"
    # 获取频道下的新闻
    def test_chnnel_news(self,channel_id,timestamp,with_top):
        data_chnnel_news = {"channel_id":channel_id,"timestamp":timestamp,"with_top":with_top}
        return requests.get(self.chnnel_news_url,params=data_chnnel_news,headers=APP_HEADER)
