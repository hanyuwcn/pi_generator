from header import HeaderMaker
from utils import writer_tools

import config
import traceback
from system import logger

class SpicesHeaderMaker(HeaderMaker):
    def make_header(self):
        try:
            logger.info("Start making header...")

            header = config.INVOICE_TITLE
            buyer = config.INVOICE_BUYER + ":"
            seller = config.INVOICE_SELLER + ":"
            date = "{date_title}: {date}".format(date_title=config.INVOICE_DATE, date=writer_tools.get_current_date())
            number = "{invoice_number_title}: {invoice_number}".format(invoice_number_title=config.INVOICE_NO, invoice_number=writer_tools.generate_invoice_number())

            logger.info("Header successfully made.")

            return {config.INVOICE_TITLE: header,
                    config.INVOICE_BUYER: buyer,
                    config.INVOICE_SELLER: seller,
                    config.INVOICE_DATE: date,
                    config.INVOICE_NO: number}  ## (TODO) set this dictionary static into configurations
        except Exception as e:
            logger.error("Application collapse when making the header!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")