import os

import pandas as pd
import config
from system import logger


def read_excel_to_pandas(file_name):
    """
    Read the file from the path to the dataframe.

    :param file_name: file name of the file, assuming to be placed in the same directory with the application
    :return: the dataframe
    """
    file_path = os.getcwd() + "/" + file_name + "."
    return pd.read_excel(file_path)


def target_column_value_in_dataframe(dataframe, key_column_name, key_column_value, value_column_name):
    """
    Find the target value in the table given the column and row information.

    :param dataframe: of the scenario
    :param key_column_name: of the required column name
    :param key_column_value: of the target column value
    :param value_column_name: of the column value that looks for
    :return:
    """
    target_df = dataframe.loc[dataframe[key_column_name] == key_column_value, [value_column_name]]
    return target_df[value_column_name].values[0]


def check_columns_existence(dataframe, name_df, critical_columns):
    """
    Check if the dataframe contains all given columns.

    :param dataframe: target dataframe
    :param name_df: name of the dataframe
    :param critical_columns: list of all target columns

    :return: the result of this checking
    """
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
