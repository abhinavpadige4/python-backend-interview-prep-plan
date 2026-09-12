"""
LeetCode 175: Combine Two Tables
Problem: Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
Write a SQL query to report the first name, last name, city, and state of each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.

Solution: Use LEFT JOIN to combine Person and Address tables on PersonId.
"""

# SQL Solution for LeetCode 175: Combine Two Tables
COMBINE_TWO_TABLES_SQL = """
SELECT 
    p.FirstName, 
       p.LastName, 
       a.City, 
       a.State
FROM Person p
LEFT JOIN Address a ON p.PersonId = a.PersonId;
"""

# Alternative SQL solution using explicit NULL handling
COMBINE_TWO_TABLES_SQL_ALT = """
SELECT 
    p.FirstName, 
    p.LastName, 
    a.City, 
    a.State
FROM Person p
LEFT JOIN Address a 
    ON p.PersonId = a.PersonId;
"""

# Explanation and test data simulation
def explain_combine_two_tables():
    """
    Explain the solution for combining two tables.
    """
    explanation = """
    Problem Analysis:
    - We need to combine data from Person and Address tables
    - Person table contains basic person information
    - Address table contains address information linked by PersonId
    - We want all persons from Person table, even if they don't have address info
    
    Solution Approach:
    - Use LEFT JOIN to keep all records from Person table (left table)
    - Match records from Address table (right table) where PersonId matches
    - If no match found in Address table, City and State will be NULL
    
    Why LEFT JOIN?
    - INNER JOIN would exclude persons without addresses
    - RIGHT JOIN would prioritize Address table (not what we want)
    - FULL OUTER JOIN is not needed as we want all persons
    
    Time Complexity: O(n + m) where n and m are table sizes
    Space Complexity: O(n + m) for the result set
    """
    return explanation


# Test data simulation (in-memory representation)
def simulate_combine_two_tables():
    """
    Simulate the SQL query result with sample data.
    """
    # Sample Person table data
    persons = [
        {"PersonId": 1, "FirstName": "Wang", "LastName": "Allen"},
        {"PersonId": 2, "FirstName": "Alice", "LastName": "Bob"}
    ]
    
    # Sample Address table data
    addresses = [
        {"AddressId": 1, "PersonId": 2, "City": "New York City", "State": "New York"}
    ]
    
    # Simulate LEFT JOIN
    result = []
    for person in persons:
        # Find matching address
        address = None
        for addr in addresses:
            if addr["PersonId"] == person["PersonId"]:
                address = addr
                break
        
        # Build result row
        result.append({
            "FirstName": person["FirstName"],
            "LastName": person["LastName"],
            "City": address["City"] if address else None,
            "State": address["State"] if address else None
        })
    
    return result


if __name__ == "__main__":
    print("SQL Solution:")
    print(COMBINE_TWO_TABLES_SQL.strip())
    print("\n" + "="*50 + "\n")
    
    print("Explanation:")
    print(explain_combine_two_tables())
    print("\n" + "="*50 + "\n")
    
    print("Simulation with sample data:")
    results = simulate_combine_two_tables()
    for row in results:
        print(row)