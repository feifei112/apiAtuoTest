"""
工厂类
"""

from api.aritcle import PublishAritcle, Mis, NewsChnnel
from api.login import MpLogin, AdministSeries, App
from app import basic_loger
basic_loger()

class FactoryApi:
    # 自媒体登陆类的类属性
    ChannelNewsRecomme = None
    mp_login = MpLogin()

    pub_lish_aritcle = PublishAritcle()

    aeminst_series = AdministSeries()

    mis = Mis()

    app_login = App()

    chnnel_new_coome =NewsChnnel()


