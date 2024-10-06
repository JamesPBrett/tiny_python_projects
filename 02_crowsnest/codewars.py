#!/usr/bin/env python3
"""
Author : jamesbrett <jamesbrett@localhost>
Date   : 2024-10-03
Purpose: Crow's Nest
"""

def find_deleted_number(arr, mixed_arr):
    # Sort mixed array
    sorted_arr = sorted(mixed_arr)
    
    # Compare sorted arrays
    if sorted_arr == sorted(arr):
        return 0
    
    # Find the difference between the arrays
    for num in arr:
        if num not in sorted_arr:
            return num