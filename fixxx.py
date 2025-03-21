#Note to self
#Make it so that the result can contain spaces

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']

def encrypt(message,shift):
    number_from_text = []
    for i in message.lower():
        if i == " ":
            i = ""
        else:
            num = keys.index(i)
            number_from_text.append(num)
    encrypted_numbers = []
    for x in number_from_text:
        shifted_number = x + (shift % 26)
        if shifted_number > 25:
            index_from_start = shifted_number - 26 #to prevent value from reaching > 26 and to loop back again
            encrypted_numbers.append(keys.index(index_from_start))
        else:
            encrypted_numbers.append(shifted_number)
    encrypted_text = ""
    for y in encrypted_numbers:
        encrypted_text += keys[y]
    return encrypted_text

def decrypt(message, shift):
    char_index = []
    for i in message.lower():
        if i == " ":
            i = ""
        else:  
            char_index.append(keys.index(i))
    shifted_numbers = []
    for x in char_index:
        shifted_number = x - shift % 26
        shifted_numbers.append(shifted_number)
    decrypted_text = ""
    for y in shifted_numbers:
        decrypted_text += str(keys[y])
    return decrypted_text


encrypted = encrypt("Hello world", 3)
print(encrypted) 
print(decrypt(encrypted, 3))    