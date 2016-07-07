==============
Status Checker
==============


.. image:: https://img.shields.io/pypi/v/pystatuschecker.svg
        :target: https://pypi.python.org/pypi/pystatuschecker

.. image:: https://img.shields.io/travis/timmartin19/pystatuschecker.svg
        :target: https://travis-ci.org/timmartin19/pystatuschecker

.. image:: https://readthedocs.org/projects/pystatuschecker/badge/?version=latest
        :target: https://status-checker.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/timmartin19/pystatuschecker/shield.svg
     :target: https://pyup.io/repos/github/timmartin19/pystatuschecker/
     :alt: Updates


A very simple package for checking the status of a service and its components


* Free software: MIT license
* Documentation: https://pystatuschecker.readthedocs.io.


Examples
--------

.. code-block:: python

    from status_checker import StatusChecker

    def check_database(config):
        # ... check if it's up and either return a dictionary like
        # {'available': <bool>} or throw an exception

    def check_other_service(config):
        # ... same as above

    status_checker = StatusChecker(database=check_database, other_service=check_other_service)
    status_dict = status_checker.status(config)

The status_dict include the state of the components
in the 'components' key, the `failure_count`, and the `status`
of the service as a whole

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
