#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np
import sympy as smp

import pytest
from numpy.testing import assert_allclose

import practical.types as types

#####################################################################
# GENERIC PREDICATES
#####################################################################

def test_anything():
    bullshit = [
        None,
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4),
        np.inf,
        3,
        -9.45,
        math.pi,
        True,
        np.bool_(64)]

    for x in bullshit:
        assert types.anything(x)

def test_nothing():

    bullshit = [
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4),
        np.inf,
        3,
        -9.45,
        math.pi,
        True,
        (None, None),
        np.bool_(64)]

    for x in bullshit:
        assert not types.nothing(x)

    assert types.nothing(None)

def test_one_of():
    x, y, z = smp.symbols('x y z')

    ok_spec = [
        {'a': (-2, 345)},
        {1: (-1, -1), 'z': (9, 9.3)},
        {'test': (3.4, 9.2)}]

    ok_symbolic = [
        3,
        -9.45,
        math.pi,
        True,
        np.bool_(64),
        x,
        x * y + z,
        smp.cos(y),
        4.5 * z ** x]

    for a in ok_spec:
        assert not types.one_of(types.numeric, types.symbolic)(a)
        assert not types.one_of(types.finite)(a)
        assert types.one_of(types.symbolic, types.iterable)(a)

    for a in ok_symbolic:
        assert not types.one_of(types.iterable, types.specifications)(a)
        assert types.one_of(types.iterable, types.symbolic)(a)

def test_iterable():
    bullshit = [
        list,
        lambda x: 3 * x,
        True,
        45,
        np.inf,
        np.bool_(None),
        None,
        types.numeric,
        types.one_of(types.numeric, types.bounds)]

    ok = [
        range(5),
        np.arange(32).reshape(4, -1),
        np.array((6, 3)),
        "iuuhig"]

    for x in bullshit:
        assert not types.iterable(x)

    for x in ok:
        assert types.iterable(x)

#####################################################################
# NUMERIC PREDICATES
#####################################################################

def test_numeric():
    bullshit = [
        None,
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4)]

    ok = [
        np.inf,
        3,
        -9.45,
        math.pi,
        True,
        np.bool_(64)]

    for x in bullshit:
        assert not types.numeric(x)

    for x in ok:
        assert types.numeric(x)

def test_finite():
    bullshit = [
        None,
        np.inf,
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (),
        (-84,),
        (43, -2),
        {},
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4)]

    ok = [
        3,
        -9.45,
        math.pi,
        True,
        np.bool_(64)]

    for x in bullshit:
        assert not types.finite(x)

    for x in ok:
        assert types.finite(x)

#####################################################################
# SYMBOLIC PREDICATES
#####################################################################

def test_symbolic():
    x, y, z = smp.symbols('x y z')

    bullshit = [
        None,
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4)]

    ok = [
        3,
        np.inf,
        -9.45,
        math.pi,
        True,
        np.bool_(64),
        x,
        x * y + z,
        smp.cos(y),
        4.5 * z ** x]

    for a in bullshit:
        assert not types.symbolic(a)

    for a in ok:
        assert types.symbolic(a)

#####################################################################
# BOUNDS PREDICATES
#####################################################################

def test_bounds_predicate_on_bullshit():
    bullshit = [
        3.4,
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4)]

    for x in bullshit:
        assert not types.bounds(x)

def test_bounds_predicate_on_tuples():
    tuples = [
        (-np.inf, 345),
        (-np.inf, np.inf),
        (9.3, 9.3),
        (3.4, 9)]

    for x in tuples:
        assert types.bounds(x)

def test_bounds_predicate_on_dicts():
    dicts = [
        {'a': (-np.inf, 345)},
        {1: (-np.inf, np.inf), 'z': (9.3, 9.3)},
        {'test': (3.4, 9.2)}]

    for x in dicts:
        assert types.bounds(x)

def test_bounds_predicate_on_arrays():
    arrays = [
        np.arange(12).reshape(6, -1)]

    for x in arrays:
        assert types.bounds(x)

#####################################################################
# SPECIFICATIONS PREDICATES
#####################################################################

def test_specifications_predicate_on_bullshit():
    bullshit = [
        3.4,
        "dsgiojdgf",
        lambda x, y : x - y,
        (True, 49.3),
        (3.1, np.nan),
        {'r': (-np.inf, 4.3)},  # format ok ; sould fail because of the infinite bound 
        (-84,),
        (),
        (43, -2),
        {},
        {'tr': 'àdfsg', (4, 5): (4.5, 9)},
        np.arange(12).reshape(3, 4)]

    for x in bullshit:
        assert not types.specifications(x)

def test_specifications_predicate_on_dicts():
    dicts = [
        {'a': (-2, 345)},
        {1: (-1, -1), 'z': (9, 9.3)},
        {'test': (3.4, 9.2)}]

    for x in dicts:
        assert types.specifications(x)

#####################################################################
# MATRIX & ARRAY PREDICATES
#####################################################################
