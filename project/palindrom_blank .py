def clean_char(string):
  return ''.join(char.lower() for char in string if char.isalnum())


def is_palindrome(string):
    cleaned_string = clean_char(string)
    return cleaned_string == cleaned_string[::-1]



print(is_palindrome("hello"))
print(is_palindrome("annna"))
print(is_palindrome("A man, a plan, a canal, Panama"))



