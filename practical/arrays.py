# -*- coding: utf-8 -*-

"""
==========================
Matrices & vector handling
==========================

"""

from __future__ import division, print_function, absolute_import

from decorator import decorator
import numpy as np

from practical.types import *

#####################################################################
# SHAPE ENFORCING
#####################################################################

def reshapes(*shapes):
    """
    Function decorator. Check whether the ndarray arguments match the
    required shapes.

    Parameters
    ----------
    shapes: list of tuples.
        The expected shapes for each ndarray argument.
        For non array types, provide an empty tuple.

    Returns
    -------
    out: caller function, decorated.
        All the ndarray arguments are reshaped.
    """
    def caller(f, *args, **kwargs):
        assert len(args) == len(shapes)

        reshaped_args = [
            np.reshape(
                a=arg,
                newshape=shapes[i])
            if shapes[i] and isinstance(arg, np.ndarray) else arg
            for i, arg in enumerate(args)]

        return f(*reshaped_args, **kwargs)

    return decorator(caller)

#####################################################################
# LINEAR ALGEBRA & ARRAY MANIPULATIONS
#####################################################################

@typecheck
def convert_dict_to_array(
        data: dict,
        keys: one_of(nothing, iterable) = None,
        default: numeric = 0.0) -> np.ndarray:
    """
    Creates an array with the size of keys, filling missing dimensions.

    Args:
        data (dict): the dictionary to convert.
        keys (list of string): the FULL list of axes keys.

    Returns:
        np.array: the array, with the size of keys.
    """
    axes = keys if keys else data.keys()

    data_list = [
        data.get(a, default) 
        for a in axes]

    data_array = np.array(data_list)

    return reshape_into_vector(data_array)

@typecheck
def reshape_into_matrix(
        data: np.ndarray,
        shape: tuple) -> np.ndarray:
    """
    """
    return np.reshape(
        a=data,
        newshape=shape,
        order='C')

@typecheck
def reshape_into_vector(
        data: np.ndarray) -> np.ndarray:
    """
    """
    return np.reshape(
        a=data,
        newshape=(-1, data.size),
        order='C')