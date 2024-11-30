from output.pi_writer import PIWriter
from utils import writer_tools

import xlsxwriter
import config





class BAGFilterMachinePIWriter(PIWriter):
    def write_to_output(self, header, quote, footer):
        ## (TODO) to remove duplication
        workbook = xlsxwriter.Workbook(config.PI_FILE_NAME)
        self.worksheet = workbook.add_worksheet()

        self.row = 0
        self.column = 0

        self.write_header()
        self.write_quote()
        self.write_footer()

        workbook.close()

    def write_header(self, header):
        self.worksheet.write(self.row, self.column, config.INVOICE_TITLE)
        self.row += 1

        self.worksheet.write(self.row, self.column, config.INVOICE_RECIPIENT)
        self.row += 1

        self.worksheet.write(self.row, self.column, config.INVOICE_ADDRESS)
        self.worksheet.write(self.row, self.column + 1, config.INVOICE_DATE + writer_tools.get_current_date())
        self.row += 1

        self.worksheet.write(self.row, self.column + 1, config.INVOICE_NO + writer_tools.generate_invoice_number())
        self.row += 2

    def write_quote(self, quote):
        pass

    def write_footer(self, footer):
        pass

