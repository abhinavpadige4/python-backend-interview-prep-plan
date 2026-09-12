"""
LeetCode 704: Binary Search
Problem: Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Solution: Standard binary search algorithm using two pointers.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Search for target in sorted array using binary search.
    
    Args:
        nums: List[int] - Sorted array of integers in ascending order
        target: int - Target value to search for
        
    Returns:
        int - Index of target if found, otherwise -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents potential overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Alternative solution using recursion
def search_recursive(nums: List[int], target: int) -> int:
    """
    Recursive binary search implementation.
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    def binary_search(left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)
    
    return binary_search(0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {search(nums1, target1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {search(nums2, target2)}")  # Expected: -1
    
    # Test case 3
    nums3 = [5]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {search(nums3, target3)}")  # Expected: 0
    
    # Test case 4
    nums4 = []
    target4 = 5
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {search(nums4, target4)}")  # Expected: -1