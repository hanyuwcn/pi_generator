from quote import QuoteMaker
import config
import pandas as pd
import traceback
from utils import reader_tools, writer_tools
from system import logger


class SpicesQuoteMaker(QuoteMaker):
    def make_quote(self, enquiry_df, catalog_df):
        try:
            logger.info("Start making the quote...")

            catalog_columns = list(catalog_df.columns)   ## (TODO) Need to catch columns not exist error
            catalog_columns = [column_name for column_name in catalog_columns
                               if column_name not in config.CATALOG_DROP_COLUMNS]
            catalog_columns.extend([config.QUOTE_UNIT_PRICE, config.QUOTE_QUANTITY, config.QUOTE_AMOUNT])
            quote_df = pd.DataFrame(columns=catalog_columns)

            total_amount = 0.0

            for product_name in enquiry_df[config.ENQUIRY_PRODUCT_NAME].values:
                if product_name not in catalog_df[config.CATALOG_PRODUCT_NAME].values:
                    product_info = {config.QUOTE_PRODUCT_NAME: product_name}
                    logger.debug("{product_name} does not exist in the catalog.".format(product_name=product_name))
                else:
                    product_info = {config.QUOTE_PRODUCT_NAME: product_name}
                    for column in catalog_columns:
                        if column not in [config.QUOTE_PRODUCT_NAME,
                                          config.QUOTE_UNIT_PRICE,
                                          config.QUOTE_QUANTITY,
                                          config.QUOTE_AMOUNT]:
                            value = reader_tools.target_column_value_in_dataframe(
                                catalog_df, config.CATALOG_PRODUCT_NAME, product_name, column)
                            product_info[column] = value

                    unit_price = self._get_unit_price(catalog_df, product_name)
                    quantity = self._get_quantity(enquiry_df, product_name)
                    price = quantity * unit_price

                    total_amount += price
                    amount = writer_tools.translate_value_to_price(price)

                    product_info[config.QUOTE_UNIT_PRICE] = unit_price
                    product_info[config.QUOTE_QUANTITY] = quantity
                    product_info[config.QUOTE_AMOUNT] = amount

                quote_df.loc[len(quote_df)] = product_info

            logger.info("Quote successfully made.")
        except Exception as e:
            logger.error("Application collapse when making the quote!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

        return {config.QUOTE_TABLE: quote_df, config.QUOTE_TOTAL_AMOUNT: total_amount}

    @staticmethod
    def _get_unit_price(catalog_df, product_name):
        unit_price_value = reader_tools.target_column_value_in_dataframe(
            catalog_df, config.CATALOG_PRODUCT_NAME, product_name, config.CATALOG_UNIT_PRICE)
        if pd.isna(unit_price_value):
            logger.warning("{product_name}'s price is missing!".format(product_name=product_name))
            unit_price = 0
        else:
            unit_price = writer_tools.extract_number_from_string(str(unit_price_value))
        return unit_price

    @staticmethod
    def _get_quantity(enquiry_df, product_name):
        quantity_value = reader_tools.target_column_value_in_dataframe(enquiry_df, config.ENQUIRY_PRODUCT_NAME,
                                                                 product_name, config.ENQUIRY_QUANTITY)

        if pd.isna(quantity_value):
            quantity_value = config.ENQUIRY_DEFAULT_QUANTITY
        unit_price = writer_tools.extract_number_from_string(str(quantity_value))
        return unit_price
