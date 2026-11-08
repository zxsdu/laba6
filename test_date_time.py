"""Тести для пакета date_time."""
import unittest
from datetime import date, datetime, time
from unittest.mock import patch

import date_time
from date_time.current_info import (
    get_current_date, get_current_datetime, get_current_time,
)
from date_time.formatting import format_date_time

FIXED = datetime(2026, 11, 8, 14, 30, 5, 123456)  # неділя


class TestCurrentInfo(unittest.TestCase):
    def test_get_current_date(self):
        with patch("date_time.current_info.datetime") as mocked:
            mocked.now.return_value = FIXED
            self.assertEqual(get_current_date(), date(2026, 11, 8))

    def test_get_current_time(self):
        with patch("date_time.current_info.datetime") as mocked:
            mocked.now.return_value = FIXED
            self.assertEqual(get_current_time(), time(14, 30, 5))

    def test_get_current_datetime(self):
        with patch("date_time.current_info.datetime") as mocked:
            mocked.now.return_value = FIXED
            self.assertEqual(get_current_datetime(),
                             datetime(2026, 11, 8, 14, 30, 5))

    def test_real_types(self):
        self.assertIsInstance(get_current_date(), date)
        self.assertIsInstance(get_current_time(), time)
        self.assertEqual(get_current_time().microsecond, 0)


class TestFormatting(unittest.TestCase):
    def test_named_formats(self):
        expected = {
            "iso": "2026-11-08 14:30:05",
            "ua": "08.11.2026 14:30",
            "us": "11/08/2026 02:30 PM",
            "date": "08.11.2026",
            "time": "14:30:05",
            "long": "8 листопада 2026 р., 14:30",
            "full": "неділя, 8 листопада 2026 р., 14:30:05",
        }
        for name, text in expected.items():
            with self.subTest(fmt=name):
                self.assertEqual(format_date_time(FIXED, name), text)

    def test_default_format(self):
        self.assertEqual(format_date_time(FIXED), "08.11.2026 14:30")

    def test_custom_strftime(self):
        self.assertEqual(format_date_time(FIXED, "%d/%m/%y"), "08/11/26")

    def test_months_and_weekdays(self):
        self.assertEqual(format_date_time(datetime(2026, 1, 5), "long"),
                         "5 січня 2026 р., 00:00")
        self.assertTrue(format_date_time(datetime(2026, 3, 6), "full")
                        .startswith("п’ятниця"))

    def test_errors(self):
        with self.assertRaises(ValueError):
            format_date_time(FIXED, "unknown")
        with self.assertRaises(TypeError):
            format_date_time("2026-11-08", "iso")
        with self.assertRaises(TypeError):
            format_date_time(FIXED, 123)


class TestPackage(unittest.TestCase):
    def test_package_metadata(self):
        self.assertEqual(date_time.__version__, "1.0.0")
        self.assertIn("formatting", date_time.__all__)

    def test_docstrings(self):
        for obj in (date_time, get_current_date, get_current_time,
                    get_current_datetime, format_date_time):
            self.assertTrue(obj.__doc__ and obj.__doc__.strip())


if __name__ == "__main__":
    unittest.main()
