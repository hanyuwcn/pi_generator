from output import PIWriter
from utils import writer_tools
from system import logger

import xlsxwriter
import os
import pandas as pd
import config
import traceback


class SpicesPIWriter(PIWriter):
    def __init__(self):
        super().__init__()
        self.worksheet = None
        self.row = None

    def write_to_output(self, header, quote, footer):
        try:
            if os.path.exists(config.PI_FILE_NAME):
                logger.info("{pi_file} already existed.".format(pi_file=config.PI_FILE_NAME))
                logger.info("{pi_file} is being replaced with new version.".format(pi_file=config.PI_FILE_NAME))
                os.remove(config.PI_FILE_NAME)
        except Exception as e:
            logger.error("Application collapse when attempting to remove existing file!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

        try:
            logger.info("Start creating an Excel workbook/worksheet!")

            workbook = xlsxwriter.Workbook(config.PI_FILE_NAME)
            self.worksheet = workbook.add_worksheet()

            logger.info("[{file}] successfully created.".format(file=config.PI_FILE_NAME))
        except Exception as e:
            logger.error("Application collapse when creating an Excel workbook/worksheet!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

        logger.info("Start writing invoice into Excel worksheet.")

        self.row = 0

        self.write_header(header)
        self.write_quote(quote)
        self.write_footer(footer)

        workbook.close()
        logger.info("Invoice successfully wrote into Excel worksheet.")

    def write_header(self, header):
        try:
            logger.debug("Start writing headers into Excel worksheet.")

            self.worksheet.write(self.row, 0, header[config.INVOICE_TITLE])
            self.row += 1

            self.worksheet.write(self.row, 0, header[config.INVOICE_BUYER])
            self.worksheet.write(self.row, 1, header[config.INVOICE_NO])
            self.row += 1

            self.worksheet.write(self.row, 0, header[config.INVOICE_SELLER])
            self.worksheet.write(self.row, 1, header[config.INVOICE_DATE])
            self.row += 2

            logger.debug("Headers successfully wrote into Excel worksheet.")
        except Exception as e:
            logger.error("Application collapse when writing headers into worksheet!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    def write_quote(self, quote):
        try:
            logger.debug("Start writing quote into Excel worksheet.")

            quote_df = quote[config.QUOTE_TABLE]
            self.write_quote_header(list(quote_df.columns))
            self.write_quote_content(quote_df.values.tolist())
            self.write_quote_total_amount(len(quote_df.columns), quote[config.QUOTE_TOTAL_AMOUNT])
            self.row += 1

            logger.debug("Quote successfully wrote into Excel worksheet.")
        except Exception as e:
            logger.error("Application collapse when writing quote into worksheet!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    def write_footer(self, footer):
        try:
            logger.debug("Start writing footers into Excel worksheet...")

            self.worksheet.write(self.row, 0, footer[config.INVOICE_TOTAL_PRICE_TITLE])
            self.row += 1

            self.worksheet.write(self.row, 0, footer[config.DEPOSIT_HEADER])
            self.row += 1

            self.worksheet.write(self.row, 0, "{remark}:".format(remark=config.REMARK_TITLE))
            self.row += 1

            self._write_items_with_index([footer[config.INVOICE_PACKING_TITLE],
                                          footer[config.INVOICE_PAYMENT_TITLE],
                                          footer[config.INVOICE_PORT_TITLE],
                                          footer[config.INVOICE_DELIVERY_TIME_TITLE],
                                          footer[config.INVOICE_DESTINATION_TITLE],
                                          footer[config.INVOICE_INSURANCE_TITLE],
                                          footer[config.INVOICE_TRANSPORTATION_TITLE]])

            logger.debug("Footers successfully wrote into Excel worksheet.")
        except Exception as e:
            logger.error("Application collapse when writing footers into worksheet!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    def write_quote_header(self, quote_headers):
        self.worksheet.write(self.row, 0, config.PI_INVOICE_INDEX)
        self.worksheet.write_row(self.row, 1, quote_headers)
        self.row += 1

    def write_quote_content(self, quote_content):
        index = 1
        for quote_item in quote_content:
            quote_item = ["N/A" if pd.isna(x) else x for x in quote_item]
            try:
                logger.debug("Start writing quote into Excel worksheet...")

                self.worksheet.write(self.row, 0, index)
                self.worksheet.write_row(self.row, 1, quote_item)
                index += 1
                self.row += 1

                logger.debug("Quote successfully wrote into Excel worksheet.")
            except Exception as e:
                logger.error("Application collapse when writing quote into worksheet!")
                logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    def write_quote_total_amount(self, col, total_amount):
        self.worksheet.write(self.row, 0, config.QUOTE_TOTAL)
        self.worksheet.write(self.row, col, writer_tools.translate_value_to_price(total_amount))
        self.row += 1

    def _write_items_with_index(self, items):
        index = 1
        for item in items:
            self.worksheet.write(self.row, 0, "{index}. {item}".format(index=index, item=item))
            self.row += 1
            index += 1
