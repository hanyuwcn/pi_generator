from header import HeaderMaker
import config
from utils import writer_tools

class BAGFilterMachineHeaderMaker(HeaderMaker):
    def make_header(self):
        header = config.INVOICE_TITLE
        recipient = config.INVOICE_RECIPIENT + ":"
        address = config.INVOICE_ADDRESS + ":"
        date = "{date_title}: {date}".format(date_title=config.INVOICE_DATE, date=writer_tools.get_current_date())
        number = "{invoice_number_title}: {invoice_number}".format(invoice_number_title=config.INVOICE_NO, invoice_number=writer_tools.generate_invoice_number())

        return {config.INVOICE_TITLE: header,
                config.INVOICE_RECIPIENT: recipient,
                config.INVOICE_ADDRESS: address,
                config.INVOICE_DATE: date,
                config.INVOICE_NO: number}  ## (TODO) set this dictionary static into configurations