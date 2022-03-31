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
        

        curl --location --request GET 'www.ovex.io/api/v2/rfq/get_quote?market=btczar&from_amount=500000&side=buy&to_amount=1'
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


