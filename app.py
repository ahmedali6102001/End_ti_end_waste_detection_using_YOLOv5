from wasteDetection.logger import logging
from wasteDetection.exception import AppException
import sys


logging.info("Welcome to my custom log")


try:
    x = 3/'s'

except Exception as e:
    raise AppException(e, sys)