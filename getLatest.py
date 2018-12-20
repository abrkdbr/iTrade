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

def get_quote(symbol=None):
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    return quote_client.get_hour_trading_timeline(symbol=symbol) 
   
if __name__ == '__main__':
#    symbol_list=['TSLA','600570','000513','PDD','MLNX'] #not work for 600570,000513.
    symbol_list=['TSLA','PDD','MLNX']
    for symbol in symbol_list:
        hour_trading,time_line=get_quote(symbol=symbol)
        print("**********Hour Trading start:"+symbol+" **********")
        print(hour_trading.__dict__)
        print("**********Hour Trading end:"+symbol+" **********")
