import datetime
import json
import unittest

from assertpy import assert_that
from hwamsmartctrl.stovedata import StoveData, stove_data_of


class StoveDataTest(unittest.TestCase):
    def test_conversion(self):
        jsonStr = """
        {
            "updating": 0,
            "message_id": 3,
            "phase": 5,
            "night_lowering": 0,
            "new_fire_wood_hours": 1,
            "new_fire_wood_minutes": 55,
            "burn_level": 2,
            "operation_mode": 2,
            "maintenance_alarms": 0,
            "safety_alarms": 0,
            "refill_alarm": 0,
            "remote_refill_alarm": 1,
            "time_since_remote_msg": 6016,
            "version_major": 3,
            "version_minor": 23,
            "version_build": 0,
            "remote_version_major": 3,
            "remote_version_minor": 6,
            "remote_version_build": 0,
            "wifi_version_major": 12,
            "wifi_version_minor": 6,
            "wifi_version_build": 0,
            "day": 14,
            "month": 9,
            "year": 2024,
            "hours": 23,
            "minutes": 1,
            "seconds": 10,
            "night_begin_hour": 22,
            "night_begin_minute": 0,
            "night_end_hour": 6,
            "night_end_minute": 0,
            "stove_temperature": 5769,
            "room_temperature": 2343,
            "oxygen_level": 0,
            "valve1_position": 40,
            "valve2_position": 60,
            "valve3_position": 35,
            "algorithm": "DS.DSB2.221129",
            "door_open": false,
            "service_date": "2023-09-26",
            "remote_refill_beeps": 3
        }
        """
        actual = stove_data_of(json.loads(jsonStr))
        assert_that(actual.updating).is_false()
        assert_that(actual.phase).is_equal_to(5)
        assert_that(actual.night_lowering).is_false()
        assert_that(actual.new_fire_wood_time).is_equal_to(
            datetime.time(hour=1, minute=55))
        assert_that(actual.burn_level).is_equal_to(2)
        assert_that(actual.operation_mode).is_equal_to(2)
        assert_that(actual.maintenance_alarms).is_equal_to(0)
        assert_that(actual.safety_alarms).is_equal_to(0)
        assert_that(actual.refill_alarm).is_equal_to(0)
        assert_that(actual.remote_refill_alarm).is_equal_to(1)
        assert_that(actual.time_since_remote_msg).is_equal_to(6016)
        assert_that(actual.version).is_equal_to("3.23.0")
        assert_that(actual.remote_version).is_equal_to("3.6.0")
        assert_that(actual.wifi_version).is_equal_to("12.6.0")
        assert_that(actual.current_datetime).is_equal_to(datetime.datetime(
            year=2024, month=9, day=14, hour=23, minute=1, second=10))
        assert_that(actual.night_begin_time).is_equal_to(
            datetime.time(hour=22, minute=0))
        assert_that(actual.night_end_time).is_equal_to(
            datetime.time(hour=6, minute=0))
        assert_that(actual.stove_temperature).is_equal_to(58)
        assert_that(actual.room_temperature).is_equal_to(23)
        assert_that(actual.oxygen_level).is_equal_to(0)
        assert_that(actual.valve1_position).is_equal_to(40)
        assert_that(actual.valve2_position).is_equal_to(60)
        assert_that(actual.valve3_position).is_equal_to(35)
        assert_that(actual.algorithm).is_equal_to("DS.DSB2.221129")
        assert_that(actual.door_open).is_false()
        assert_that(actual.service_date).is_equal_to(
            datetime.date(year=2023, month=9, day=26))
        assert_that(actual.remote_refill_beeps).is_equal_to(3)
