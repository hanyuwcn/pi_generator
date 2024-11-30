from output.pi_writer import PIWriter
from utils import writer_tools

import xlsxwriter
import os
import pandas as pd
import config


class BAGFilterMachinePIWriter(PIWriter):
    def __init__(self):
        super().__init__()
        self.worksheet = None
        self.row = None

    def write_to_output(self, header, quote, footer):
        if os.path.exists(config.PI_FILE_NAME):
            os.remove(config.PI_FILE_NAME)

        workbook = xlsxwriter.Workbook(config.PI_FILE_NAME)
        self.worksheet = workbook.add_worksheet()

        self.row = 0

        self.write_header(header)
        self.write_quote(quote)
        self.write_footer(footer)

        workbook.close()

    def write_header(self, header):
        print(header)
        self.worksheet.write(self.row, 0, header[config.INVOICE_TITLE])
        self.row += 1
        #
        self.worksheet.write(self.row, 0, header[config.INVOICE_RECIPIENT])
        self.row += 1

        self.worksheet.write(self.row, 0, header[config.INVOICE_ADDRESS])
        self.worksheet.write(self.row, 1, header[config.INVOICE_DATE])
        self.row += 1

        self.worksheet.write(self.row, 1, header[config.INVOICE_NO])
        self.row += 2

    def write_quote(self, quote):
        quote_df = quote[config.QUOTE_TABLE]
        self.write_quote_header(list(quote_df.columns))
        self.write_quote_content(quote_df.values.tolist())
        self.write_quote_total_amount(len(quote_df.columns), quote[config.QUOTE_TOTAL_AMOUNT])
        self.row += 1


    def write_footer(self, footer):
        print(footer)
        index = 1

        self.worksheet.write(self.row, 0, "{index}. {delivery_term}"
                             .format(index=index, delivery_term=footer[config.INVOICE_DELIVERY]))
        index += 1
        self.row += 1

        self.worksheet.write(self.row, 0, "{index}. {payment_terms}"
                             .format(index=index, payment_terms=footer[config.INVOICE_PAYMENT]))
        index += 1
        self.row += 1

        self.worksheet.write(self.row, 0, "{index}. {port_of_loading}"
                             .format(index=index, port_of_loading=footer[config.INVOICE_PORT]))
        index += 1
        self.row += 1

        self.worksheet.write(self.row, 0, "{index}. {producing_time}"
                             .format(index=index, producing_time=footer[config.INVOICE_PRODUCING_TIME]))
        index += 1
        self.row += 1

        self.worksheet.write(self.row, 0,
                             "{index}. {destination_port}"
                             .format(index=index, destination_port=footer[config.INVOICE_DESTINATION]))
        index += 1
        self.row += 1

        self.worksheet.write(self.row, 0,
                             "{index}. {transportation}".format(index=index,
                                                                         transportation=footer[config.INVOICE_TRANSPORTATION]))

    def write_quote_header(self, quote_headers):
        self.worksheet.write(self.row, 0, config.PI_INVOICE_INDEX)
        self.worksheet.write_row(self.row, 1, quote_headers)
        self.row += 1


    def write_quote_content(self, quote_content):
        index = 1
        for quote_item in quote_content:
            quote_item = ["N/A" if pd.isna(x) else x for x in quote_item]
            try:
                print(quote_item)
                self.worksheet.write(self.row, 0, index)
                self.worksheet.write_row(self.row, 1, quote_item)
                index += 1
                self.row += 1
            except:
                pass

    def write_quote_total_amount(self, col, total_amount):
        self.worksheet.write(self.row, col, writer_tools.translate_value_to_price(total_amount))
        self.row += 1


