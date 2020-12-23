# This file exists within 'easy-as-pypi-config':
#
#   https://github.com/tallybark/easy-as-pypi-config#🍐
#
# Copyright © 2018-2020 Landon Bouma. All rights reserved.
#
# Permission is hereby granted,  free of charge,  to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge,  publish,  distribute, sublicense,
# and/or  sell copies  of the Software,  and to permit persons  to whom the
# Software  is  furnished  to do so,  subject  to  the following conditions:
#
# The  above  copyright  notice  and  this  permission  notice  shall  be
# included  in  all  copies  or  substantial  portions  of  the  Software.
#
# THE  SOFTWARE  IS  PROVIDED  "AS IS",  WITHOUT  WARRANTY  OF ANY KIND,
# EXPRESS OR IMPLIED,  INCLUDING  BUT NOT LIMITED  TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE  FOR ANY
# CLAIM,  DAMAGES OR OTHER LIABILITY,  WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE,  ARISING FROM,  OUT OF  OR IN  CONNECTION WITH THE
# SOFTWARE   OR   THE   USE   OR   OTHER   DEALINGS  IN   THE  SOFTWARE.

import os

from configobj import ConfigObj

import pytest


@pytest.fixture
def config_instance(tmpdir, faker):
    """Provide a (dynamicly generated) ConfigObj instance."""

    def generate_config(**kwargs):
        cfg_dict = generate_dict(**kwargs)
        # NOPE: You'd overwrite your user's file with the default path:
        #   from easy_as_pypi_config.fileboss import default_config_path
        #   configfile_path = default_config_path()
        configfile_path = os.path.join(tmpdir, 'easy-as-pypi-config-test.conf')
        config = ConfigObj(configfile_path)
        config.merge(cfg_dict)
        return config

    # ***

    def generate_dict(**kwargs):
        cfg_dict = {}

        # ***

        cfg_foo = {}
        cfg_dict['foo'] = cfg_foo

        cfg_foo.setdefault('bar', kwargs.get('bar', 'baz'))

        # ***

        return cfg_dict

    # ***

    return generate_config

