import asyncio
import datetime
import os
import unittest
from unittest.mock import patch

from assertpy import assert_that
from aioresponses import aioresponses

from hwamsmartctrl.airbox import Airbox


class AirboxTest(unittest.IsolatedAsyncioTestCase):

    ip = "10.0.0.1"

    @classmethod
    def setUpClass(cls):
        cls.loop = asyncio.get_event_loop()
        cls.uut = cls.loop.run_until_complete(Airbox(cls.ip).connect())

    @classmethod
    def tearDownClass(cls):
        cls.loop.run_until_complete(cls.uut.close())
        cls.loop.close()

    @patch('aiodns.DNSResolver')
    def test_determine_hostname(self, dns_resolver_class):
        # GIVEN
        async def gethostbyaddr_mock(name: str):
            return "thename"

        resolver_mock = dns_resolver_class.return_value
        resolver_mock.gethostbyaddr = gethostbyaddr_mock

        # WHEN
        name = self.loop.run_until_complete(self.uut.determine_hostname())

        # THEN
        assert_that(name).is_equal_to("thename")

    @aioresponses()
    def test_get_stove_data(self, mocked):
        jsonFilePath = os.path.join(
            os.path.dirname(__file__),
            'get_stove_data.json')
        with open(jsonFilePath, "r") as file:
            content = file.read()

            mocked.get(
                f'http://{self.ip}/get_stove_data',
                status=200,
                body=content,
                headers={"Content-Type": "text/json"})

            data = self.loop.run_until_complete(self.uut.get_stove_data())
            assert_that(data.updating).is_false()
            assert_that(data.phase).is_equal_to(5)
            assert_that(data.night_lowering).is_false()
            assert_that(
                data.new_fire_wood_time).is_equal_to(
                datetime.time(
                    hour=0, minute=0))
            assert_that(data.burn_level).is_equal_to(2)
            assert_that(data.operation_mode).is_equal_to(2)
            assert_that(data.maintenance_alarms).is_equal_to(0)
            assert_that(data.safety_alarms).is_equal_to(0)
            assert_that(data.refill_alarm).is_false()
            assert_that(data.remote_refill_alarm).is_true(),
            assert_that(data.time_since_remote_msg).is_equal_to(6016)
            assert_that(data.version).is_equal_to("3.23.0")
            assert_that(data.remote_version).is_equal_to("3.6.0")
            assert_that(data.wifi_version).is_equal_to("12.6.0")
            assert_that(
                data.current_datetime).is_equal_to(
                datetime.datetime(
                    year=2024,
                    month=9,
                    day=14,
                    hour=23,
                    minute=1,
                    second=10))
            assert_that(
                data.night_begin_time).is_equal_to(
                datetime.time(
                    hour=22,
                    minute=0))
            assert_that(
                data.night_end_time).is_equal_to(
                datetime.time(
                    hour=6,
                    minute=0))
            assert_that(data.stove_temperature).is_equal_to(58)
            assert_that(data.room_temperature).is_equal_to(23)
            assert_that(data.oxygen_level).is_equal_to(0)
            assert_that(data.valve1_position).is_equal_to(40)
            assert_that(data.valve2_position).is_equal_to(60)
            assert_that(data.valve3_position).is_equal_to(35)
            assert_that(data.algorithm).is_equal_to("DS.DSB2.221129")
            assert_that(data.door_open).is_false()
            assert_that(
                data.service_date).is_equal_to(
                datetime.date(
                    year=2023,
                    month=9,
                    day=26))
            assert_that(data.remote_refill_beeps).is_equal_to(3)

    @aioresponses()
    def test_start_combustion(self, mocked):
        mocked.get(
            f'http://{self.ip}/start',
            status=200,
            body='{"response":"OK"}',
            headers={"Content-Type": "text/json"})
        succeeded = self.loop.run_until_complete(self.uut.start_combustion())
        assert_that(succeeded).is_true()

    @aioresponses()
    def test_set_burn_level(self, mocked):
        assert_that(self.uut.set_burn_level).raises(NotImplementedError)


if __name__ == "__main__":
    asyncio.run(unittest.main())
