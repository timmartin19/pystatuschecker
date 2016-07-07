from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

_LOG = logging.getLogger(__name__)


class StatusChecker(object):
    """
    An class to safely check the status of multiple
    components and return a dictionary indicating the status
    of the overall health
    """

    def __init__(self, read_exception=False, **component_checkers):
        """
        Instantiate the status checker with the functions to
        call that will check the status of individual components

        :param bool read_exception: If true and a status
            checker throws an exception, it will return the message
            of the exception as the message for that component

            This can lead to security issues if the exception
            messages contain sensitive information
        :param dict{unicode:func} component_checkers: A dictionary
            of the component names as the keys and a function to call
            in order to check the status of the given component

            Every component checker should return a dictionary
            with at least a key `'available'` with a boolean
            value
        """
        self._component_checkers = component_checkers
        self.read_exception = read_exception

    def status(self, *args, **kwargs):
        """
        Call this method to get a dictionary that will
        describe the status of all components.  The `*args`
        and `**kwargs` will be passed to the function

        :param list args: args to pass to all of the component checkers
        :param dict kwargs: keyword arguments to pass to
            all of the component checkers
        :return: A dictionary including the
        :rtype: dict
        """
        resp = {}
        available = True
        fail_count = 0

        for component_name, checker in self._component_checkers.items():
            status_data = self._check_status(checker, self.read_exception, *args, **kwargs)
            status_data['status'] = self._status_english(status_data['available'])
            available = available and status_data['available']
            if not status_data['available']:
                fail_count += 1
            resp[component_name] = status_data

        return dict(status=self._status_english(available),
                    available=available,
                    components=resp,
                    failure_count=fail_count)

    @staticmethod
    def _check_status(func, read_exception, *args, **kwargs):
        """
        Checks the status of a single component by
        calling the func with the args.  The func is expected to
        return a dict with at least an `available=<bool>` key
        value pair

        :param func func: The function to call
        :param read_exception: If an exception is thrown
            should the exception message be passed as the
            message parameter.  If not a generic
            message parameter will be added to the dict
        :param tuple args: A list of arguments to pass to
            to function
        :param dict kwargs: a dict of keyword arguments
            to pass to the function
        :return: a dictionary that includes the state
            of the component.  At least an 'available'
            key is guaranteed
        :rtype: dict
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            _LOG.exception(e)
            message = str(e) if read_exception else 'An error occurred while checking the status'
            return dict(message=message, available=False)

    @staticmethod
    def _status_english(status):
        """
        The status of the component in english
        """
        return 'ok' if status else 'unavailable'
