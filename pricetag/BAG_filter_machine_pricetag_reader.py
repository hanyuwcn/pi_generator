from utils.reader_tools import read_excel_to_pandas

from pricetag import PricetagReader

import config


class BAGFilterMachinePricetagReader(PricetagReader):
    def read_pricetag(self):
        df_pricetag = read_excel_to_pandas(config.PRICETAG_FILE_NAME)
        return df_pricetag
