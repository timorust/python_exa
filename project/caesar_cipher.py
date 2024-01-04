def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            if not is_upper:
                shifted_char = shifted_char.lower()
            result += shifted_char
        else:
            result += char

    return result

text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
