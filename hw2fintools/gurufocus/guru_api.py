import requests
import pandas as pd


class DividendHistory:

    def __init__(self, **kwargs):
        self.token = kwargs.get('token', 'error')
        self.ticker = kwargs.get('ticker', 'error')
        self.raw_data = self._raw_data()
        self.raw_df = self._raw_df()


    def _raw_data(self):
        return requests.get(
            f'https://api.gurufocus.com/public/user/{str(self.token)}/stock/{str(self.ticker)}/dividend').json()

    def _raw_df(self):
        div_list = self.raw_data
        div_df = pd.DataFrame(div_list)

        return div_df


class FinancialHistory:
    def __init__(self, **kwargs):
        self.token = kwargs.get('token', 'error')
        self.ticker = kwargs.get('ticker', 'error')
        self.raw_data = self._raw_data()
        self.raw_data_annuals = self._raw_data_annual()
        self.raw_data_quarterly = self._raw_data_quarterly()
        self.data_template_parameters = self._data_template_parameters()

    def _raw_data(self):
        return requests.get(
            f'https://api.gurufocus.com/public/user/{str(self.token)}/stock/{str(self.ticker)}/financials').json()

    def _raw_data_annual(self):
        data = self.raw_data
        return data['financials']['annuals']

    def _raw_data_quarterly(self):
        data = self.raw_data
        return data['financials']['quarterly']

    def _data_template_parameters(self):
        data = self.raw_data
        return data['financials']['financial_template_parameters']


class PriceHistory:

    def __init__(self, **kwargs):
        self.token = kwargs.get('token', 'error')
        self.ticker = kwargs.get('ticker', 'error')
        self.raw_data = self._raw_data()
        self.raw_df = self._raw_df()


    def _raw_data(self):
        return requests.get(
            f'https://api.gurufocus.com/public/user/{str(self.token)}/stock/{str(self.ticker)}/price').json()

    def _raw_df(self):
        price_list = self.raw_data
        price_df = pd.DataFrame(price_list, columns=['Date', 'PricePerShare'])

        return price_df

