from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest2

from status_checker import StatusChecker


class TestStatusChecker(unittest2.TestCase):
    def test_status_english_true(self):
        self.assertEqual('ok', StatusChecker._status_english(True))

    def test_status_english_false(self):
        self.assertEqual('unavailable', StatusChecker._status_english(False))

    def test_check_status__when_no_exception__returns_func_output(self):
        resp = StatusChecker._check_status(lambda: True, False)
        self.assertTrue(resp)

    def test_check_status__when_exception_and_read_exception__returns_exception_message(self):
        def func():
            raise Exception('some message')
        resp = StatusChecker._check_status(func, True)
        self.assertEqual(resp['message'], 'some message')
        self.assertFalse(resp['available'])

    def test_check_status__when_exception_and_not_read_exception__returns_generic_message(self):
        def func():
            raise Exception('some message')
        resp = StatusChecker._check_status(func, False)
        self.assertNotEqual(resp['message'], 'some message')
        self.assertFalse(resp['available'])

    def test_status_with_failures(self):
        def func():
            raise Exception('some message')
        status_checker = StatusChecker(success=lambda: dict(available=True),
                                       fail=lambda: dict(available=False),
                                       exception=func)
        resp = status_checker.status()
        self.assertFalse(resp['available'])
        self.assertEqual(2, resp['failure_count'])
        self.assertTrue(resp['components']['success']['available'])
        self.assertFalse(resp['components']['fail']['available'])
        self.assertFalse(resp['components']['exception']['available'])

    def test_status_all_success(self):
        status_checker = StatusChecker(success=lambda: dict(available=True))
        resp = status_checker.status()
        self.assertTrue(resp['available'])
        self.assertEqual(0, resp['failure_count'])
        self.assertTrue(resp['components']['success']['available'])
