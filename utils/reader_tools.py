import os

import pandas as pd
import config
from system import logger

def read_excel_to_pandas(file_name):
    file_path = os.getcwd() + "/" + file_name + "."
    return pd.read_excel(file_path)

def read_excel_to_list(file_name):
    file_path = os.getcwd() + "/" + file_name + "."

def target_column_value_in_dataframe(dataframe, key_column_name, key_column_value, value_column_name):
    target_df = dataframe.loc[dataframe[key_column_name] == key_column_value, [value_column_name]]
    return target_df[value_column_name].values[0]

def fill_empty_quantity(df, value = 1):
        df.fillna({config.ENQUIRY_QUANTITY: value}, inplace=True)


def check_columns(dataframe, name_df, critical_columns):
    valid = True

    header_dataframe = list(dataframe.head())
    for column_name in critical_columns:
        if column_name not in header_dataframe:
            valid = False

            logger.warning("[{column_name}] is required to proceed but is not found in {name_df}.".format(
                column_name=column_name,
                name_df=name_df
            ))

    if valid:
        logger.debug("All critical columns exist in {name_df}.".format(name_df=name_df))

    return valid