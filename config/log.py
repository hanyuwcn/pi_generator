## Below are log related
from datetime import datetime

from config import PRODUCT

APPLICATION = "Performa_Invoice_Generator"
LOG_FILE_NAME = "log-{product}-{application}-{datetime}.log".format(product=PRODUCT, application=APPLICATION, datetime=datetime.now().strftime("%Y%m%d%H%M%S"))
LOG_FORMAT = "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
LOG_DATE_FORMAT = "%H:%M:%S"
