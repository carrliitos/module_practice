import os, os.path

from utils import logger
from utils import context

# current_file_path = os.path.abspath(__file__)
# current_dir = os.path.abspath(os.path.join(current_file_path, os.pardir))
# parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

directory = context.get_context(os.path.abspath(__file__))

logger_file = f"{directory}/logs/connections.log"

def clarity(connection_name):
    connection_logger = logger.setup_logger("connections_log", logger_file)
    connection_logger.info(f"Connecting to {connection_name}")
    connection_logger.debug(f"Debug logging to {connection_name}")