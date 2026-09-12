"""
LeetCode 349: Intersection of Two Arrays II
Problem: Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Solution: Use hashmap to count frequencies of elements in the first array, then iterate through the second array.
Time Complexity: O(n + m) where n and m are lengths of nums1 and nums2
Space Complexity: O(min(n, m)) for the hashmap
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


# Alternative solution using sorting (when space is not a concern)
def intersect_sorting(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Alternative solution using two-pointer technique after sorting.
    Time Complexity: O(n log n + m log m)
    Space Complexity: O(1) or O(log n + m) for sorting
    """
    nums1.sort()
    nums2.sort()
    
    i, j = 0, 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Output: {intersect(nums1_1, nums2_1)}")  # Expected: [2, 2]
    
    # Test case 2
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Output: {intersect(nums1_2, nums2_2)}")  # Expected: [4, 9]
    
    # Test case 3
    nums1_3 = [1, 2, 2, 1]
    nums2_3 = [2]
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Output: {intersect(nums1_3, nums2_3)}")  # Expected: [2]