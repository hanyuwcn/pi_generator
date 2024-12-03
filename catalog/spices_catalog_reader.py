from utils import reader_tools
from catalog import CatalogReader
from system import logger

import config
import traceback


class SpicesCatalogReader(CatalogReader):
    def read_catalog(self):
        try:
            logger.info("Start reading catalog...")

            self.df_catalog = reader_tools.read_excel_to_pandas(config.CATALOG_FILE_NAME)

            logger.info("Catalog successfully read.")

            if not self.validate():
                logger.warning("{catalog_df} is not valid.".format(catalog_df=config.CATALOG_DATAFRAME_NAME))

            return self.df_catalog
        except FileNotFoundError as file_not_found_error:
            logger.error("Can NOT find [{catalog_file_name}]!".format(catalog_file_name=config.CATALOG_FILE_NAME))
            logger.error(f"{file_not_found_error.__class__}, occur_error: {traceback.format_exc()}")
        except Exception as e:
            logger.error("Application collapse when reading the catalog!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    def validate(self):
        return reader_tools.check_columns(dataframe=self.df_catalog,
                                          name_df=config.CATALOG_DATAFRAME_NAME,
                                          critical_columns=config.CATALOG_CRITICAL_COLUMNS)

