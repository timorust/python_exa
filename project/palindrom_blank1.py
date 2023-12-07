def clean(str):
        cleaned_string = ''.join(char.lower() for char in str if char.isalnum())
        return cleaned_string

def is_palindrome(string):
    cleaned_string = clean(string)
    return cleaned_string == cleaned_string[::-1]

# Test cases
print(is_palindrome("hello"))
print(is_palindrome("annna"))  # Output: True
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True

#tests:
a = "אבא"
b = "annna"
c = "A man, a plan, a canal, Panama"
d = "annna0"
e = "detective"
f = "אמוץ"
j = "hello"


if is_palindrome(a) == True: print(f"correct! '{a}' is a Palindrom") 
else: print(f"Wrong! {a} is a Palindrom") 

if is_palindrome(b) == True: print(f"correct! '{b}' is a Palindrom") 
else: print(f"Wrong! {b} is a Palindrom")

if is_palindrome(c) == True: print(f"correct! '{c}' is a Palindrom") 
else: print(f"Wrong! {c} is a Palindrom") 

if is_palindrome(d) != True: print(f"correct! '{d}' is not a Palindrom") 
else: print(f"Wrong! {d} is not a Palindrom")

if is_palindrome(e) != True: print(f"correct! '{e}' is not a Palindrom") 
else: print(f"Wrong! {e} is not a Palindrom") 

if is_palindrome(f) != True: print(f"correct! '{f}' is not a Palindrom") 
else: print(f"Wrong! {f} is not a Palindrom")

if is_palindrome(j) != True: print(f"correct! '{j}' is not a Palindrom") 
else: print(f"Wrong! {j} is not a Palindrom")