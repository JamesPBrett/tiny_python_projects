import pytest
from codewars import find_deleted_number

def test_find_deleted_number_with_missing_number():
    arr = [1, 2, 3, 4, 5]
    mixed_arr = [1, 2, 3, 5]
    assert find_deleted_number(arr, mixed_arr) == 4
    
    
def test_find_deleted_number_with_identical_arrays():
    arr = [1, 2, 3, 4, 5]
    mixed_arr = [1, 2, 3, 4, 5]
    assert find_deleted_number(arr, mixed_arr) == 0
    
def test_find_deleted_number_with_sorted_mixed_array():
    arr = [1, 2, 3, 4, 5]
    mixed_arr = [1, 2, 3, 5]
    assert find_deleted_number(arr, sorted(mixed_arr)) == 4
    

def test_fixed_tests():
    assert find_deleted_number([1,2,3,4,5], [3,4,1,5]) == 2
    assert find_deleted_number([1,2,3,4,5,6,7,8,9], [1,9,7,4,6,2,3,8]) == 5
    assert find_deleted_number([1,2,3,4,5,6,7,8,9], [5,7,6,9,4,8,1,2,3]) == 0
    assert find_deleted_number([0,1,2,3,4,5], [1,2,3,4,5]) == 0
    assert find_deleted_number([1, 2, 3], [1, 2]) == 3
