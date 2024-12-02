from config import QUANTITY_UNIT, CURRENCY

## Below are related to Quote
QUOTE_TABLE = "Quotation"
QUOTE_PRODUCT_NAME = "Product"
QUOTE_DESCRIPTION = "Description"
QUOTE_QUANTITY = "QTY({quantity_unit})".format(quantity_unit=QUANTITY_UNIT)
QUOTE_UNIT_PRICE = "Unit FOB Price({currency})".format(currency=CURRENCY)
QUOTE_AMOUNT = "Amount({currency})".format(currency=CURRENCY)

QUOTE_TOTAL = "Total"
QUOTE_TOTAL_AMOUNT = "Total amount"
QUOTE_DIGIT_ROUNDING = '.2f'