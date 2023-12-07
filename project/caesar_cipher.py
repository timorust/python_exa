def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            is_upper = char.isupper()
            # Convert the character to uppercase for easier manipulation
            char = char.upper()
            # Apply the Caesar cipher shift
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Convert back to lowercase if the original character was lowercase
            if not is_upper:
                shifted_char = shifted_char.lower()
            result += shifted_char
        else:
            # If the character is not alphabetic, leave it unchanged
            result += char

    return result

# Example usage
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
