from quote import QuoteMaker
import config
import pandas as pd
import traceback
from utils import reader_tools, writer_tools, logger


class SpicesQuoteMaker(QuoteMaker):
    def make_quote(self, enquiry, pricetag):
        try:
            logger.info("Start making the quote...")

            reader_tools.fill_empty_quantity(enquiry, value=1)

            quote_df = pd.DataFrame(columns=config.QUOTE_HEADERS)
            total_amount = 0.0

            for product_name in enquiry[config.ENQUIRY_PRODUCT_NAME].values:
                if product_name not in pricetag[config.PRICETAG_PRODUCT_NAME].values:
                    product_info = {config.QUOTE_PRODUCT_NAME: product_name}
                else:
                    description = reader_tools.target_column_value_in_dataframe(pricetag, config.PRICETAG_PRODUCT_NAME,
                                                                                product_name, config.PRICETAG_DESCRIPTION)
                    unit_price = writer_tools.translate_string_to_price(
                        reader_tools.target_column_value_in_dataframe(pricetag, config.PRICETAG_PRODUCT_NAME, product_name,
                                                                      config.PRICETAG_UNIT_PRICE))
                    quantity = reader_tools.target_column_value_in_dataframe(enquiry, config.ENQUIRY_PRODUCT_NAME,
                                                                             product_name, config.ENQUIRY_QUANTITY)
                    value = quantity * float(unit_price)

                    total_amount += value
                    amount = writer_tools.translate_value_to_price(value)

                    product_info = {config.QUOTE_PRODUCT_NAME: product_name,
                                    config.QUOTE_DESCRIPTION: description,
                                    config.QUOTE_QUANTITY: quantity,
                                    config.QUOTE_UNIT_PRICE: unit_price,
                                    config.QUOTE_AMOUNT: amount}

                quote_df.loc[len(quote_df)] = product_info

            logger.info("Quote successfully made.")
        except Exception as e:
            logger.error("Application collapse when reading the catalog!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

        return {config.QUOTE_TABLE: quote_df, config.QUOTE_TOTAL_AMOUNT: total_amount}
