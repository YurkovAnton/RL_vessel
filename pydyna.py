# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pydyna')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pydyna')
    _pydyna = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pydyna', [dirname(__file__)])
        except ImportError:
            import _pydyna
            return _pydyna
        try:
            _mod = imp.load_module('_pydyna', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pydyna = swig_import_helper()
    del swig_import_helper
else:
    import _pydyna
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pydyna.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _pydyna.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pydyna.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pydyna.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pydyna.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pydyna.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pydyna.SwigPyIterator_copy(self)

    def next(self):
        return _pydyna.SwigPyIterator_next(self)

    def __next__(self):
        return _pydyna.SwigPyIterator___next__(self)

    def previous(self):
        return _pydyna.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pydyna.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pydyna.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pydyna.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pydyna.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pydyna.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pydyna.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pydyna.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pydyna.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class DoubleVector1D(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector1D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector1D, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pydyna.DoubleVector1D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pydyna.DoubleVector1D___nonzero__(self)

    def __bool__(self):
        return _pydyna.DoubleVector1D___bool__(self)

    def __len__(self):
        return _pydyna.DoubleVector1D___len__(self)

    def __getslice__(self, i, j):
        return _pydyna.DoubleVector1D___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pydyna.DoubleVector1D___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pydyna.DoubleVector1D___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pydyna.DoubleVector1D___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pydyna.DoubleVector1D___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pydyna.DoubleVector1D___setitem__(self, *args)

    def pop(self):
        return _pydyna.DoubleVector1D_pop(self)

    def append(self, x):
        return _pydyna.DoubleVector1D_append(self, x)

    def empty(self):
        return _pydyna.DoubleVector1D_empty(self)

    def size(self):
        return _pydyna.DoubleVector1D_size(self)

    def swap(self, v):
        return _pydyna.DoubleVector1D_swap(self, v)

    def begin(self):
        return _pydyna.DoubleVector1D_begin(self)

    def end(self):
        return _pydyna.DoubleVector1D_end(self)

    def rbegin(self):
        return _pydyna.DoubleVector1D_rbegin(self)

    def rend(self):
        return _pydyna.DoubleVector1D_rend(self)

    def clear(self):
        return _pydyna.DoubleVector1D_clear(self)

    def get_allocator(self):
        return _pydyna.DoubleVector1D_get_allocator(self)

    def pop_back(self):
        return _pydyna.DoubleVector1D_pop_back(self)

    def erase(self, *args):
        return _pydyna.DoubleVector1D_erase(self, *args)

    def __init__(self, *args):
        this = _pydyna.new_DoubleVector1D(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pydyna.DoubleVector1D_push_back(self, x)

    def front(self):
        return _pydyna.DoubleVector1D_front(self)

    def back(self):
        return _pydyna.DoubleVector1D_back(self)

    def assign(self, n, x):
        return _pydyna.DoubleVector1D_assign(self, n, x)

    def resize(self, *args):
        return _pydyna.DoubleVector1D_resize(self, *args)

    def insert(self, *args):
        return _pydyna.DoubleVector1D_insert(self, *args)

    def reserve(self, n):
        return _pydyna.DoubleVector1D_reserve(self, n)

    def capacity(self):
        return _pydyna.DoubleVector1D_capacity(self)
    __swig_destroy__ = _pydyna.delete_DoubleVector1D
    __del__ = lambda self: None
DoubleVector1D_swigregister = _pydyna.DoubleVector1D_swigregister
DoubleVector1D_swigregister(DoubleVector1D)

class FastTimeWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FastTimeWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FastTimeWrapper, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pydyna.new_FastTimeWrapper()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pydyna.delete_FastTimeWrapper
    __del__ = lambda self: None

    def load_p3d(self, p3d_file_name):
        return _pydyna.FastTimeWrapper_load_p3d(self, p3d_file_name)

    def select_vessel(self, vessel_id):
        return _pydyna.FastTimeWrapper_select_vessel(self, vessel_id)

    def get_vessel_pos_vel(self):
        return _pydyna.FastTimeWrapper_get_vessel_pos_vel(self)

    def set_norm_dem_rudder_level(self, level):
        return _pydyna.FastTimeWrapper_set_norm_dem_rudder_level(self, level)

    def set_norm_dem_prop_level(self, level):
        return _pydyna.FastTimeWrapper_set_norm_dem_prop_level(self, level)

    def advance(self):
        return _pydyna.FastTimeWrapper_advance(self)

    def reset_vessel_state(self, init_pos_vec):
        return _pydyna.FastTimeWrapper_reset_vessel_state(self, init_pos_vec)
FastTimeWrapper_swigregister = _pydyna.FastTimeWrapper_swigregister
FastTimeWrapper_swigregister(FastTimeWrapper)

# This file is compatible with both classic and new-style classes.


