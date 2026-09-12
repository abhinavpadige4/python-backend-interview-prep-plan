"""
LeetCode 703: Kth Largest Element in a Stream
Problem: Design a class to find the kth largest element in a stream. Note that it is the kth largest element 
in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Solution: Use min-heap of size k to keep track of k largest elements seen so far.
The root of the heap will be the kth largest element.
Time Complexity: O(log k) for add operation, O(n log k) for initialization
Space Complexity: O(k) for the heap
"""

import heapq
from typing import List

class KthLargest:
    """
    Class to find the kth largest element in a stream using min-heap.
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the KthLargest object.
        
        Args:
            k: int - The kth largest element to find
            nums: List[int] - Initial stream of integers
        """
        self.k = k
        self.heap = []  # Min-heap to store k largest elements
        
        # Add all initial numbers to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Appends the integer val to the stream and returns the kth largest element.
        
        Args:
            val: int - Integer to append to the stream
            
        Returns:
            int - The kth largest element in the stream
        """
        # Add new value to heap
        heapq.heappush(self.heap, val)
        
        # If heap size exceeds k, remove smallest element
        if len(self.heap) > k:
            heapq.heappop(self.heap)
        
        # The root of min-heap is the kth largest element
        return self.heap[0]


# Alternative solution using sorting (less efficient for frequent additions)
class KthLargestSort:
    """
    Alternative implementation using sorting (less efficient for streams).
    Time Complexity: O(n log n) for add operation
    Space Complexity: O(n)
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the KthLargest object.
        """
        self.k = k
        self.nums = nums[:]  # Make a copy
        self.nums.sort()     # Keep sorted for efficiency

    def add(self, val: int) -> int:
        """
        Appends the integer val to the stream and returns the kth largest element.
        """
        # Insert val in sorted position
        import bisect
        bisect.insort(self.nums, val)
        
        # Return kth largest (from the end)
        return self.nums[-self.k]


# Alternative solution using max-heap (conceptual)
class KthLargestMaxHeap:
    """
    Alternative implementation using max-heap (conceptual - not practical for this problem).
    Would require storing all elements and extracting k times.
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the KthLargest object.
        """
        self.k = k
        self.nums = nums[:]

    def add(self, val: int) -> int:
        """
        Appends the integer val to the stream and returns the kth largest element.
        """
        self.nums.append(val)
        # Sort in descending order and return kth element
        sorted_nums = sorted(self.nums, reverse=True)
        return sorted_nums[self.k - 1]


# Test the implementation
def test_kth_largest():
    """
    Test the KthLargest implementation.
    """
    print("Testing KthLargest (min-heap approach)...")
    
    # Test case from LeetCode example
    k = 3
    arr = [4, 5, 8, 2]
    kth_largest = KthLargest(k, arr)
    
    print(f"Initialized with k={k}, nums={arr}")
    print(f"Initial heap state: {kth_largest.heap}")
    print(f"Initial kth largest: {kth_largest.heap[0] if kth_largest.heap else None}")
    print()
    
    # Test add operations
    test_values = [3, 5, 10, 9, 4]
    expected_results = [4, 5, 5, 8, 8]  # Expected kth largest after each add
    
    print("Add operations:")
    for i, (val, expected) in enumerate(zip(test_values, expected_results)):
        result = kth_largest.add(val)
        print(f"  Add({val}): returned {result}, expected {expected}, {'✓' if result == expected else '✗'}")
        print(f"    Heap state: {kth_largest.heap}")
    print()
    
    # Test edge cases
    print("Edge case tests:")
    
    # Test with k=1 (should return maximum element)
    kth_largest_1 = KthLargest(1, [])
    print(f"  k=1, empty stream: add(3) -> {kth_largest_1.add(3)} (expected: 3)")
    print(f"  k=1, add(5) -> {kth_largest_1.add(5)} (expected: 5)")
    print(f"  k=1, add(1) -> {kth_largest_1.add(1)} (expected: 5)")
    
    # Test with k larger than initial array
    kth_largest_large_k = KthLargest(5, [1, 2, 3])
    print(f"  k=5, nums=[1,2,3]: initial -> {kth_largest_large_k.heap}")
    print(f"  add(4) -> {kth_largest_large_k.add(4)} (expected: 1)")
    print(f"  add(5) -> {kth_largest_large_k.add(5)} (expected: 1)")
    print(f"  add(6) -> {kth_largest_large_k.add(6)} (expected: 2)")
    
    # Compare with alternative implementations
    print("\n" + "="*50)
    print("Comparing with alternative implementations:")
    
    test_cases = [
        (3, [4, 5, 8, 2], [3, 5, 10, 9, 4]),
        (1, [], [5, 1, 8]),
        (2, [0], [-1, 1, 2])
    ]
    
    for k, init_nums, add_vals in test_cases:
        print(f"\nTest case: k={k}, init_nums={init_nums}, add_vals={add_vals}")
        
        # Min-heap approach
        kl_heap = KthLargest(k, init_nums[:])
        heap_results = [kl_heap.add(val) for val in add_vals]
        
        # Sorting approach
        kl_sort = KthLargestSort(k, init_nums[:])
        sort_results = [kl_sort.add(val) for val in add_vals]
        
        print(f"  Heap results:  {heap_results}")
        print(f"  Sort results:  {sort_results}")
        print(f"  Match:         {heap_results == sort_results}")


if __name__ == "__main__":
    test_kth_largest()