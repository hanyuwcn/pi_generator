## Below are log related
from datetime import datetime
from config import PRODUCT

APPLICATION = "Performa Invoice Generator"
LOG_FILE_NAME = "log-{product}-{application}-{datetime}.log".format(product=PRODUCT, application=APPLICATION, datetime=datetime.now().strftime("%Y%m%d%H%M%S"))
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"