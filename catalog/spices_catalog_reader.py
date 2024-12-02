from utils import reader_tools
from catalog import CatalogReader
from system import logger

import config
import traceback


class SpicesCatalogReader(CatalogReader):
    def read_catalog(self):
        try:
            logger.info("Start reading catalog...")

            df_catalog = reader_tools.read_excel_to_pandas(config.CATALOG_FILE_NAME)

            logger.info("Catalog successfully read.")

            return df_catalog
        except Exception as e:
            logger.error("Application collapse when reading the catalog!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")