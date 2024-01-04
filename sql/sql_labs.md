#SQL LABS

1.[Finding Patients from Hamilton with Allergies Using SQL]
(https://codedamn.com/problem/D3DM-IpnYIZtDzBJEbFpb)

Finding Patients from Hamilton with Allergies Using SQL

Write an SQL query to find a list of patients' first_name, last_name, and allergies who are from the city of Hamilton and have non-null values in the allergies column.

Tables Used: patients
Important Concepts
SQL Keywords: Understanding SQL keywords like SELECT, FROM, and WHERE will be essential.
NULL Values: Know how to handle NULL values in SQL, especially when you want to include or exclude them in your results.
Good luck!

plan:

select:
(columns) first_name, last_name, allergies

from:
(table) patients

where:
(expressions)
city of Hamilton and
non-null values in the allergies column.

solution:

```sql
SELECT first_name,last_name,allergies FROM 'patients' where allergies != 'null' and city = 'Hamilton'
```

2.[Filtering and Sorting Customer Data by City and Contact Name in SQLite]
(https://codedamn.com/problem/uwLBw_QmCxdpHK-r88GAY)

Filtering and Sorting Customer Data by City and Contact Name in SQLite
Easy

Introduction
In this lab, you will be working with the SQLite database northwind.sqlite. Your main task is to construct an SQL query to retrieve specific information from the customers table.

Objective
Your SQL query should fulfill the following requirements:

Retrieve the city, company_name, and contact_name columns from the customers table.
Filter the records to only include rows where the city name contains the letter 'L'.
Sort the resulting data set by contact_name in ascending order.
Key Concepts
To complete this lab, you should be familiar with the following SQL operations:

SELECT for specifying the columns you want to retrieve
WHERE for filtering rows based on a condition
ORDER BY for sorting the results
Good luck!

plan:
SELECT (columns)
city, company_name, contact_name

FROM(tables)
customers

WHERE (expression)
city name contains the letter 'L'

ORDER BY
Sort the resulting data set by contact_name in ascending order.

solution:

```sql
SELECT city, company_name, contact_name FROM 'customers' where city like '%L%' ORDER BY contact_name ASC
```

3.[Finding the Tallest Patient's Name and Height]
(https://codedamn.com/problem/Cv13HZLsoEPU3NyW4AVYc)

Finding the Tallest Patient's Name and Height
Easy

Your goal is to retrieve specific information about patients based on certain criteria. Specifically, you are tasked with the following:

Retrieve the first_name, last_name, and height of the patient with the greatest height from the patients table
Schema
Schema of the patients table for reference

patient_id
first_name
last_name
gender
birth_date
city
province_id
allergies
height
weight
Concepts:
SELECT Statement: Used to select data from a database. The result is then stored in a result table.
Aggregate Functions: SQL aggregate functions return a single value, calculated from values in a column. The function MAX() is one such function which returns the maximum value of the selected column.

plan:

SELECT (columns)
first_name, last_name, height

FROM(tables)
patients

WHERE (expression)

solution:

```sql
SELECT first_name, last_name, MAX(height) as height FROM 'patients'
```

4. [Filtering Patients by Specific IDs in a Hospital Database]
   (https://codedamn.com/problem/6Q_jz6_gzvEhEy_qEkGtu)

Filtering Patients by Specific IDs in a Hospital Database
Easy

The database focuses on hospital data, and for this particular exercise you'll be using the patients table.

Schema
patients table schema

patient_id
first_name
last_name
gender
birth_date
city
province_id
allergies
height
weight
Task
Write a SQL query to show all columns for patients who have specific patient_ids: 1, 45, 534, 879, 1000.

Concepts to Know
SELECT: To specify the columns you want to retrieve.
WHERE: To filter the records based on certain conditions.
IN: To specify multiple values in a WHERE clause.
Remember, the focus here is not just on getting the right answer, but also on understanding the SQL concepts being applied.

Good luck!

plan:

SELECT (columns)

-

FROM (tables)
patients

WHERE(expression)
patient_ids
IN (1, 45, 534, 879, 1000)

```sql
SELECT * FROM 'patients' where patient_id in (1, 45, 534, 879, 1000)
```

5. [Counting Total Admissions for a Specific Patient in a Hospital Database]
   (https://codedamn.com/problem/fnMulyhVKEw_WhMHbc9S0)

Counting Total Admissions for a Specific Patient in a Hospital Database

Write an SQL query to show the patient id and the total number of admissions for a patient with a patient_id of 579. Your query should return the patient_id and the total count of admissions for that patient with the column name alias total_admissions

Tables Used: admissions
Concepts
SELECT: To specify the columns you want in your result set.
COUNT(): An aggregate function to count the number of rows.
WHERE: To filter the records based on a condition.
Remember, your query should be compatible with SQLite syntax. Good luck!

plan:

SELECT (columns)
patient id
count() as total_admissions

and the total number of admissions

FROM (tables)
admissions

WHERE(expression)
patient_id = 579

```sql
SELECT patient_id, count(patient_id) as total_admissions  FROM 'admissions' where patient_id = 579
```

6. [Calculating Weight Difference for Maroni Patients in SQLite]
   (https://codedamn.com/problem/t8pOvulqE9FCk8TqvjjO9)

Calculating Weight Difference for Maroni Patients in SQLite

Your task is to write an SQL query to find the difference between the largest and smallest weight among patients with the last name 'Maroni'.

Concepts
SELECT: To specify the columns that should be returned in the result set.
MAX(): SQL function to get the maximum value in a numeric dataset.
MIN(): SQL function to get the minimum value in a numeric dataset.
WHERE: To filter records based on specific conditions.
Requirements
Your query should only return a single column named weight_delta that contains the weight difference.
You must use the patients table
Your query should run without errors to pass the lab.
Good luck!

plan:

SELECT (columns)

max(weight) - min(weight) as weight_delta

FROM (tables)
patients

WHERE(expression)
last_name = 'Maroni'

```sql
SELECT max(weight) - min(weight) as weight_delta FROM 'patients' where last_name = 'Maroni'
```

7. [Retrieve Even-Numbered Order IDs from the Orders Table]
   (https://codedamn.com/problem/HSRUdKYRltVmmVAvZOQOj)

Retrieve Even-Numbered Order IDs from the Orders Table

Retrieve all the even-numbered Order_id from the orders table.

Concepts to Review:
SELECT Statement: The fundamental SQL command used to retrieve data from a table.
WHERE Clause: Used in SQL to filter records based on specific conditions.
MOD Function: In SQL, the MOD function returns the remainder of a division. For example, MOD(column_name, n) will give the remainder when column_name is divided by n.
Your goal is to combine these concepts effectively to retrieve the desired data from the orders table. Good luck!

plan:

SELECT (columns)
Order_id

FROM (tables)
orders

WHERE(expression)

```sql

```
