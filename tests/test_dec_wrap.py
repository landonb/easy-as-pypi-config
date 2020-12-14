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

from easy_as_pypi_config.dec_wrap import decorate_and_wrap


def test_decorate_and_wrap_with_complete(basic_config_root):
    config_obj = decorate_and_wrap(
        section_name='a-test!', section_cdec=basic_config_root, complete=True,
    )
    assert config_obj.dict() == {'a-test!': {'foo': {'bar': ''}}}


def test_decorate_and_wrap_sans_complete(basic_config_root):
    config_obj = decorate_and_wrap(
        section_name='a-test!', section_cdec=basic_config_root, complete=False,
    )
    assert config_obj.dict() == {'a-test!': {}}

