"""
LeetCode 1114: Print in Order
Problem: Suppose we have a class:
  public class Foo {
    public void first() { print("first"); }
    public void second() { print("second"); }
    public void third() { print("third"); }
  }
The same instance of Foo will be passed to three different threads. Thread A will call first(), 
thread B will call second(), and thread C will call third(). Design a mechanism to ensure that 
second() is executed after first(), and third() is executed after second().

Solution: Use threading.Lock or Semaphore to control execution order.
Time Complexity: O(1) for each method call
Space Complexity: O(1) for the locks
"""

import threading
from typing import Callable

class Foo:
    """
    Class to ensure ordered execution of first(), second(), and third() methods by different threads.
    """

    def __init__(self):
        """
        Initialize two locks to control execution order.
        Initially, lock2 and lock3 are acquired to block second() and third().
        """
        self.lock_first_second = threading.Lock()
        self.lock_second_third = threading.Lock()
        
        # Initially acquire the locks to block second and third methods
        self.lock_first_second.acquire()
        self.lock_second_third.acquire()

    def first(self, printFirst: Callable[[], None]) -> None:
        """
        Print "first" and release lock for second().
        
        Args:
            printFirst: Callable[[], None] - function to print "first"
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Release lock to allow second() to proceed
        self.lock_first_second.release()

    def second(self, printSecond: Callable[[], None]) -> None:
        """
        Wait for first() to complete, then print "second" and release lock for third().
        
        Args:
            printSecond: Callable[[], None] - function to print "second"
        """
        # Wait for first() to complete
        self.lock_first_second.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # Release lock to allow third() to proceed
        self.lock_second_third.release()

    def third(self, printThird: Callable[[], None]) -> None:
        """
        Wait for second() to complete, then print "third".
        
        Args:
            printThird: Callable[[], None] - function to print "third"
        """
        # Wait for second() to complete
        self.lock_second_third.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


# Alternative solution using Semaphore
class FooSemaphore:
    """
    Alternative implementation using Semaphore instead of Lock.
    """

    def __init__(self):
        """
        Initialize two semaphores with 0 permits to block second and third initially.
        """
        self.sem_first_second = threading.Semaphore(0)
        self.sem_second_third = threading.Semaphore(0)

    def first(self, printFirst: Callable[[], None]) -> None:
        """
        Print "first" and release semaphore for second().
        """
        printFirst()
        self.sem_first_second.release()

    def second(self, printSecond: Callable[[], None]) -> None:
        """
        Wait for first() to complete, then print "second" and release semaphore for third().
        """
        self.sem_first_second.acquire()
        printSecond()
        self.sem_second_third.release()

    def third(self, printThird: Callable[[], None]) -> None:
        """
        Wait for second() to complete, then print "third".
        """
        self.sem_second_third.acquire()
        printThird()


# Test the implementation
def test_print_in_order():
    """
    Test the Foo class implementation with threads.
    """
    def print_first():
        print("first", end="")
    
    def print_second():
        print("second", end="")
    
    def print_third():
        print("third", end="")
    
    print("Testing Foo class with threads:")
    print("Expected output: firstsecondthird")
    print("Actual output:   ", end="")
    
    # Create instance
    foo = Foo()
    
    # Create threads
    thread_a = threading.Thread(target=foo.first, args=(print_first,))
    thread_b = threading.Thread(target=foo.second, args=(print_second,))
    thread_c = threading.Thread(target=foo.third, args=(print_third,))
    
    # Start threads in any order
    thread_b.start()  # second thread
    thread_c.start()  # third thread
    thread_a.start()  # first thread
    
    # Wait for all threads to complete
    thread_a.join()
    thread_b.join()
    thread_c.join()
    
    print()  # New line at end
    
    # Test with Semaphore version
    print("\nTesting FooSemaphore class with threads:")
    print("Expected output: firstsecondthird")
    print("Actual output:   ", end="")
    
    foo_sem = FooSemaphore()
    
    # Create threads
    thread_a_sem = threading.Thread(target=foo_sem.first, args=(print_first,))
    thread_b_sem = threading.Thread(target=foo_sem.second, args=(print_second,))
    thread_c_sem = threading.Thread(target=foo_sem.third, args=(print_third,))
    
    # Start threads in any order
    thread_b_sem.start()  # second thread
    thread_c_sem.start()  # third thread
    thread_a_sem.start()  # first thread
    
    # Wait for all threads to complete
    thread_a_sem.join()
    thread_b_sem.join()
    thread_c_sem.join()
    
    print()  # New line at end


if __name__ == "__main__":
    test_print_in_order()