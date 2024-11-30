from enquiry import EnquiryReader
from utils.reader_tools import read_excel_to_pandas

import config


class BAGFilterMachineEnquiryReader(EnquiryReader):
    def read_enquiry(self):
        return read_excel_to_pandas(config.ENQUIRY_FILE_NAME)
