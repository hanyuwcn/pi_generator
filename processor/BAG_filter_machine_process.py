import pandas as pd

from processor import Process
from enquiry import BAGFilterMachineEnquiryReader
from pricetag import BAGFilterMachinePricetagReader
from output import BAGFilterMachinePIWriter

from utils import reader_tools

import config

class BAGFilterMachineProcess(Process):
    def __init__(self):
        super().__init__()
        self.enquiry_reader = BAGFilterMachineEnquiryReader()
        self.pricetag_reader = BAGFilterMachinePricetagReader()
        self.pi_writer = BAGFilterMachinePIWriter()

    def make_header(self):
        pass

    def make_quote(self):
        enquiry_df = self.enquiry_reader.read_enquiry()
        pricetag_df = self.pricetag_reader.read_pricetag()

        quote_df = pd.DataFrame(columns=config.QUOTE_HEADERS)
        for product_name in enquiry_df[config.ENQUIRY_PRODUCT_NAME]:
            # description = reader_tools.target_column_value_in_dataframe(pricetag_df, config.PRICETAG_PRODUCT_NAME, product_name, config.PRICETAG_DESCRIPTION)
            # unit_price = reader_tools.translate_string_to_price(reader_tools.target_column_value_in_dataframe(pricetag_df, config.PRICETAG_PRODUCT_NAME, product_name, config.PRICETAG_UNIT_PRICE)[0])
            #
            # quantity = reader_tools.translate_string_to_price(reader_tools.target_column_value_in_dataframe(enquiry_df, config.ENQUIRY_PRODUCT_NAME, product_name, config.ENQUIRY_QUANTITY).values)
            # amount = round(quantity * unit_price, config.QUOTE_DIGIT_ROUNDING)

            description = "description of " + product_name
            unit_price = 5.0
            quantity = 1
            amount = round(quantity * unit_price, config.QUOTE_DIGIT_ROUNDING)

            ## (TODO) Add an index
            ## (TODO) QTY has unit (set), should specify singularity and plurality
            ## (TODO) Unit FOB Price has unit
            ## (TODO) Amount has unit
            ## (TODO) Amount has a dollar sign like $500.00
            ## (TODO) price should have a 3 digit separation like 3'000.00



            product_info = {config.QUOTE_PRODUCT_NAME: product_name,
                             config.QUOTE_DESCRIPTION: description,
                             config.QUOTE_QUANTITY: quantity,
                             config.QUOTE_UNIT_PRICE: unit_price,
                             config.QUOTE_AMOUNT: amount}

            quote_df.loc[len(quote_df)] = product_info

        return quote_df

    def make_footer(self):
        pass

    def write_to_output(self):
        pass