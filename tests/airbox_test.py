import datetime
import unittest
from assertpy import assert_that
from hwamsmartctrl import airbox

class AirboxTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.uut = airbox.connect("192.168.1.194")
    
    def tearDown(self):
        self.uut.close()
    
    async def test_determine_hostname(self):
        with self.uut.determineHostname() as name:
            assert_that(name).is_equal_to("ihs_82646f88f3c3")

    async def test_get_stove_data(self):
        with self.uut.getStoveData() as data:
            assert_that(data.day).is_equal_to(datetime.date.now().day())

    async def test_start_combustion(self):        
        with self.uut.startCombustion() as succeeded:
            assert_that(succeeded).is_true()
        with self.uut.getStoveData() as data:
            assert_that(data).contains_entry(phase=0)
    
    async def test_set_burn_level(self):
        assert_that(self.uut.setBurnLevel).raises(NotImplementedError)


