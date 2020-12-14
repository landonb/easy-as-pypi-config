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

from gettext import gettext as _

# FIXME/2020-12-14 04:07: Need table printer if this module gonna be useful!
#
#  from dob_bright.reports.render_results import render_results

__all__ = (
    'echo_config_decorator_table',
)


def echo_config_decorator_table(
    cfg_decors,
    exclude_section=False,
    include_hidden=False,
    render_results=lambda results, headers, **kwargs: None,
    **kwargs,
):
    sec_key_vals = []

    def _echo_config_decorator_table():
        for condec in cfg_decors:
            condec.walk(visitor)

        echo_table()

    def visitor(condec, keyval):
        # MAYBE: Option to show hidden config.
        # MAYBE: Option to show generated config.
        if keyval.hidden and not include_hidden:
            return

        val_def = str(keyval.value)
        if val_def != str(keyval.default):
            val_def += val_def and ' ' or ''
            val_def += encode_default(str(keyval.default))

        val_row = [
            condec.section_path(sep='.')
        ] if not exclude_section else []
        val_row += [
            keyval.name,
            val_def,
            keyval.doc,
        ]

        sec_key_vals.append(val_row)

    def echo_table():
        headers = [
            _("Section")
        ] if not exclude_section else []
        headers += [
            _("Name"),
            _("Value {}").format(encode_default(_("Default"))),
            _("Help"),
        ]

        render_results(
            results=sec_key_vals,
            headers=headers,
            **kwargs,
        )

    def encode_default(text):
        # 2019-11-30: (lb): I switched from [square brackets] to <angle brackets>
        # to avoid JSON-encoded lists being [[double bracketed]] (which triggered
        # extra mental cycles upon sight).
        return '<{}>'.format(text)

    _echo_config_decorator_table()


