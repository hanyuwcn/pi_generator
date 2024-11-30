from writer import write_to_file
from pricetag import BAGFilterMachinePricetagReader
from utils import reader_tools
from utils import writer_tools
from enquiry import BAGFilterMachineEnquiryReader
from output import BAGFilterMachinePIWriter, PIWriter
from header import BAGFilterMachineHeaderMaker
from footer import BAGFilterMachineFooterMaker
from quote import BAGFilterMachineQuoteMaker
import config

from processor import BAGFilterMachineProcess


## (TODO) Add log that can export to an txt file
## (TODO) Add python documents to methods and classes

if __name__ == '__main__':
    enquiry = BAGFilterMachineEnquiryReader().read_enquiry()
    pricetag = BAGFilterMachinePricetagReader().read_pricetag()

    print(BAGFilterMachineHeaderMaker().make_header())


    quote_maker = BAGFilterMachineQuoteMaker()
    quote_info = quote_maker.make_quote(enquiry, pricetag)

    info = {"amount": quote_info["total_amount"], "deposit_amount": writer_tools.get_deposit(quote_info["total_amount"])}
    footer_maker = BAGFilterMachineFooterMaker()
    print(footer_maker.make_footer(info))