import pandas as pd
from datetime import datetime
import numpy as np


def div_hist_s1v1(csv_file_path):
    """Normalize GuruFocus Dividend History To Standard Schema

    :param
        csv_file_path: Path to csv file
    :return:
        Dataframe
    """

    div0 = pd.read_csv(csv_file_path, index_col=0)

    div1 = div0.rename(
        columns={'amount': 'DivAmount', 'type': 'DivType', 'currency': 'Currency', 'ex_date': 'ExDivDate',
                 'pay_date': 'DivPayDate', 'record_date': 'DivRecordDate'
                 }
    )

    div1['DivDeclareDate'] = np.nan
    div1['DivFrequency'] = np.nan
    div1['DivType'] = div1['DivType'].replace('Cash Div.', 'regular')
    div1['DivType'] = div1['DivType'].replace('Special Div.', 'special')
    div1['ExDivDate'] = pd.to_datetime(div1['ExDivDate'], errors='coerce')
    div1['DivRecordDate'] = pd.to_datetime(div1['DivRecordDate'], errors='coerce')
    div1['DivPayDate'] = pd.to_datetime(div1['DivPayDate'], errors='coerce')

    div2 = div1.loc[div1['DivType'] == 'regular']
    div2 = div2.set_index('ExDivDate')
    div2 = div2.groupby(div2.index.year).agg(YearCount=pd.NamedAgg(column='DivAmount', aggfunc='count'))
    ave_div = div2['YearCount'].mean()


    if ave_div < 1:
        div1['DivFrequency'] = 0

    elif ave_div > 1 and ave_div < 2:
        div1['DivFrequency'] = 1

    elif ave_div > 2 and ave_div < 3:
        div1['DivFrequency'] = 2

    elif ave_div > 3 and ave_div < 5:
        div1['DivFrequency'] = 4

    elif ave_div > 5 and ave_div < 12:
        div1['DivFrequency'] = 12

    else:
        div1['DivFrequency'] = 0


    return div1


def price_hist_s2v1(csv_file_path):
    """Normalized GuruFocus Price History To Standard Schema

    :param
        csv_file_path: Path to csv file
    :return:
        Dataframe
    """
    price0 = pd.read_csv(csv_file_path, index_col=0)
    price0['Date'] = pd.to_datetime(price0['Date'], errors='coerce')

    return price0


