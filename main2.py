import re
import json

def checkUserName(dataInDic, userName):
    index = 0
    while (index < len(dataInDic['user'])):
        if(dataInDic['user'][index]['userName'] == userName):
            return True
    else:
        return "No"

def readJsonFile(fileName):
    openedJsonFile = open(fileName)
    readJsonFile = json.load(openedJsonFile)
    openedJsonFile.close()

def writeJsonFile(fileName, data):
    jsonData = json.dumps(data, indent = 4)
    jsonFile = open(fileName, 'w')
    jsonFile.write(jsonData)
    jsonFile.close()


signInSignUp = input("Sign-up(SU) or Sign-in(SI) :- ")
if (signInSignUp == "SU"):
    userName = input("User Name :- ")
    pswd1 = input("Password 1 :- ")
    pswd2 = input("Password 2 :- ")
    if(pswd1 != pswd2):
        print ("Both password are not same.")
    if(re.search('[0-9]',pswd1) is True):
        if("#" in pswd1 or "@" in pswd1):
            dataInDic = readJsonFile('userDetails.json')
            checked = checkUserName(dataInDic, userName)
            if(checked == "No"):
                newUser = {
                    "userName": userName,
                    "password": pswd1
                }
                dataInDic['user'].append(newUser)
                writeJsonFile('userDetails.json', dataInDic)
                print ("Congrats " + userName + "! You are Signed Up Successfully." )
            if(checked == True):
                print("User Name already Exist."
        # else:
        #     print ("Atleast password should contain one spacial character and one number.")
    # else:
    #     print ("Atleast password should contain one spacial character and one number.")




            
        
             