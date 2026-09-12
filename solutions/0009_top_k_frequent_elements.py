"""
LeetCode 347: Top K Frequent Elements
Problem: Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Solution: Use hashmap to count frequencies, then use heap or bucket sort to get top k.
Time Complexity: O(n + k log n) for heap approach, O(n) for bucket sort
Space Complexity: O(n) for storing frequencies
"""

import heapq
from collections import Counter
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements in the array.
    
    Args:
        nums: List[int] - Array of integers
        k: int - Number of top frequent elements to return
        
    Returns:
        List[int] - The k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Use min-heap to keep track of top k elements
    # We store negative frequency to simulate max-heap behavior with min-heap
    min_heap = []
    
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        # Keep heap size at most k
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract elements from heap (ignore frequencies)
    return [num for freq, num in min_heap]


# Alternative solution using bucket sort (O(n) time complexity)
def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    Alternative solution using bucket sort for O(n) time complexity.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Create buckets where index represents frequency
    # Maximum frequency can be len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Place elements in buckets based on their frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect top k frequent elements from buckets (start from highest frequency)
    result = []
    for i in range(len(buckets) - 1, 0, -1):  # From high to low frequency
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result


# Alternative solution using sorting (less efficient but simple)
def top_k_frequent_sort(nums: List[int], k: int) -> List[int]:
    """
    Alternative solution using sorting.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    freq_map = Counter(nums)
    # Sort by frequency (descending) and take top k
    return [num for num, _ in sorted(freq_map.items(), key=lambda x: x[1], reverse=True)[:k]]


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {top_k_frequent(nums1, k1)}")  # Expected: [1, 2] or [2, 1]
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {top_k_frequent(nums2, k2)}")  # Expected: [1]
    
    # Test case 3
    nums3 = [4, 1, -1, 2, -1, 2, 3]
    k3 = 2
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {top_k_frequent(nums3, k3)}")  # Expected: [-1, 2] or [2, -1]
    
    # Verify all solutions give same results
    print("\n" + "="*50)
    print("Verifying all solutions:")
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([4, 1, -1, 2, -1, 2, 3], 2)
    ]
    
    for nums, k in test_cases:
        heap_result = sorted(top_k_frequent(nums, k))
        bucket_result = sorted(top_k_frequent_bucket_sort(nums, k))
        sort_result = sorted(top_k_frequent_sort(nums, k))
        print(f"nums={nums}, k={k}:")
        print(f"  Heap: {heap_result}")
        print(f"  Bucket: {bucket_result}")
        print(f"  Sort: {sort_result}")
        print(f"  All equal: {heap_result == bucket_result == sort_result}")
        print()