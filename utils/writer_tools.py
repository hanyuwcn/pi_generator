from datetime import date

import math
import config
import re


def get_current_date():
    """
    :return: the current date
    """
    return str(date.today())


def generate_invoice_number():
    """
    Make up the Invoice number of the given format.

    :return: the made up Invoice number
    """
    return f"{config.INVOICE_NO_PREFIX}-{str(date.today().strftime("%y%m%d"))}"


def get_deposit(amount, deposit_percentage=config.DEPOSIT_PERCENTAGE, makeup=True):
    """
    Get deposit amount from a quote.

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
    """
    Extract numeric string from a given string.

    :param str: given string that contains ONLY ONE number. Sample valid inputs: "6.0", "$10", "10.5 each"
    :return: a float in the string. Sample output from above examples: 6.0, 10.0, 10.5
    """
    number = re.findall(r"\d+\.?\d*", str)[0]
    return float(number)


def translate_value_to_price(value):
    """
    Translate the numeric value to a price format.

    :param value: in numeric type
    :return: the price format of the numeric value
    """
    ## (TODO) digit rounding to string is not compatible with thousands separation to string
    value = f'{round(value, config.ROUND_DIGITS):,}'
    return config.CURRENCY_SIGN + value
