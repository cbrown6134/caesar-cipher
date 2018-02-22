def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value > 126:
        unicode_value = unicode_value - 95
    elif unicode_value < 32:
        unicode_value = unicode_value + 95
    

    new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ''

    for letter in message:
        result += shift(letter, shift_amount)

    return result


def decrypt(message, shift_amount):
    return encrypt(message, -1 * shift_amount)

unencrypted_message = "She works two jobs to make ends meet; at least, that was her reason for not having time to join Obama for lunch."
encrypted_message = encrypt(unencrypted_message, 64)
decrypted_message = decrypt(encrypted_message, 64)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

