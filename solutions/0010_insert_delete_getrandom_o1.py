"""
LeetCode 380: Insert Delete GetRandom O(1)
Problem: Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
  Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Solution: Use list and dictionary combination. List stores values for O(1) random access, 
dictionary maps values to their indices in the list for O(1) lookup and update.
Time Complexity: O(1) average for all operations
Space Complexity: O(n) where n is number of elements
"""

import random
from typing import Dict, List

class RandomizedSet:
    """
    RandomizedSet that supports insert, remove, and getRandom operations in O(1) average time.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals: List[int] = []           # List to store values
        self.val_to_index: Dict[int, int] = {}  # Dictionary to map value to its index in vals

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        
        Args:
            val: int - Value to insert
            
        Returns:
            bool - True if value was inserted, False if it already existed
        """
        if val in self.val_to_index:
            return False
        
        # Add to end of list
        self.vals.append(val)
        # Map value to its index
        self.val_to_index[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        
        Args:
            val: int - Value to remove
            
        Returns:
            bool - True if value was removed, False if it didn't exist
        """
        if val not in self.val_to_index:
            return False
        
        # Get index of element to remove
        index_to_remove = self.val_to_index[val]
        last_element = self.vals[-1]
        
        # Move last element to the position of element to remove
        self.vals[index_to_remove] = last_element
        self.val_to_index[last_element] = index_to_remove
        
        # Remove last element
        self.vals.pop()
        # Remove the value from dictionary
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        Returns:
            int - Random element from the set
        """
        return random.choice(self.vals)


# Test the implementation
def test_randomized_set():
    """
    Test the RandomizedSet implementation.
    """
    print("Testing RandomizedSet...")
    
    # Create instance
    randomized_set = RandomizedSet()
    
    # Test insert operations
    print(f"Insert 1: {randomized_set.insert(1)}")  # Expected: True
    print(f"Insert 2: {randomized_set.insert(2)}")  # Expected: True
    print(f"Insert 1 (again): {randomized_set.insert(1)}")  # Expected: False
    
    # Test getRandom (should return 1 or 2 with equal probability)
    print("GetRandom samples:")
    random_samples = []
    for _ in range(10):
        random_samples.append(randomized_set.getRandom())
    print(f"  Samples: {random_samples}")
    
    # Test remove operations
    print(f"Remove 1: {randomized_set.remove(1)}")  # Expected: True
    print(f"Remove 3: {randomized_set.remove(3)}")  # Expected: False (not present)
    
    # Test getRandom after removal (should only return 2)
    print("GetRandom after removing 1:")
    random_samples_after = []
    for _ in range(5):
        random_samples_after.append(randomized_set.getRandom())
    print(f"  Samples: {random_samples_after}")
    
    # Final state
    print(f"Final vals: {randomized_set.vals}")
    print(f"Final val_to_index: {randomized_set.val_to_index}")


if __name__ == "__main__":
    test_randomized_set()