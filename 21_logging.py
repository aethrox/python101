# Logging
import logging

# Security Levels
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("1nnr3d Logger")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug message!")
logger.info("This is important information!")
