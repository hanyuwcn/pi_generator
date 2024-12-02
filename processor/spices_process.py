from processor import Processor
from enquiry import SpicesEnquiryReader
from catalog import SpicesCatalogReader
from header import SpicesHeaderMaker
from footer import SpicesFooterMaker
from quote import SpicesQuoteMaker
from output import SpicesPIWriter

from utils import writer_tools
from system import logger

import traceback

import config

class SpicesProcessor(Processor):
    def __init__(self):
        try:
            logger.debug("Launching all modules for the process.")

            super().__init__()
            self.enquiry_reader = SpicesEnquiryReader()
            self.catalog_reader = SpicesCatalogReader()
            self.header_maker = SpicesHeaderMaker()
            self.footer_maker = SpicesFooterMaker()
            self.quote_maker = SpicesQuoteMaker()
            self.pi_writer = SpicesPIWriter()

            logger.debug("All modules launched.")
        except Exception as e:
            logger.error("Application collapse when attempting to launch modules!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    def make_footer(self):
        total_amount = self.quote[config.QUOTE_TOTAL_AMOUNT]
        deposit = writer_tools.get_deposit(total_amount, rounding=False)

        self.footer = self.footer_maker.make_footer(
            {config.QUOTE_TOTAL_AMOUNT: total_amount, config.DEPOSIT_HEADER: deposit})

    def process(self):
        self.read_catalog()
        self.read_enquiry()
        self.make_header()
        self.make_quote()
        self.make_footer()
        self.write_to_output()