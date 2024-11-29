import os
import re

import pandas as pd

def read_excel_to_pandas(file_name):
    file_path = os.getcwd() + "/" + file_name + "."
    return pd.read_excel(file_path)

def read_excel_to_list(file_name):
    file_path = os.getcwd() + "/" + file_name + "."

def target_column_value_in_dataframe(dataframe, key_column_name, key_column_value, value_column_name):
    target_df = dataframe.loc[dataframe[key_column_name] == key_column_value, [value_column_name]]
    return target_df.iloc[0]

def translate_string_to_price(price_str):
    return re.findall(r"\d+\.?\d*", price_str)

