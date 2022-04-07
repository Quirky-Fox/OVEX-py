from .base import BaseClient


class Client(BaseClient):
    """
    Python SDK for the OVEX API.

    Example usage:

      from ovex_python.client import Client


      c = Client(api_key_id='key_id')
      try:
        res = c.get_ticker(pair='XBTZAR')
        print res
      except Exception as e:
        print e
    """
    
    def get_fee_withdraw(self, symbol=None):
        """
        Gets the withdrawal fees. If a currency symbol is provided, will return only fees for that currency, or else will return all.
        ----------------------------------------------------------------
        curl --location --request GET 'www.ovex.io/api/v2/fees/withdraw'
        """
        resp = self.do('GET', '/fees/withdraw', auth=True)
        fees = {l['currency']:{'currency_type':l['type'], 'fee':l['fee']['value'], 'fee_type':l['fee']['type']} for l in resp}
        if symbol:
            return fees[symbol.lower()]
        else: 
            return fees
        
    def get_fee_deposit(self, symbol=None):
        """
        Gets the deposit fees. If a currency symbol is provided, will return only fees for that currency, or else will return all.
        ----------------------------------------------------------------
        curl --location --request GET 'www.ovex.io/api/v2/fees/deposit'
        """
        resp = self.do('GET', '/fees/deposit', auth=True)
        fees = {l['currency']:{'currency_type':l['type'], 'fee':l['fee']['value'], 'fee_type':l['fee']['type']} for l in resp}
        if symbol:
            return fees[symbol.lower()]
        else: 
            return fees
        
    def get_quote_rfq(self, from_amount=None, to_amount=None, market='btczar', side='buy'):
        """
        Request for quote (RfQ). Get a strict all inclusive quote for trading between 2 currencies.

        Specify a market e.g. (btczar)

        Specify a 'side' of the market. e.g.('buy' btc with zar or 'sell' btc for ZAR)

        Specify either a from_amount OR to_amount e.g.(side = buy, from_amount = x ZAR, to_amount = y BTC). NB: If both from_amount and to_amount are specified, from_amount is used for quoting.

        ----------------------------------------------------------------
        
        market = Market for quote. Available markets: btczar, ethzar, tusdzar, usdtzar
        from_amount = Amount specified in input volume. E.g. (market = btczar, side = buy : from_amount is in zar. If side = sell, from_amount is in btc)
        side = Either 'buy or 'sell'. (Optional) Default: 'buy'
        to_amount = Amount specified in output volume. E.g. (market = btczar, side = buy : to_amount is in btc. If side = sell, to_amount is in zar)
        

        curl --location --request GET 'www.ovex.io/api/v2/rfq/get_quote'
        """
        market = market.lower()
        side = side.lower()
        if market not in ['btczar', 'ethzar', 'tusdzar', 'usdtzar']:
            raise ValueError('Invalid market')
        
        if not any([from_amount, to_amount]) or all([from_amount, to_amount]):
            raise ValueError('Invalid from_amount and to_amount - Specify either a from_amount OR to_amount')
        
        req = {
            'market': market,
            'side': side,
            'from_amount': from_amount,
            'to_amount': to_amount
        }
        return self.do('GET', '/rfq/get_quote', req=req, auth=True)


    def get_trades(self, limit=50, order_by='desc', timestamp=None, id_from=None, id_to=None):
        """
        Get the RfQ trades,

        ----------------------------------------------------------------
        
        limit = Limit the number of returned orders, default to 50. (Optional)
        order_by = If set, returned rfq trades will be sorted in specific order, default to 'desc'
        timestamp = An integer represents the seconds elapsed since Unix epoch. If set, only trades executed before the time will be returned.
        id_from = Trade id. If set, only trades created after the trade will be returned.
        id_to = Trade id. If set, only trades created before the trade will be returned.
        

        curl --location --request GET 'www.ovex.io/api/v2/rfq/trades'
        """
        
        req = {
            'limit': limit,
            'order_by': order_by,
            'timestamp': timestamp,
            'from': id_from,
            'to': id_to
        }
        return self.do('GET', '/rfq/trades', req=req, auth=True)
    
    def accept_quote(self,quote_token):
        """
        Accept a quote,

        ----------------------------------------------------------------
        
        quote_token = Unique token generated from requesting a quote obtained from the get_quote endpoint.
        

        curl --location --request GET 'www.ovex.io/api/v2/rfq/accept_quote'
        """
        
        req = {
            'quote_token': quote_token
        }
        return self.do('POST', '/rfq/accept_quote', req=req, auth=True)
    
    
    def get_withdraws(self, currency, page=1, limit=100):
        """
        Get the withdraws.

        ----------------------------------------------------------------
        
        currency = Any supported currencies: zar, btc, eth, tusd, ZAR, BTC, ETH, TUSD.
        page = Page number (defaults to 1). (Optional)
        limit = Number of withdraws per page (defaults to 100, maximum is 1000). (Optional)

        curl --location --request GET 'www.ovex.io/api/v2/withdraws'
        """
        
        req = {
            'currency': currency,
            'page': page,
            'limit': limit
        }
        return self.do('GET', '/withdraws', req=req, auth=True)
    
    def get_deposits(self, currency, limit=None, state=None):
        """
        Get the deposits.

        ----------------------------------------------------------------
        
        currency = Currency value contains zar, btc, eth, tusd, ZAR, BTC, ETH, TUSD. (Optional)
        limit = Set result limit. (Optional)
        state = State of the deposit. (Optional)

        curl --location --request GET 'www.ovex.io/api/v2/deposits'
        """
        
        req = {
            'currency': currency,
            'limit': limit,
            'state': state
        }
        return self.do('GET', '/deposits', req=req, auth=True)
    
    
    def get_deposit_info(self, txid):
        """
        Get the information about a specific deposit.

        ----------------------------------------------------------------
        
        txid = Transaction ID of the deposit

        curl --location --request GET 'www.ovex.io/api/v2/deposit'
        """
        
        req = {
            'txid': txid
        }
        return self.do('GET', '/deposit', req=req, auth=True)
    
    def get_deposit_address(self, currency):
        """
        Get the deposit address.

        ----------------------------------------------------------------
        
        currency = The currency for the deposit address.

        curl --location --request GET 'www.ovex.io/api/v2/deposit_address'
        """
        
        req = {
            'currency': currency
        }
        return self.do('GET', '/deposit_address', req=req, auth=True)
    
    
    
    def get_currencies(self, type=None):
        """
        Get all the currencies and all their information.

        ----------------------------------------------------------------
        
        type = 'coin'/'fiat'

        curl --location --request GET 'www.ovex.io/api/v2/currencies'
        """
        
        req = {
            'type': type
        }
        return self.do('GET', '/currencies', req=req, auth=False)
    
    
    def get_currency_info(self, id):
        """
        Get the currencies and all their information.

        ----------------------------------------------------------------
        
        id = the currency id.

        curl --location --request GET 'www.ovex.io/api/v2/currencies/{id}'
        """
        
        return self.do('GET', f'/currencies/{id}', auth=False)
    
    def get_accounts(self, currency=None):
        """
        Get the accounts.

        ----------------------------------------------------------------
        
        currency = User account currency.

        curl --location --request GET 'www.ovex.io/api/v2/accounts'
        """
        
        req = {
            'currency': currency
        }
        
        return self.do('GET', '/accounts', req=req, auth=True)
    
