import pytest
import time

@pytest.fixture(autouse=True)
def wait_between_tests():

    yield

    time.sleep(5)
