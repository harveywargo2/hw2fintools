import pandas as pd
from datetime import datetime
import numpy as np


def annual_fin_hist_s5v1(fin_file_path, param_file_path):

    fin_df0 = pd.read_csv(fin_file_path, index_col=0)
    param_df = pd.read_csv(param_file_path, index_col=0).T
    fy_pattern = r"([\d]{4})-"
    month_pattern = r"-([\d]{2})"
    reit = param_df.loc['0', 'REITs']

    fin_df1 = pd.DataFrame()
    fin_df1['FiscalYearMonth'] = fin_df0['Fiscal Year']
    fin_df1['FiscalYear'] = fin_df0['Fiscal Year'].str.extract(fy_pattern)
    fin_df1['FiscalYear'] = pd.to_numeric(fin_df1['FiscalYear'], errors='coerce')
    fin_df1['FiscalMonth'] = fin_df0['Fiscal Year'].str.extract(month_pattern)
    fin_df1['FiscalMonth'] = pd.to_numeric(fin_df1['FiscalMonth'], errors='coerce')

    # Income Statement
    fin_df1['Revenue'] = pd.to_numeric(fin_df0['income_statement.Revenue'], errors='coerce')
    fin_df1['COGS'] = pd.to_numeric(fin_df0['income_statement.Cost of Goods Sold'], errors='coerce')
    fin_df1['GrossProfit'] = pd.to_numeric(fin_df0['income_statement.Gross Profit'], errors='coerce')
    fin_df1['R&D'] = pd.to_numeric(fin_df0['income_statement.Research & Development'], errors='coerce')
    fin_df1['OperatingIncome'] = pd.to_numeric(fin_df0['income_statement.Operating Income'], errors='coerce')
    fin_df1['InterestExpense'] = pd.to_numeric(fin_df0['income_statement.Interest Expense'], errors='coerce')
    fin_df1['InterestIncomeNet'] = pd.to_numeric(fin_df0['income_statement.Net Interest Income'], errors='coerce')
    fin_df1['IncomeTax'] = pd.to_numeric(fin_df0['income_statement.Tax Provision'], errors='coerce')
    fin_df1['IncomeFromContinuingOperations'] = pd.to_numeric(
        fin_df0['income_statement.Net Income (Continuing Operations)'], errors='coerce')
    fin_df1['NetIncome'] = pd.to_numeric(fin_df0['income_statement.Net Income'], errors='coerce')

    ## Balance Sheet
    fin_df1['C&E'] = pd.to_numeric(fin_df0['balance_sheet.Cash and Cash Equivalents'], errors='coerce')
    fin_df1['STI'] = pd.to_numeric(fin_df0['balance_sheet.Marketable Securities'], errors='coerce')
    fin_df1['Receivables'] = pd.to_numeric(fin_df0['balance_sheet.Marketable Securities'], errors='coerce')
    fin_df1['TreasuryStock'] = pd.to_numeric(fin_df0['balance_sheet.Treasury Stock'], errors='coerce')

    fin_df1['Goodwill'] = pd.to_numeric(fin_df0['balance_sheet.Goodwill'], errors='coerce')
    fin_df1['GrossPPE'] = pd.to_numeric(fin_df0['balance_sheet.Gross Property, Plant and Equipment'], errors='coerce')
    fin_df1['NetPPE'] = pd.to_numeric(fin_df0['balance_sheet.Property, Plant and Equipment'], errors='coerce')
    fin_df1['CurrentAssets'] = pd.to_numeric(fin_df0['balance_sheet.Total Current Assets'], errors='coerce')
    fin_df1['TotalAssets'] = pd.to_numeric(fin_df0['balance_sheet.Total Assets'], errors='coerce')

    fin_df1['ShortDebt'] = pd.to_numeric(fin_df0['balance_sheet.Short-Term Debt'], errors='coerce')
    fin_df1['LongDebt'] = pd.to_numeric(fin_df0['balance_sheet.Long-Term Debt'], errors='coerce')
    fin_df1['CurrentLiabilities'] = pd.to_numeric(fin_df0['balance_sheet.Total Current Liabilities'], errors='coerce')
    fin_df1['TotalLiabilities'] = pd.to_numeric(fin_df0['balance_sheet.Total Liabilities'], errors='coerce')

    ## Free Cash Flow
    fin_df1['Depreciation'] = pd.to_numeric(
        fin_df0['cashflow_statement.Cash Flow Depreciation, Depletion and Amortization'], errors='coerce')
    fin_df1['OpCash'] = pd.to_numeric(fin_df0['cashflow_statement.Cash Flow from Operations'], errors='coerce')

    fin_df1['CAPEX'] = pd.to_numeric(fin_df0['cashflow_statement.Capital Expenditure'], errors='coerce')
    fin_df1['FreeCash'] = pd.to_numeric(fin_df0['cashflow_statement.Free Cash Flow'], errors='coerce')

    fin_df1['DebtIssue'] = pd.to_numeric(fin_df0['cashflow_statement.Issuance of Debt'], errors='coerce')
    fin_df1['DebtRepaid'] = pd.to_numeric(fin_df0['cashflow_statement.Payments of Debt'], errors='coerce')

    fin_df1['StockIssue'] = pd.to_numeric(fin_df0['cashflow_statement.Issuance of Stock'], errors='coerce')
    fin_df1['StockBuyBack'] = pd.to_numeric(fin_df0['cashflow_statement.Repurchase of Stock'], errors='coerce')
    fin_df1['DivCash'] = pd.to_numeric(fin_df0['cashflow_statement.Cash Flow for Dividends'], errors='coerce')

    ## Supplemental
    fin_df1['SharesOutstandingEOP'] = pd.to_numeric(fin_df0['valuation_and_quality.Shares Outstanding (EOP)'],
                                                    errors='coerce')
    fin_df1['SharesOutstandingBasic'] = pd.to_numeric(
        fin_df0['valuation_and_quality.Shares Outstanding (Basic Average)'], errors='coerce')
    fin_df1['SharesOutstandingDiluted'] = pd.to_numeric(
        fin_df0['per_share_data_array.Shares Outstanding (Diluted Average)'], errors='coerce')

    ## Per Share Data
    fin_df1['RevPS'] = pd.to_numeric(fin_df0['per_share_data_array.Revenue per Share'], errors='coerce')
    fin_df1['EarnPS'] = pd.to_numeric(fin_df0['per_share_data_array.Earnings per Share (Diluted)'], errors='coerce')
    fin_df1['FreeCashPS'] = pd.to_numeric(fin_df0['per_share_data_array.Free Cash Flow per Share'], errors='coerce')
    fin_df1['OpCashPS'] = pd.to_numeric(fin_df0['per_share_data_array.Operating Cash Flow per Share'], errors='coerce')
    fin_df1['DivPS'] = pd.to_numeric(fin_df0['per_share_data_array.Dividends per Share'], errors='coerce')

    fin_df1['HighPrice'] = pd.to_numeric(fin_df0['valuation_and_quality.Highest Stock Price'], errors='coerce')
    fin_df1['LowPrice'] = pd.to_numeric(fin_df0['valuation_and_quality.Lowest Stock Price'], errors='coerce')

    final_df = fin_df1.copy()

    return final_df


def div_hist_s1v1(div_file_path):
    """Normalize GuruFocus Dividend History To Standard Schema

    :param
        csv_file_path: Path to csv file
    :return:
        Dataframe
    """

    div0 = pd.read_csv(div_file_path, index_col=0)

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


def price_hist_s2v1(price_file_path):
    """Normalized GuruFocus Price History To Standard Schema

    :param
        csv_file_path: Path to csv file
    :return:
        Dataframe
    """
    price0 = pd.read_csv(price_file_path, index_col=0)
    price0['Date'] = pd.to_datetime(price0['Date'], errors='coerce')

    return price0


