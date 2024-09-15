import datetime
import unittest
from assertpy import assert_that
from unittest.mock import Mock
from hwamsmartctrl import airbox
from hwamsmartctrl.airbox import Airbox
import aiohttp 
import json

class AriboxTest(unittest.TestCase):
    async def setUp(self):
        self.airbox = airbox.connect("192.168.1.194")
    
    async def test_determineHostname(self):
        with self.airbox.determineHostname() as name:
            assert_that(name).contains_key("ihs_82646f88f3c3")

    async def test_getStoveData(self):
        with self.airbox.getStoveData() as data:
            assert_that(data).contains_key("day")

    async def test_startCombustion(self):        
        with self.airbox.startCombustion() as succeeded:
            assert_that(succeeded).is_true()
        with self.airbox.getStoveData() as data:
            assert_that(data).contains_entry(phase=0)
    
    async def test_setBurnLevel(self):
        assert_that(self.airbox.setBurnLevel).raises(NotImplementedError)


