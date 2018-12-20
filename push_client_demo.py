import time
from tigeropen.push.push_client import PushClient
from tigeropen.examples.client_config import get_client_config
from tigeropen.common.consts import THREAD_LOCAL, SecurityType, Market, Currency
from tigeropen.trade.domain.order import ORDER_STATUS
from tigeropen.trade.request.model import AccountsParams
from tigeropen.common.response import TigerResponse
from tigeropen.tiger_open_client import TigerOpenClient
from tigeropen.trade.trade_client import TradeClient
from tigeropen.quote.request import OpenApiRequest
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.consts import Language
from tigeropen.common.util.signature_utils import read_private_key

def get_client_config():
    client_config = TigerOpenClientConfig(sandbox_debug=False)
    client_config.language = Language.en_US

    client_config.private_key=read_private_key('/Users/yunqiuliu/Tiger-Trade/rsa_private_key.pem')
    client_config.tiger_id='20150081'
    client_config.account='U8317066'
    return client_config

def on_query_subscribed_quote(symbols, focus_keys, limit, used):
    print(symbols, focus_keys, limit, used)


def on_quote_changed(symbol, items, hour_trading):
    print(symbol, items, hour_trading)


if __name__ == '__main__':
    client_config = get_client_config()
    protocol, host, port = client_config.socket_host_port
    push_client = PushClient(host, port, use_ssl=(protocol == 'ssl'))
    push_client.quote_changed = on_quote_changed
    push_client.subscribed_symbols = on_query_subscribed_quote
    push_client.connect(client_config.tiger_id, client_config.private_key)

    push_client.query_subscribed_quote()
    push_client.subscribe_quote(['AAPL', 'GOOG'])
    push_client.subscribe_asset()

    time.sleep(600)
    push_client.disconnect()
