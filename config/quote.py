from config import QUANTITY_UNIT, CURRENCY

## Below are related to Quote
QUOTE_TABLE = "Quotation"
QUOTE_PRODUCT_NAME = "Product Name"
QUOTE_DESCRIPTION = "Description"
QUOTE_QUANTITY = "QTY({quantity_unit})".format(quantity_unit=QUANTITY_UNIT)
QUOTE_UNIT_PRICE = "Unit FOB Price({currency})".format(currency=CURRENCY)
QUOTE_AMOUNT = "Amount({currency})".format(currency=CURRENCY)

QUOTE_HEADERS = [QUOTE_PRODUCT_NAME, QUOTE_DESCRIPTION, QUOTE_QUANTITY, QUOTE_UNIT_PRICE, QUOTE_AMOUNT]
QUOTE_TOTAL_AMOUNT = "Total amount"
QUOTE_DIGIT_ROUNDING = '.2f'