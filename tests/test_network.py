from firmware.firmware import Firmware
from utils.logger import logger

fw = Firmware()

def test_network():

    logger.info("Starting Network Test")

    assert fw.network_status() == "CONNECTED"

    logger.info("Network Test Passed")
