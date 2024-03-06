import requests
import json
import xor
import base64



def send_request(user, password):
    r = requests.post("https://wifi.gsb.gov.tr/j_spring_security_check", data={"j_username" : user, "j_password" : password, "submit": "Login"})
    if "Invalid username/password." in r.text:
        print("invalid username/password")
    else:
        print("successfully logged in")


#open the json file.
with open("data.json") as informationsOfPerson:
    outputInfos = json.loads(informationsOfPerson.read())
    username = outputInfos["tc"]
    crypted = outputInfos["pw"]
    xor_key = outputInfos["xor_key"]
    
    originalUsername = str(xor.originalPasswordGetter(base64.b64decode(username).decode(), xor_key)).strip()
    originalPassword = str(xor.originalPasswordGetter(base64.b64decode(crypted).decode(), xor_key)).strip()
    
    send_request(originalUsername , originalPassword)