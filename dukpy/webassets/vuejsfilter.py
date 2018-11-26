# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import os

from webassets.filter import Filter, option

import dukpy


__all__ = ('CompileLess', )


class CompileVueTemplate(Filter):
    name = 'vuejs-template'
    max_debug_level = None
    options = {}

    def input(self, _in, out, **kw):
        options = {'paths': []}
        if 'source_path' in kw:
            options['paths'].append(os.path.dirname(kw['source_path']))

        src = dukpy.vue_template_compiler(_in.read(), options=options)
        out.write(src)
