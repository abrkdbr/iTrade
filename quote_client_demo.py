# -*- coding: utf-8 -*-
"""
Created on 2018/10/31
@author: 
"""
import logging

from tigeropen.common.consts import Market, QuoteRight, TimelinePeriod
from tigeropen.quote.quote_client import QuoteClient
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


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a', )
logger = logging.getLogger('TigerOpenApi')

client_config = get_client_config()
openapi_client = QuoteClient(client_config, logger=logger)


def get_quote():
    openapi_client.get_market_status(Market.US)
    openapi_client.get_briefs(symbols=['AAPL', '00700', '600519'], include_ask_bid=True, right=QuoteRight.BR)
    openapi_client.get_timeline('AAPL', period=TimelinePeriod.DAY, include_hour_trading=True)
    openapi_client.get_bars('AAPL')
    openapi_client.get_hour_trading_timeline('AAPL')


if __name__ == '__main__':
    get_quote()
