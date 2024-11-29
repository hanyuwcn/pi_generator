from writer import write_to_file
from pricetag import BAGFilterMachinePricetagReader
from utils import reader_tools
from enquiry import BAGFilterMachineEnquiryReader

import config

from processor import BAGFilterMachineProcess


## (TODO) Add log that can export to an txt file
## (TODO) Add python documents to methods and classes

if __name__ == '__main__':
    # pricetag_df = BAGFilterMachinePricetagReader().read_pricetag()
    # print(pricetag_df)
    # print(target_column_value_in_dataframe(pricetag_df, "Product Name", "product A", "UNIT FOB PRICE "))

    # enquiry_reader = BAGFilterMachineEnquiryReader()
    # print(enquiry_reader.read_enquiry())

    # print(reader_tools.translate_string_to_price('5 USD'))


    process = BAGFilterMachineProcess()
    print(process.read_enquiry())
    print(process.read_pricetag())
    print(process.make_quote())
