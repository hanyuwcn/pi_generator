from enquiry import EnquiryReader
from utils import reader_tools
from system import logger

import config
import traceback


class SpicesEnquiryReader(EnquiryReader):
    def read_enquiry(self):
        """
        Read Enquiry from file into a dataframe;
        also check some default rules for these columns(e.g. containing critical columns).

        :return: a dataframe of Enquiry
        """
        try:
            logger.info("Start reading enquiry...")

            self.enquiry_df = reader_tools.read_excel_to_pandas(config.ENQUIRY_FILE_NAME)

            logger.info("Enquiry successfully read.")

            if not self.validate():
                logger.warning("{enquiry_df} is not valid.".format(enquiry_df=config.ENQUIRY_DATAFRAME_NAME))

            return self.enquiry_df
        except FileNotFoundError as file_not_found_error:
            logger.error("Can NOT find [{enquiry_file_name}]!".format(enquiry_file_name=config.ENQUIRY_FILE_NAME))
            logger.error(f"{file_not_found_error.__class__}, occur_error: {traceback.format_exc()}")
        except Exception as e:
            logger.error("Application collapse when reading the enquiry!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    def validate(self):
        """
        :return: whether the Catalog is valid
        """
        return reader_tools.check_columns(dataframe=self.enquiry_df,
                                          name_df=config.ENQUIRY_DATAFRAME_NAME,
                                          critical_columns=config.ENQUIRY_CRITICAL_COLUMNS)
