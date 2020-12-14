############
Installation
############

.. |virtualenv| replace:: ``virtualenv``
.. _virtualenv: https://virtualenv.pypa.io/en/latest/

.. |workon| replace:: ``workon``
.. _workon: https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html?highlight=workon#workon

To install system-wide, run as superuser::

    $ pip3 install easy-as-pypi-config

To install user-local, simply run::

    $ pip3 install -U easy-as-pypi-config

To install within a |virtualenv|_, try::

    $ mkvirtualenv easy-as-pypi-config
    (easy-as-pypi-config) $ pip install release-ghub-pypi

To develop on the project, link to the source files instead::

    (easy-as-pypi-config) $ deactivate
    $ rmvirtualenv easy-as-pypi-config
    $ git clone git@github.com:tallybark/easy-as-pypi-config.git
    $ cd easy-as-pypi-config
    $ mkvirtualenv -a $(pwd) --python=/usr/bin/python3.8 easy-as-pypi-config
    (easy-as-pypi-config) $ make develop

After creating the virtual environment,
to start developing from a fresh terminal, run |workon|_::

    $ workon easy-as-pypi-config
    (easy-as-pypi-config) $ ...

