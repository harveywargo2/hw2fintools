import os
import pandas as pd
from hw2fintools import mod_path


xlsx_path = os.path.join(mod_path, 'xlsx')


def get_df_stock_watch_list():
    df = pd.read_excel(os.path.join(xlsx_path, "stock_watch_list.xlsx"))
    return df

