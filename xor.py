import base64


# The password crypter.
def password_crypter(data, xor_key):
    j = 0
    crypted = ""
    for i in range(len(data)):
        crypted += chr(ord(data[i]) ^ ord(xor_key[j]))
        j += 1
        if j == len(xor_key):
            j = 0
    
    cryptedInBase64 = base64.b64encode(crypted.encode()).decode()
    return cryptedInBase64

decrypted = (password_crypter("37588622652", "ma24fall"))

#The password decrypter.
def password_decrypter(password_crypted, xor_key):
    j = 0
    decrypted = ""

    for i in range(len(password_crypted)):
        decrypted += chr(ord(password_crypted[i]) ^ ord(xor_key[j]))
        j += 1
        if j == len(xor_key):
            j = 0
    
    return decrypted

decryptedInBase64 = base64.b64decode(decrypted).decode() 


#print(password_decrypter(decryptedInBase64, "ma24fall"))

#Getting the decrypted forms.
def originalPasswordGetter(decryptedInBase64, xor_key):
    return password_decrypter(decryptedInBase64, xor_key)
