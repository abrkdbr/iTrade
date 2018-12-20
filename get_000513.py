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

def get_quote():
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    #quote_client.get_market_status(Market.ALL)
    #quote_client.get_briefs(symbols=['AAPL', '00700', '600519'], include_ask_bid=True, right=QuoteRight.BR)
    #quote_client.get_briefs(symbols=['00700', '600519'], include_ask_bid=True, right=QuoteRight.BR)
#    return quote_client.get_timeline('AAPL', period=TimelinePeriod.5MIN, begin_time='20000101', include_hour_trading=True)
    timeArray = time.strptime("2000-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
    #today_time = time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))
    #timeArray = time.strptime(today_time,"%Y-%m-%d %H:%M:%S")
    begin_time=int(time.mktime(timeArray))*10**3
    return quote_client.get_bars('000513',period=BarPeriod.DAY,begin_time=begin_time)
    #return quote_client.get_bars('AAPL',period=BarPeriod.FIVE_MINUTES,begin_time=begin_time)
#    return quote_client.get_briefs(symbols=['000513'], include_ask_bid=True, right=QuoteRight.BR)
    #quote_client.get_hour_trading_timeline('AAPL')
    
if __name__ == '__main__':
    market_status=get_quote()
    print(market_status)
    print(market_status[-1])
    print(market_status[-1].close)
    price=market_status[-1].close

#    if price>=33.00 or price<=29.00:
    if price>=33.00:
        print("send a message to Yunqiu")
        #调用aws短信接口
        sms.send_sms(Message='The price of 000513 is '+str(price)+'(Inprice:27.88) now, can consider sell out')
    if price<=28.00:
        print("send a message to Yunqiu")
        #调用aws短信接口
        sms.send_sms(Message='The price of 000513 is '+str(price)+'(Inprice:27.88) now, can consider BUY IN')

