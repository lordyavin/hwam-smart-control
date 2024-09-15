import unittest
from assertpy import assert_that

from hwamsmartctrl.airbox import Airbox

class AriboxTest(unittest.TestCase):
    async def test_getStoveData(self):        
        aribox = Airbox("192.168.1.194")
        with aribox.getStoveData() as data:
            assert_that(data).contains_key("day")

    async def test_startCombustion(self):        
        aribox = Airbox("192.168.1.194")
        with aribox.startCombustion() as succeeded:
            assert_that(succeeded).is_true()
        with aribox.getStoveData() as data:
            assert_that(data).contains_entry(phase=0)
    
    async def test_setBurnLevel(self):        
        aribox = Airbox("192.168.1.194")
        with aribox.setBurnLevel(1) as succeeded:
            assert_that(succeeded).is_true()
        with aribox.getStoveData() as data:
            assert_that(data).contains_entry(level=1)

        with aribox.setBurnLevel(6) as succeeded:
            assert_that(succeeded).is_true()
    