# Markhus Dammar
# 22 October 2021
# This program will decrypt messages using the shift


def encryptMessage(message, key):
    message = message.upper()
    encrypted_text = ""
    for letter in message:
        shifted_text = ord(letter) + key
        if shifted_text < 65:
            shifted_text += 26
        if shifted_text > 90:
            shifted_text -= 26
        encrypted_text += chr(shifted_text)
    return encrypted_text


user_text = input("Enter a message to encrypt >>>")
shift = int(input("How many shall we shift the message by?"))

while shift < 1 or shift % 26 == 0:
    print("Error, stay within range")
    shift = int(input("How many shall we shift the message by?"))

print("The original message is as follows: " + user_text)
print("Here is the encrypted message: " + encryptMessage(user_text, shift))





