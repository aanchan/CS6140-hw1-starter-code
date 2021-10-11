import pytest
import numpy as np


@pytest.fixture
def get_samples():
    # These can be replaced with actual
    # vectors you want to work with
    x1 = np.random.rand(3)
    x2 = np.random.rand(4)
    yield x1, x2


def test_equality(get_samples):
    """
    This is an example test case
    with fixtures and documentation
    GIVEN Two vectors x1, x2
    WHEN they are generated randomly to be of unqeual sizes
    THEN assert that the sizes are actually unequal
    :param get_samples:
    :return:
    """
    x1 = get_samples[0]
    x2 = get_samples[1]
    assert np.size(x1) != np.size(x2)


def test_euclidean_for_loop(get_samples):
    """
    Use this to test your for loop implementation
    :param get_samples:
    :return:
    """
    raise NotImplementedError


def test_euclidean_vectorized(get_samples):
    """
    Use this to test your for loop implementation
    Note you cannot use numpy.linalg.norm
    :param get_samples:
    :return:
    """