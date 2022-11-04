# -*- coding: utf-8 -*-
"""Tests for `Libreria_para_procesar_df` package."""

import random

import pytest

from Libreria_para_procesar_df import Libreria_para_procesar_df


@pytest.fixture
def generate_numbers():
    """Sample pytest fixture. Generates list of random integers.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

    return random.sample(range(100), 10)


def test_sum_numbers(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = Libreria_para_procesar_df.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers)


def test_max_number(generate_numbers):
    """Sample test function for max_number, using pytest fixture."""

    our_result = Libreria_para_procesar_df.max_number(generate_numbers)
    assert our_result == max(generate_numbers)


# def test_max_number_bad(generate_numbers):
#     """Sample test function that fails. Uncomment to see."""
#
#     our_result = Libreria_para_procesar_df.max_number(generate_numbers)
#     assert our_result == max(generate_numbers) + 1
