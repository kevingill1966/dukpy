Notes on problem createing vuejs compoent
=========================================

I tried to build a vue.js filter, but could not get the javascript to run.

installed vue template compiler::

    $ python
    Python 2.7.15rc1 (default, Apr 15 2018, 21:51:34) 
    [GCC 7.3.0] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import dukpy
    >>> dukpy.install_jspackage('vue-template-compiler', None, './dukpy/jsmodules')
    Packages going to be installed: vue-template-compiler->2.5.17, de-indent->1.0.2, he->1.2.0
    Fetching https://registry.npmjs.org/de-indent/-/de-indent-1.0.2.tgz..
    Fetching https://registry.npmjs.org/vue-template-compiler/-/vue-template-compiler-2.5.17.tgz....................................................................................................
    Fetching https://registry.npmjs.org/he/-/he-1.2.0.tgz........................................
    Installing vue-template-compiler in ./dukpy/jsmodules Done!


Running my tests
----------------

Command::

    nosetests -v tests/test_webassets_filter.py

Error::

    ======================================================================
    ERROR: test_webassets_filter.TestVueFilter.test_template
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/kevin/.virtualenvs/insight_nrn/local/lib/python2.7/site-packages/nose/case.py", line 197, in runTest
        self.test(*self.arg)
      File "/srv/insight_nrn/submodules/dukpy/tests/test_webassets_filter.py", line 163, in test_template
        self.mkbundle('in', filters='vuejs-template', output='out').build()
      File "/home/kevin/.virtualenvs/insight_nrn/src/webassets/src/webassets/bundle.py", line 683, in build
        disable_cache=disable_cache))
      File "/home/kevin/.virtualenvs/insight_nrn/src/webassets/src/webassets/bundle.py", line 620, in _build
        force, disable_cache=disable_cache, extra_filters=extra_filters)
      File "/home/kevin/.virtualenvs/insight_nrn/src/webassets/src/webassets/bundle.py", line 544, in _merge_and_apply
        kwargs=item_data)
      File "/home/kevin/.virtualenvs/insight_nrn/src/webassets/src/webassets/merge.py", line 280, in apply
        return self._wrap_cache(key, func)
      File "/home/kevin/.virtualenvs/insight_nrn/src/webassets/src/webassets/merge.py", line 222, in _wrap_cache
        content = func().getvalue()
      File "/home/kevin/.virtualenvs/insight_nrn/src/webassets/src/webassets/merge.py", line 255, in func
        getattr(filter, type)(data, out, **kwargs_final)
      File "/srv/insight_nrn/submodules/dukpy/dukpy/webassets/vuejsfilter.py", line 24, in input
        src = dukpy.vue_template_compiler(_in.read(), options=options)
      File "/srv/insight_nrn/submodules/dukpy/dukpy/vuejs.py", line 18, in vue_template_compiler
        options=options
      File "/srv/insight_nrn/submodules/dukpy/dukpy/evaljs.py", line 57, in evaljs
        res = _dukpy.eval_string(self, jscode, jsvars)
    JSRuntimeError: SyntaxError: unterminated statement (line 2)
        vue-template-compiler/package.json:2
        duk_js_compiler.c:6594
        anon  native strict preventsyield
        anon vue-template-compiler:5 preventsyield
        require  native strict preventsyield
        eval src/pyduktape.c:1 preventsyield

