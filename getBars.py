from tigeropen.common.consts import Language
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.consts import Language, Market, TimelinePeriod, QuoteRight

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
    return quote_client.get_bars('600570')
   
if __name__ == '__main__':
    a=get_quote()
    for bar in a:
        print(bar.close,bar.high,bar.low)
#    print(a) 一长串Bar对象
"""
    time = []
    open = []
    high = []
    low = []
    close = []
    volume=[]
    for bar in a:
        time.append(datetime.fromtimestamp(bar.time/1000))
        open.append(bar.open)
        high.append(bar.high)
        low.append(bar.low)
        close.append(bar.close)
        volumn.append(bar.volume)
    bars=pd.DataFrame(data=data,columns=[])
    print(bars)
   """
