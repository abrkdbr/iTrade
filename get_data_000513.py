from tigeropen.common.consts import Language
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.consts import Language, Market, TimelinePeriod, QuoteRight,BarPeriod
import time
import json
import sms

def get_client_config():
    """ 获取client_config
    https://www.itiger.com/openapi/info 开发者信息获取
    """
    client_config = TigerOpenClientConfig(sandbox_debug=False)
    client_config.private_key = read_private_key('/Users/yunqiuliu/Tiger-Trade/rsa_private_key.pem')
    client_config.tiger_id = '20150081'
    client_config.account = 'U8317066'
    client_config.language = Language.en_US
    return client_config

def get_quote(begin_time=None,Symbol=None):
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    #timeArray = time.strptime("2000-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
    #begin_time=int(time.mktime(timeArray))*10**3
    return quote_client.get_bars('000513',period=BarPeriod.ONE_MINUTE,begin_time=begintimestamp)
    
if __name__ == '__main__':
    current_tstamp=time.time()
    #should be run in the morning everyday later on.
    #today_time = time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))
    #timeArray = time.strptime(today_time,"%Y-%m-%d %H:%M:%S")
    #begin_time=int(time.mktime(timeArray))*10**3
    begintimestamp=1453426260000             #2016.1.22, ms
    t=time.time()                            #s
    print(str(t) + "current_time")
    stockfile=open("/Users/yunqiuliu/Tiger-Trade/000513.txt","a")
    while begintimestamp < t*10**3:
        print(str(begintimestamp))
        market_status=get_quote(begin_time=begintimestamp)
        print(market_status, file = stockfile)
        begintimestamp += 259740000          #ms
        time.sleep(1)
    stockfile.close()
  






"""

    if price>=57.00:
        print("send a message to Yunqiu")
        #调用aws短信接口
        sms.send_sms(Message='The price of 600570 is '+str(price)+'(Inprice:) now, can consider sell out')
        
    if price<=48.00:
        print("send a message to Yunqiu")
        #调用aws短信接口
        sms.send_sms(Message='The price of 600570 is '+str(price)+'(Inprice:) now, can consider BUY IN')
"""
