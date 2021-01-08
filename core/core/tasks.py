from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
def add(x, y):
    logger.info("HELLO THERE!")
    time.sleep(10)
    return x + y
