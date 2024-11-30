from datetime import date

import math
import config
import re

def get_current_date():
    return str(date.today())

def generate_invoice_number():
    prefix = config.INVOICE_NO_PREFIX
    datefix = str(date.today().strftime("%y%m%d"))
    return prefix + datefix

def get_deposit(amount, deposit_percentage = config.DEPOSIT_PERCENTAGE):
    multiple = 1
    portion = amount * deposit_percentage

    while portion / multiple > 10:
        multiple *= 10

    return math.floor(portion / multiple) * multiple

def translate_string_to_price(price_str):
    return re.findall(r"\d+\.?\d*", price_str)[0]

def translate_value_to_price(value):
    # digit_value = format(value, config.QUOTE_DIGIT_ROUNDING)
    # ## (TODO) digit rounding to string is not compatible with thousands separation to string
    value = f'{round(value, config.ROUND_DIGITS):,}'
    return config.CURRENCY_SIGN + value
