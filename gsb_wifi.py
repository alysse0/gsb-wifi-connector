import requests
import json
import xor

def send_request(user, password):
    r = requests.post("https://wifi.gsb.gov.tr/j_spring_security_check", data={"j_username" : user, "j_password" : password, "submit": "Login"})
    if "Invalid username/password." in r.text:
        print("invalid username/password")
    else:
        print("successfully logged in")

with open("data.json") as informationsOfPerson:
    outputInfos = json.loads(informationsOfPerson.read())
    username = outputInfos["tc"]
    crypted = outputInfos["pw"]


    
    originalUsername = str(xor.password_decrypter(username)).strip()
    originalPassword = str(xor.password_decrypter(crypted)).strip()
    
    send_request(originalPassword , originalPassword)