BASIC SQL 2:

1. Write a query to display employee first name, last name, and department name for all employees.
SELECT e.first_name, e.last_name, d.dept_name 
FROM employees e 
LEFT JOIN departments d ON e.department_id = d.dept_id

2. Write a query to display first name, last name, and department name of employees who work in the IT department.
SELECT e.first_name, e.last_name, d.dept_name 
FROM employees e 
LEFT JOIN departments d ON e.department_id = d.dept_id
WHERE d.dept_name = 'IT'

3. Write a query to display employee first name, last name, department name, and city for all employees. 
SELECT e.first_name, e.last_name, d.dept_name, l.city 
FROM employees e 
LEFT JOIN departments d ON e.department_id = d.dept_id
LEFT JOIN locations l ON d.location_id = l.location_id

4. Write a query to display employee first name, last name, department name, and city for employees who work in the city 'London'.
SELECT e.first_name, e.last_name, d.dept_name, l.city 
FROM employees e 
LEFT JOIN departments d ON e.department_id = d.dept_id
LEFT JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London'

5. Write a query to display:
Tables: employees, jobs
first_name
last_name
job_title
for all employees.
SELECT e.first_name, e.last_name, j.job_title
FROM employees e 
LEFT JOIN jobs j ON e.job_id = j.job_id

6. ables: employees, jobs

📝 Write a query to display:

first_name

last_name

job_title

Only for employees whose job title is ‘Programmer’.

SELECT e.first_name, e.last_name, j.job_title
FROM employees e 
LEFT JOIN jobs j ON e.job_id = j.job_id
WHERE j.job_title = 'Programmer'
