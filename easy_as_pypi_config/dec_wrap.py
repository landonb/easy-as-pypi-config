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

"""easy_as_pypi_config sub.package provides Carousel UX user configuration settings."""

from config_decorator.config_decorator import ConfigDecorator

from .fileboss import create_configobj

__all__ = (
    'decorate_and_wrap',
)


def decorate_and_wrap(section_name, section_cdec, complete=False):
    def _decorate_and_wrap():
        # Sink the section once so we can get ConfigObj to print
        # the leading [section_name].
        condec = ConfigDecorator.create_root_for_section(section_name, section_cdec)
        return wrap_in_configobj(condec, complete=complete)

    def wrap_in_configobj(condec, complete=False):
        config_obj = create_configobj(conf_path=None)
        # Set skip_unset so none of the default values are spit out (keeps the
        # config more concise); and set keep_empties so empty sections are spit
        # out (so, e.g., `[default]` at least appears).
        config_obj.merge(condec.as_dict(
            skip_unset=not complete,
            keep_empties=not complete,
        ))
        return config_obj

    return _decorate_and_wrap()

