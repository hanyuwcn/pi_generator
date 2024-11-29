from enquiry import EnquiryReader
from utils.reader_tools import read_excel_to_pandas

import config


class BAGFilterMachineEnquiryReader(EnquiryReader):
    def read_enquiry(self):
        self.df_enquiry = read_excel_to_pandas(config.ENQUIRY_FILE_NAME)
        self.fill_empty_quantity()
        return self.df_enquiry

    def fill_empty_quantity(self, value = 1):
        self.df_enquiry.fillna({config.ENQUIRY_QUANTITY: value}, inplace=True)
