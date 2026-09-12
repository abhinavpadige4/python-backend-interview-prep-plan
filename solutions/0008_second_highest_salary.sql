"""
LeetCode 176: Second Highest Salary
Problem: Write a SQL query to get the second highest salary from the Employee table. 
If there is no second highest salary, then return null.

Employee table:
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

Solution: Use subquery to find maximum salary, then find maximum salary less than that.
Time Complexity: O(n) where n is number of employees
Space Complexity: O(1)
"""

# SQL Solution for LeetCode 176: Second Highest Salary
SECOND_HIGHEST_SALARY_SQL = """
SELECT 
    MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
"""

# Alternative SQL solution using LIMIT and OFFSET
SECOND_HIGHEST_SALARY_SQL_ALT = """
SELECT 
    (SELECT DISTINCT Salary 
     FROM Employee 
     ORDER BY Salary DESC 
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;
"""

# Alternative SQL solution using OFFSET with handling for no second highest
SECOND_HIGHEST_SALARY_SQL_ALT2 = """
SELECT 
    CASE 
        WHEN (SELECT COUNT(DISTINCT Salary) FROM Employee) >= 2
        THEN (SELECT DISTINCT Salary 
              FROM Employee 
              ORDER BY Salary DESC 
              LIMIT 1 OFFSET 1)
        ELSE NULL
    END AS SecondHighestSalary;
"""


def explain_second_highest_salary():
    """
    Explain the solution for finding second highest salary.
    """
    explanation = """
    Problem Analysis:
    - Find the second highest distinct salary from Employee table
    - If there's no second highest salary (less than 2 distinct salaries), return null
    
    Solution Approach (Primary):
    1. Find the maximum salary using subquery: (SELECT MAX(Salary) FROM Employee)
    2. Find maximum salary that is less than this maximum: WHERE Salary < [max_salary]
    3. Use MAX() aggregate to get the highest among those lesser salaries
    
    Why this approach works:
    - The inner subquery gets the highest salary
    - The outer query finds all salaries less than the highest
    - MAX() of those gives us the second highest
    - Automatically handles case where no second highest exists (returns null)
    
    Alternative Approach (LIMIT/OFFSET):
    - Order salaries descending and skip the first (highest) one
    - Take the next one as second highest
    - Need to handle case where result might be empty
    
    Time Complexity: O(n) for scanning the table
    Space Complexity: O(1) 
    """
    return explanation


def simulate_second_highest_salary():
    """
    Simulate the SQL query result with sample data.
    """
    # Test case 1: Normal case with multiple salaries
    salaries1 = [100, 200, 300]
    # Expected: 200
    
    # Test case 2: Two salaries
    salaries2 = [100, 200]
    # Expected: 100
    
    # Test case 3: Single salary
    salaries3 = [100]
    # Expected: None/null
    
    # Test case 4: Duplicate salaries
    salaries4 = [100, 100, 200]
    # Expected: 100 (second highest distinct)
    
    def get_second_highest(salaries):
        distinct_salaries = sorted(list(set(salaries)), reverse=True)
        if len(distinct_salaries) >= 2:
            return distinct_salaries[1]
        return None
    
    test_cases = [
        ([100, 200, 300], 200),
        ([100, 200], 100),
        ([100], None),
        ([100, 100, 200], 100),
        ([1, 2, 2, 3], 2)
    ]
    
    results = []
    for salaries, expected in test_cases:
        result = get_second_highest(salaries)
        results.append({
            "input": salaries,
            "expected": expected,
            "actual": result,
            "pass": result == expected
        })
    
    return results


if __name__ == "__main__":
    print("SQL Solution:")
    print(SECOND_HIGHEST_SALARY_SQL.strip())
    print("\n" + "="*50 + "\n")
    
    print("Alternative SQL Solution (LIMIT/OFFSET):")
    print(SECOND_HIGHEST_SALARY_SQL_ALT.strip())
    print("\n" + "="*50 + "\n")
    
    print("Explanation:")
    print(explain_second_highest_salary())
    print("\n" + "="*50 + "\n")
    
    print("Simulation Results:")
    results = simulate_second_highest_salary()
    for i, result in enumerate(results, 1):
        print(f"Test Case {i}:")
        print(f"  Input: {result['input']}")
        print(f"  Expected: {result['expected']}")
        print(f"  Actual: {result['actual']}")
        print(f"  Pass: {result['pass']}")
        print()