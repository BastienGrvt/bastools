from ._imports import *

def get_not_none(self, arg, arg_type=object):
    if arg is not None:
        if isinstance(arg, arg_type):
            return arg
        else:
            raise TypeError(f"TypeError in the parameters dictionary, {arg_type} expected.")
    else:
        raise ValueError(f"Please set the parameters `arg` to not None value.")

def set_not_none(self, class_parent, **kwargs):
    if class_parent is not None:
        for name, val in kwargs.items():
            if val is not None:
                setattr(class_parent, name, val) 
    else:
        raise ValueError(f"Please set the `class_parent` to not None value.")

