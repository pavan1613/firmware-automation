from firmware.firmware import Firmware
from utils.logger import logger

fw = Firmware()

def test_memory():

    logger.info("Starting Memory Test")

    assert fw.memory_check() == 1024

    logger.info("Memory Test Passed")
