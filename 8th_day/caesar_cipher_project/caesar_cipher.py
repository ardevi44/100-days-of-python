alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# The resulting encrypted or decrypted message
result = ""


def encrypt(original_text, shift_amount):
    alphabet_last_index = len(alphabet) - 1  # Last index of the alphabet
    encrypted_result = ""
    for letter in original_text:
        if not letter in alphabet:  # If is some other letter not in alphabet just add this
            encrypted_result += letter
            continue
        shifted_index = alphabet.index(letter) + shift_amount
        if shifted_index > alphabet_last_index:  # We're out of bounds
            # The difference between last and the current index
            indexes_diff = alphabet_last_index - alphabet.index(letter)
            encrypted_result += alphabet[shift_amount - indexes_diff - 1]
        else:
            encrypted_result += alphabet[alphabet.index(letter) + shift_amount]
    if len(encrypted_result) != 0:
        return encrypted_result
    else:
        return 0


def decrypt(original_text, shift_amount):
    decrypted_result = ""
    for letter in original_text:
        if not letter in alphabet:
            decrypted_result += letter
            continue
        shifted_index = alphabet.index(letter) - shift_amount
        decrypted_result += alphabet[shifted_index]
    if len(decrypted_result) != 0:
        return decrypted_result
    else:
        return 0


direction = ""
while direction != "\x04":
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt or Ctrl + D to exit the program:\n").lower()
    if direction == "encode":
        original_text = input("Type your message:\n").lower()
        shift_amount = int(input("Type the shift number:\n"))
        result = encrypt(original_text=original_text,
                         shift_amount=shift_amount)
        print(result)
    elif direction == "decode":
        original_text = input("Type your message:\n").lower()
        shift_amount = int(input("Type the shift number:\n"))
        result = decrypt(original_text=original_text,
                         shift_amount=shift_amount)
        print(result)
    else:
        print("Bye bye...")
