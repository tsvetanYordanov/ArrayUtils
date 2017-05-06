# -*- coding: utf-8 -*-

# The parametrize function is generated, so this doesn't work:
#
#     from pytest.mark import parametrize
#
import pytest

parametrize = pytest.mark.parametrize

from array_splitter.array_splitter_util import ArraySplitterUtil


class TestArraySplitterUtil(object):
    @parametrize('array',
                 [[1, 2, 3], [1, 2, 3, 4, 5, 6],
                  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'klmn'],
                  [(1, 23), (45, 6), (7, 89), (0, 0, -1)]])
    @parametrize('num_of_splits', [1])
    def test_split_array(self, array, num_of_splits):
        array_splitter_util = ArraySplitterUtil(array)
        result = array_splitter_util.split_array(num_of_splits)
        array_len = len(array)
        arr_remainder = (array_len % num_of_splits)
        arr_quotient = array_len / num_of_splits
        expected_num_of_splits = arr_quotient + arr_remainder

        # Should be split into arrays num_of_splits arrays
        assert expected_num_of_splits == len(result)
        # They should be equally sized arrays if original array is divisible
        # by num_of_splits, otherwise all but the last array should be
        # equally sized
        if arr_remainder == 0:
            for arr in result:
                assert arr_quotient == len(arr)
        else:
            for arr in result[:-1]:
                assert arr_quotient == len(arr)
        # If the size of the original array cannot be divided equally
        # the final part should have length equal to the remainder
        if arr_remainder != 0:
            assert arr_remainder == len(result[-1])
