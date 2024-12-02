from enquiry import EnquiryReader
from utils import reader_tools
from system import logger


import config
import traceback

class SpicesEnquiryReader(EnquiryReader):
    def read_enquiry(self):
        try:
            logger.info("Start reading enquiry...")

            enquiry = reader_tools.read_excel_to_pandas(config.ENQUIRY_FILE_NAME)

            logger.info("Enquiry successfully read.")

            return enquiry
        except Exception as e:
            logger.error("Application collapse when reading the enquiry!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")