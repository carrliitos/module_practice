import os, os.path

from utils import logger
from utils import connections
from utils import context

# current_file_path = os.path.abspath(__file__)
# current_dir = os.path.abspath(os.path.join(current_file_path, os.pardir))
# parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

directory = context.get_context(os.path.abspath(__file__))

logger_file = f"{directory}/logs/htn_bp_col.log"

def run():
    first_logger = logger.setup_logger("first_logger", logger_file)
    first_logger.info("This is an info message")
    connections.clarity("Benzon")
    first_logger.debug("Another logger")
