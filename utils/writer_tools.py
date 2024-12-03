from datetime import date

import math
import config
import re

def get_current_date():
    return str(date.today())

def generate_invoice_number():
    prefix = config.INVOICE_NO_PREFIX
    datefix = str(date.today().strftime("%y%m%d"))
    return prefix + "-" + datefix

def get_deposit(amount, deposit_percentage = config.DEPOSIT_PERCENTAGE, makeup = True):
    """
    Get deposit amount from a quote

    :param amount: total amount
    :param deposit_percentage: percentage of deposit to total amount
    :param makeup: either the deposit would be some tens, hundreds number. This is NOT digit rounding
    :return:
    """
    if makeup:
        multiple = 1
        portion = amount * deposit_percentage

        while portion / multiple > 10:
            multiple *= 10

        return math.floor(portion / multiple) * multiple
    else:
        return round(amount * deposit_percentage, ndigits=config.ROUND_DIGITS)

def extract_number_from_string(str):
    number = re.findall(r"\d+\.?\d*", str)[0]
    return float(number)

def translate_value_to_price(value):
    ## (TODO) digit rounding to string is not compatible with thousands separation to string
    value = f'{round(value, config.ROUND_DIGITS):,}'
    return config.CURRENCY_SIGN + value