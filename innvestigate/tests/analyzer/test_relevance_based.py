# Begin: Python 2/3 compatibility header small
# Get Python 3 functionality:
from __future__ import\
    absolute_import, print_function, division, unicode_literals
from future.utils import raise_with_traceback, raise_from
# catch exception with: except Exception as e
from builtins import range, map, zip, filter
from io import open
import six
# End: Python 2/3 compatability header small


###############################################################################
###############################################################################
###############################################################################


import pytest


from innvestigate.utils.tests import dryrun

from innvestigate.analyzer import *


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__BaselineLRPZ():

    def method(model):
        return BaselineLRPZ(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPZ():

    def method(model):
        return LRPZ(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPZ__equal_BaselineLRPZ():

    _all_close_rtol = 10**-5
    _all_close_atol = 10**-5

    def method1(model):
        return BaselineLRPZ(model)

    def method2(model):
        return LRPZWithBias(model)

    return dryrun.test_equal_analyzer(method1,
                                      method2,
                                      "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPZ__with_input_layer_rule():

    def method(model):
        return LRPZ(model, input_layer_rule="Flat")

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPZ__with_boxed_input_layer_rule():

    def method(model):
        return LRPZ(model, input_layer_rule=(-10, 10))

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPZWithBias():

    def method(model):
        return LRPZWithBias(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPZPlus():

    def method(model):
        return LRPZPlus(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPEpsilon():

    def method(model):
        return LRPEpsilon(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPEpsilonWithBias():

    def method(model):
        return LRPEpsilonWithBias(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPWSquare():

    def method(model):
        return LRPWSquare(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPFlat():

    def method(model):
        return LRPFlat(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPAlphaBeta():

    def method(model):
        return LRPAlphaBeta(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPAlpha1Beta1():

    def method(model):
        return LRPAlpha1Beta1(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPAlpha1Beta1WithBias():

    def method(model):
        return LRPAlpha1Beta1WithBias(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPAlpha2Beta1():

    def method(model):
        return LRPAlpha2Beta1(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPAlpha2Beta1WithBias():

    def method(model):
        return LRPAlpha2Beta1WithBias(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPAlpha1Beta0():

    def method(model):
        return LRPAlpha1Beta0(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__LRPAlpha1Beta0WithBias():

    def method(model):
        return LRPAlpha1Beta0WithBias(model)

    return dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__SerializeLRPZ():

    def method(model):
        return LRPZ(model)

    return dryrun.test_serialize_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__SerializeLRPAlphaBeta():

    def method(model):
        return LRPAlphaBeta(model)

    return dryrun.test_serialize_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__SerializeLRPAlpha1Beta1():

    def method(model):
        return LRPAlpha1Beta1(model)

    return dryrun.test_serialize_analyzer(method, "trivia.*:mnist.log_reg")
