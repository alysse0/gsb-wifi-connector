import base64


# The password crypter.
def password_crypter(data):
    cryptedPassword = data.encode("ascii") 
    
    base64_bytes = base64.b64encode(cryptedPassword) 
    cryptedPassword = base64_bytes.decode("ascii")
    return cryptedPassword 

# The password decrypter.
def password_decrypter(password_crypted):
    originalPassword = password_crypted.encode("ascii") 
    
    originalPassword = base64.b64decode(originalPassword) 
    originalPassword = originalPassword.decode("ascii") 
    return originalPassword

