"""
F-strings are fabulous, why can't we make the same with Tuple and lists ?

Now you can::


    In [1]: from ftuple import f

    In [2]: h = "Hello"

    In [3]: w = "World"

    In [4]: f"{h} {w}"
    Out[4]: 'Hello World'

    In [5]: f({h}, {w})
    Out[5]: ('Hello', 'World')

    In [6]: f[{h}, {w}]
    Out[6]: ['Hello', 'World']


"""

__version__ = '1.0.0'

__all__ = ['f']


def _render_args(args):
    return [next(iter(a)) if isinstance(a, set) else a for a in args]


class F: 

    def __call__(self, *args):
        return tuple(_render_args(args))

    def __getitem__(self, args):
        return _render_args(args)


f = F()
