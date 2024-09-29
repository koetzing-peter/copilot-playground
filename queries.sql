-- Give me a few examples of how you could help with writing sql queries

-- GitHub Copilot
-- Sure, here are a few examples of how I can help with writing SQL queries:

-- 1. Basic SELECT Query
-- Task: Retrieve all columns from a table named employees.
SELECT * FROM employees;

-- 2. SELECT with WHERE Clause
-- Task: Retrieve the names and salaries of employees who earn more than $50,000.
SELECT name, salary
FROM employees
WHERE salary > 50000;

-- 3. JOIN Query
-- Task: Retrieve the names of employees and their department names from employees and departments tables.
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 4. GROUP BY and HAVING
-- Task: Retrieve the count of employees in each department where the count is greater than 5.
SELECT department_id, COUNT(*)
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;

-- 5. INSERT Query
-- Task: Insert a new employee into the employees table.
INSERT INTO employees (name, department_id, salary)
VALUES ('John Doe', 3, 60000);

-- 6. UPDATE Query
-- Task: Update the salary of an employee with employee_id 1.
UPDATE employees
SET salary = 70000
WHERE employee_id = 1;

-- 7. DELETE Query
-- Task: Delete an employee with employee_id 1.
DELETE FROM employees
WHERE employee_id = 1;

-- These are just a few examples. Let me know if you need help with more complex queries or specific SQL functions