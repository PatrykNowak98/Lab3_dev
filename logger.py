import logging

def get_logs(level, format_string):
    logging.basicConfig(level=level, format=format_string)
    return logging

logger = get_logs(logging.DEBUG, '%(asctime)s - %(levelname)s - %(message)s')
logger.debug("You are debugging the code.")
logger.info("Information = platypuses sweat with milk.")
logger.error("An error has occured!")
logger.warning("WARNING! Somone has entered!")
