# 3-Day Python Backend Interview Preparation

This repository contains solutions to practice problems designed for a 3-day Python backend interview preparation plan. The plan covers core backend concepts including OOP, data structures, algorithms, databases, API design, concurrency, testing, and system design.

## Study Plan Overview

### Day 1: Python Fundamentals & Data Structures
- **Warm-up**: Python fundamentals review
- **OOP and Design Patterns**: Single Number, Happy Number
- **Data Structures**: Intersection of Two Arrays II, Valid Anagram
- **Algorithms**: Binary Search
- **Backend Basics**: HTTP, REST, FastAPI introduction

### Day 2: Databases & API Design
- **Database Fundamentals**: SQL basics (Combine Two Tables, Second Highest Salary)
- **NoSQL Concepts**: Redis, MongoDB basics (Top K Frequent Elements)
- **API Design**: REST vs GraphQL (Insert Delete GetRandom O(1))
- **Concurrency**: Threading, asyncio (Print in Order)

### Day 3: System Design & Testing
- **System Design Basics**: URL shortener, rate limiter (Encode and Decode TinyURL)
- **Testing**: Unit testing with pytest, mocking (Kth Largest Element in a Stream)
- **Final Review**: Mock interview, weak points review
- **Mock Coding Interview**: 30-minute practice session

## Problems Solved

### Day 1 Problems
1. [LeetCode 136: Single Number](./solutions/0001_single_number.py) - XOR operation to find unique element
2. [LeetCode 202: Happy Number](./solutions/0002_happy_number.py) - Cycle detection using hashset
3. [LeetCode 349: Intersection of Two Arrays II](./solutions/0003_intersection_of_two_arrays_ii.py) - Hashmap frequency counting
4. [LeetCode 242: Valid Anagram](./solutions/0004_valid_anagram.py) - Character frequency comparison
5. [LeetCode 704: Binary Search](./solutions/0005_binary_search.py) - Standard binary search algorithm
6. [LeetCode 350: Intersection of Two Arrays II](./solutions/0006_intersection_of_two_arrays_ii_practice.py) - Practice with different input

### Day 2 Problems
7. [LeetCode 175: Combine Two Tables](./solutions/0007_combine_two_tables.sql) - SQL LEFT JOIN operation
8. [LeetCode 176: Second Highest Salary](./solutions/0008_second_highest_salary.sql) - Subquery for second maximum
9. [LeetCode 347: Top K Frequent Elements](./solutions/0009_top_k_frequent_elements.py) - Heap and bucket sort approaches
10. [LeetCode 380: Insert Delete GetRandom O(1)](./solutions/0010_insert_delete_getrandom_o1.py) - List + dictionary for O(1) operations
11. [LeetCode 1114: Print in Order](./solutions/0011_print_in_order.py) - Thread synchronization with locks

### Day 3 Problems
12. [LeetCode 535: Encode and Decode TinyURL](./solutions/0012_encode_decode_tinyurl.py) - Hashmap-based URL shortening
13. [LeetCode 703: Kth Largest Element in a Stream](./solutions/0013_kth_largest_element_in_a_stream.py) - Min-heap for streaming data

## Concepts Covered

### Programming Concepts
- **Time and Space Complexity Analysis**
- **Data Structures**: Arrays, Hashmaps/Dictionaries, Sets, Heaps, Lists
- **Algorithms**: Binary Search, Sorting, Greedy, Cycle Detection
- **Object-Oriented Programming**: Class design, encapsulation
- **Functional Programming**: Pure functions, immutability concepts

### Backend-Specific Concepts
- **Database Operations**: SQL queries, JOINs, aggregation, indexing concepts
- **API Design**: REST principles, endpoint design, HTTP methods
- **Concurrency**: Threading, locks, semaphores, synchronization
- **System Design**: Hashing, load balancing, caching concepts
- **Testing**: Unit testing, mocking, test-driven development principles

### Python-Specific Features
- **Collections Module**: Counter, defaultdict
- **Heapq Module**: Min-heap and max-heap simulations
- **Threading Module**: Locks, Semaphores, Thread synchronization
- **Random Module**: Random number generation, choices
- **String Manipulation**: Encoding, decoding, character operations
- **Type Hints**: Modern Python typing for better code documentation

## Solution Characteristics

Each solution includes:
- ✅ **Complete working code** - No stubs or TODOs
- ✅ **Time and space complexity analysis**
- ✅ **Clear comments explaining the approach**
- ✅ **Multiple solution variants** when applicable
- ✅ **Test cases demonstrating correctness**
- ✅ **Alternative approaches** for comparison
- ✅ **Edge case handling**

## How to Use This Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/python-backend-interview-prep-plan.git
   ```

2. **Run individual solutions**:
   ```bash
   python solutions/0001_single_number.py
   ```

3. **Review the concepts** covered in each solution file's header comments

4. **Practice implementing** the solutions yourself before checking the provided code

5. **Focus on understanding** the trade-offs between different approaches

## Recommended Study Schedule

Follow the 3-day plan outlined above, dedicating time blocks to:
- Concept review and reading
- Problem solving (try to solve before looking at solutions)
- Solution review and understanding trade-offs
- Notes consolidation (as mentioned in the plan, create a Notion page)

## GitHub Repository Structure

```
python-backend-interview-prep-plan/
├── README.md                 # This file
├── solutions/
│   ├── 0001_single_number.py
│   ├── 0002_happy_number.py
│   ├── 0003_intersection_of_two_arrays_ii.py
│   ├── 0004_valid_anagram.py
│   ├── 0005_binary_search.py
│   ├── 0006_intersection_of_two_arrays_ii_practice.py
│   ├── 0007_combine_two_tables.sql
│   ├── 0008_second_highest_salary.sql
│   ├── 0009_top_k_frequent_elements.py
│   ├── 0010_insert_delete_getrandom_o1.py
│   ├── 0011_print_in_order.py
│   ├── 0012_encode_decode_tinyurl.py
│   └── 0013_kth_largest_element_in_a_stream.py
└── .gitignore
```

## Next Steps After Completing This Plan

1. **Expand problem solving** to more LeetCode medium/hard problems
2. **Practice system design** questions specific to backend services
3. **Work on backend projects** using FastAPI, Django, or Flask
4. **Practice behavioral interviews** using STAR method
5. **Review database optimization** techniques and indexing strategies
6. **Study microservices architecture** and distributed systems concepts

## Contributing

Feel free to fork this repository and add:
- Additional practice problems
- Alternative solutions in different languages
- Detailed explanations of concepts
- Links to relevant backend resources

Good luck with your Python backend interview preparation! 🚀