import re
remail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def checkemail(email):
    if(re.search(remail,email)):
        return True
    else:
        return False

rname = '^[A-Za-z]'
def checkname(name):
    if(re.match(rname,name)):
        return True
    else:
        return False

def checkgender(gen):
    if(gen=='Male' or gen=='Female'):
        return True
    else:
        return False

def checkage(age):
    if(age>0):
        return True
    else:
        return False

rcon = '^[0-9]{10}'
def checkcontact(num):
    if(re.search(rcon,num)) and len(num)==10:
        return True
    else:
        return False
