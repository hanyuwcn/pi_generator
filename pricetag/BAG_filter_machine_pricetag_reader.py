from utils import reader_tools
from pricetag import PricetagReader

import config


class BAGFilterMachinePricetagReader(PricetagReader):
    def read_pricetag(self):
        df_pricetag = reader_tools.read_excel_to_pandas(config.PRICETAG_FILE_NAME)
        return df_pricetag
