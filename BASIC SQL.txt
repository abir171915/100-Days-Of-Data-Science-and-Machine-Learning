BASIC SQL:

1. Write a query to display the first name, last name, and hire date of all employees.
SELECT first_name, last_name, hire_date FROM employees

2. Write a query to display the first and last name of employees who were hired after January 1, 2005.
SELECT first_name, last_name FROM employees
WHERE hire_date > '2005-1-1'

3. Write a query to display employee_id, first_name, salary of all employees, sorted by salary in descending order.
SELECT emp_id, first_name, salary FROM employees
ORDER BY salary DESC

4.  Write a query to display employee_id, first_name, salary of employees who earn more than 8000, sorted by salary ascending. 
SELECT emp_id, first_name, salary FROM employees
WHERE salary > 8000
ORDER BY salary ASC

5. Write a query to find the highest salary among all employees.
SELECT MAX(salary) AS MAX_SAL FROM employees

6. Write a query to find the average salary per department.
SELECT department_id, AVG(salary) AS avg_sal FROM employees
GROUP BY department_id


