from renderer_pypi.logger import logger
from renderer_pypi.custom_exception import InvalidURLException

# logger.info("This is an info message.")
try:
    raise InvalidURLException("Custom invalid URL exception triggered.")
except InvalidURLException as e:
    logger.error(f"Caught an exception: {e}")