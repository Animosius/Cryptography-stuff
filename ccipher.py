#making a caesar cipher
#Note to self
#Optimize this, fix the damn issue (KeyError)

keys = {
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H",
    9:"I",
    10:"J",
    11:"K",
    12:"L",
    13:"M",
    14:"N",
    15:"O",
    16:"P",
    17:"Q",
    18:"R",
    19:"S",
    20:"T",
    21:"U",
    22:"V",
    23:"W",
    24:"X",
    25:"Y",
    26:"Z",
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26,
}

def encrypt(message,shift):
    message = str(message)
    shift = int(shift)
    text_to_number = [] #Changes text into number 
    for i in message.upper():
        if i == " ":
            text_to_number.append(" ")
        else:
            text_to_number.append(keys[i]) 
    #Shift numbers and store them in shifted_number
    #encrypting starts here
    shifted_numbers = [] 
    for x in text_to_number: 
        if x == " ":
            shifted_numbers.append(" ")
        else:
            added_number = x + shift
            if added_number > 26:
                special_added_number = added_number % 26
                shifted_numbers.append(special_added_number)
            else:
                shifted_numbers.append(added_number) 
    #encrypting ends here
    encrypted_text = "" #translate shifted number into text
    for y in shifted_numbers:
        if y == " ":
            encrypted_text += " "
        else:
            encrypted_text += keys[y]
    return encrypted_text

def decrypt(message, shift):
    message = str(message)
    shift = int(shift)
    text_to_number = [] #changes text into number
    for i in message.upper():
        if i == " ":
            text_to_number.append(" ")
        else:
            text_to_number.append(keys[i])
    shifted_numbers = [] #shift numbers and stores them in shifted_number
    #decrypting process start
    for x in text_to_number:
        if x == " ": 
            shifted_numbers.append(" ")
        else:
            substracted_number = x - shift 
            if substracted_number < 0:
                special_substracted_number = 26 - (x - (shift % 26)) 
                shifted_numbers.append(special_substracted_number)
            else:
                shifted_numbers.append(substracted_number) 
    #decrypting process end
    decrypted_text = "" #changes number into text
    for y in shifted_numbers:
        if y == " ":
            decrypted_text += " "
        else:
            decrypted_text += keys[y]
    return decrypted_text


message = "Hello world"
shift = 24
print(f"The message is: {message}")
print(f"The shift is: {shift}")
encrypted_message = encrypt(message=message, shift=shift)
decrypted_message = decrypt(encrypted_message, shift=shift)
print(f"Encrypted_message: {encrypted_message}")
print(f"decrypted_message: {decrypted_message}")
if decrypted_message == message:
    print("Test is successful \n You've done it")
else:
    print("Test failed")


