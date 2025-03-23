#Improvements from fixxx.py
#Made it so that it could contain spaces

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']

def encrypt(message,shift):
    #Takes a string then converts it into numbers
    number_from_text = [] 
    for i in message.lower():
        if i == " ":
            number_from_text.append(" ")
        else:
            num = keys.index(i)
            number_from_text.append(num)
    #Shift the numbers by the given "shift"
    encrypted_numbers = []
    for x in number_from_text:
        if x == " ":
            encrypted_numbers.append(" ")
        else:
            shifted_number = x + (shift % 26)
            if shifted_number > 25:
                index_from_start = shifted_number - 26 #to prevent value from reaching > 26 and to loop back again
                encrypted_numbers.append(keys.index(index_from_start))
            else:
                encrypted_numbers.append(shifted_number)
    #Converts numbers back into string
    encrypted_text = ""
    for y in encrypted_numbers:
        if y == " ":
            encrypted_text += " "
        else:
            encrypted_text += str(keys[y])
    return encrypted_text

def decrypt(message, shift):
    #converts string into numbers
    char_index = []
    for i in message.lower():
        if i == " ":
            char_index.append(" ")
        else:  
            char_index.append(keys.index(i))
    #Shift back the number by the given "shift"
    shifted_numbers = []
    for x in char_index:
        if x == " ":
            shifted_numbers.append(" ")
        else:
            shifted_number = x - shift % 26
            shifted_numbers.append(shifted_number)
    #converts numbers into string
    decrypted_text = ""
    for y in shifted_numbers:
        if y == " ":
            decrypted_text += " "
        else:
            decrypted_text += keys[y]
    return decrypted_text


encrypted = encrypt("Hello world", 3)
print(encrypted) 
print(decrypt(encrypted, 3))    