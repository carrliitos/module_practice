import os, os.path

from utils import logger
from utils import connections
from utils import context

# current_file_path = os.path.abspath(__file__)
# current_dir = os.path.abspath(os.path.join(current_file_path, os.pardir))
# parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

directory = context.get_context(os.path.abspath(__file__))

logger_file = f"{directory}/logs/crc_screening.log"

def run():
    second_logger = logger.setup_logger("screening_logger", logger_file)
    second_logger.info("Extracing stuff for the CRC Screening Project")
    connections.clarity("Clarity")
    second_logger.error("Oh no! Something wrong happened")