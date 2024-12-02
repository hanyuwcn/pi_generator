import logging
import config

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(config.APPLICATION)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt=logging.Formatter(config.LOG_FORMAT))

file_handler = logging.FileHandler(config.LOG_FILE_NAME)
file_handler.setFormatter(fmt=logging.Formatter(config.LOG_FORMAT))

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
