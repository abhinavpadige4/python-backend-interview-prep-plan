"""
LeetCode 136: Single Number
Problem: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with linear runtime complexity and use only constant extra space.

Solution: Use XOR operation. XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def single_number(nums):
    """
    Find the element that appears only once in the array.
    
    Args:
        nums: List[int] - Array of integers where every element appears twice except one
        
    Returns:
        int - The element that appears only once
    """
    result = 0
    for num in nums:
        result ^= num
    return result


# Alternative solution using hashmap (for reference)
def single_number_hashmap(nums):
    """
    Alternative solution using hashmap to count frequencies.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for num, count in freq.items():
        if count == 1:
            return num
    return -1


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 2, 1]
    print(f"Input: {nums1}")
    print(f"Output: {single_number(nums1)}")  # Expected: 1
    
    # Test case 2
    nums2 = [4, 1, 2, 1, 2]
    print(f"Input: {nums2}")
    print(f"Output: {single_number(nums2)}")  # Expected: 4
    
    # Test case 3
    nums3 = [1]
    print(f"Input: {nums3}")
    print(f"Output: {single_number(nums3)}")  # Expected: 1