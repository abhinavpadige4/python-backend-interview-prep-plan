"""
LeetCode 350: Intersection of Two Arrays II (Duplicate practice)
Problem: Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Solution: Same as problem 349 - Use hashmap to count frequencies.
Time Complexity: O(n + m)
Space Complexity: O(min(n, m))
"""

from collections import Counter
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two arrays with proper frequency counting.
    
    Args:
        nums1: List[int] - First array of integers
        nums2: List[int] - Second array of integers
        
    Returns:
        List[int] - Intersection array with elements appearing min(count1, count2) times
    """
    # Count frequencies of elements in nums1
    freq = Counter(nums1)
    result = []
    
    # Iterate through nums2 and add to result if element exists in freq with count > 0
    for num in nums2:
        if freq[num] > 0:
            result.append(num)
            freq[num] -= 1
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1 (same as 349 test case 1)
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Output: {intersect(nums1_1, nums2_1)}")  # Expected: [2, 2]
    
    # Test case 2 (same as 349 test case 2)
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Output: {intersect(nums1_2, nums2_2)}")  # Expected: [4, 9]
    
    # Test case 3 (different input for variety)
    nums1_3 = [1, 1, 2, 2, 3]
    nums2_3 = [1, 2, 2, 4]
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Output: {intersect(nums1_3, nums2_3)}")  # Expected: [1, 2, 2]