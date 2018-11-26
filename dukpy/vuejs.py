
from .nodelike import NodeLikeInterpreter


class VueCompilerError(Exception):
    pass


def vue_template_compiler(source, options=None):
    """Compiles the given vue.js template to javascript"""
    options = options or {}
    res = NodeLikeInterpreter().evaljs(
        ('const compiler = require("vue-template-compiler");'
         'var compiled = compiler.compile(dukpy.source);',
         'var result = {"error": null, "output": compiled.render};'
         'result;'),
        source=source,
        options=options
    )
    if not res:
        raise RuntimeError('Results or errors unavailable')

    if res.get('error'):
        raise VueCompilerError(res['error'])

    return res['output']
