"""
LeetCode 202: Happy Number
Problem: Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Solution: Use a set to detect cycles. Compute sum of squares of digits repeatedly.
Time Complexity: O(log n) per iteration, but bounded by cycle detection
Space Complexity: O(log n) for the set
"""

def is_happy(n):
    """
    Determine if a number is a happy number.
    
    Args:
        n: int - Positive integer to check
        
    Returns:
        bool - True if n is a happy number, False otherwise
    """
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1


# Alternative solution using Floyd's Cycle Detection (Tortoise and Hare)
def is_happy_floyd(n):
    """
    Alternative solution using Floyd's cycle detection algorithm.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum
    
    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1


# Test cases
if __name__ == "__main__":
    # Test case 1
    n1 = 19
    print(f"Input: {n1}")
    print(f"Output: {is_happy(n1)}")  # Expected: True
    
    # Test case 2
    n2 = 2
    print(f"Input: {n2}")
    print(f"Output: {is_happy(n2)}")  # Expected: False
    
    # Test case 3
    n3 = 1
    print(f"Input: {n3}")
    print(f"Output: {is_happy(n3)}")  # Expected: True