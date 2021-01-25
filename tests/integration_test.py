#!/usr/bin/env python

import twder
import unittest
import datetime


class TestStringMethods(unittest.TestCase):
    def _check_rate_value(self, v):
        self.assertNotEqual(v, '')
        self.assertEqual(v, v.strip())

    def all_element_is_str(self, container):
        for e in container:
            self.assertIsInstance(e, str)

    def check_range_result(self, range_result):
        self.assertIsInstance(range_result, list)
        map(self.all_element_is_str, range_result)

    def test_currencies(self):
        ret = twder.currencies()
        self.assertIsInstance(ret, list)
        self.all_element_is_str(ret)

    def test_currency_name_dict(self):
        ret = twder.currency_name_dict()
        currencies = twder.currencies()
        for c in currencies:
            self.assertIn(c, ret)
            self.assertIsInstance(ret[c], str)

    def test_now_all(self):
        for k, v in twder.now_all().items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, tuple)
            self._check_rate_value(v[1])
            self._check_rate_value(v[2])
            self._check_rate_value(v[3])
            self._check_rate_value(v[4])

    def test_now(self):
        ret = twder.now("JPY")
        self.assertIsInstance(ret, tuple)
        self.all_element_is_str(ret)

    def test_pastday(self):
        ret = twder.past_day("JPY")
        self.check_range_result(ret)

    def test_past_six_month(self):
        ret = twder.past_six_month("JPY")
        self.check_range_result(ret)

    def test_specify_month(self):
        now = datetime.datetime.now() - datetime.timedelta(days=31)
        ret = twder.specify_month("JPY", now.year, now.month)
        self.check_range_result(ret)


if __name__ == "__main__":
    unittest.main()
