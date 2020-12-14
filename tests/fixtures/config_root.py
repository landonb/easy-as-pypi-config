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

import pytest

from config_decorator import section


@pytest.fixture
def basic_config_root():

    @section(None)
    class ConfigRoot(object):
        pass

    @ConfigRoot.section('foo')
    class ConfigurableFoo(object):

        @property
        @ConfigRoot.setting("foo.bar option")
        def bar(self):
            return ''

        @property
        @ConfigRoot.setting("hidden option", hidden=True)
        def boo(self):
            return ''

    @ConfigRoot.section('baz')
    class ConfigurableFoo(object):
        pass

    return ConfigRoot


@pytest.fixture()
def basic_config_file(filepath):
    with open(filepath, 'w') as conf_file:
        conf_file.write(
            """
[foo]
bar = 'baz'
bat = 123

[quux]
qiix = 'foo'
""".lstrip()
        )
    return filepath

