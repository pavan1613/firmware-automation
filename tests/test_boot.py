from firmware.firmware import Firmware
from utils.logger import logger

fw = Firmware()

def test_boot():

    logger.info("Starting Boot Test")

    assert fw.boot() is True

    logger.info("Boot Test Passed")
