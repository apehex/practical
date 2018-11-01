# -*- coding: utf-8 -*-

"""
================
Internal toolbox
================

Documentation is available in the docstrings and
online at __
"""

from __future__ import division, print_function, absolute_import

from practical.arrays import (
    convert_dict_to_array,
    reshapes,
    reshape_into_matrix,
    reshape_into_vector)
from practical.memory import (
    memoize)
from practical.types import (
    typecheck,
    anything,
    one_of,
    iterable,
    numeric,
    finite,
    symbolic,
    bounds,
    specifications)
from practical.units import (
    convert_radian_to_degree,
    convert_degree_to_radian)
from practical.web import (
    extract_text_from_html_markup)

__author__ = """apehex"""
__email__ = 'apehex@protonmail.com'
__version__ = '0.4.5'

__all__ = [
    'convert_dict_to_array',
    'reshapes',
    'reshape_into_matrix',
    'reshape_into_vector']

__all__ += [
    'memoize']

__all__ += [
    'typecheck',
    'anything',
    'one_of',
    'iterable',
    'numeric',
    'finite',
    'symbolic',
    'bounds',
    'specifications']

__all__ += [
    'convert_radian_to_degree',
    'convert_degree_to_radian']

__all__ += [
    'extract_text_from_html_markup']
