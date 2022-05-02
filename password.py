import re
password=raw_input("enter the password:")
while True:
    if(len(password)<8):
        flag=-1
        break
    elif not re.search("[a-z]",password):
        flag=-1
        break
    elif not re.search("[A-Z]",password):
        flag=-1
        break
    elif not re.search("[0-9]",password):
        flag=-1
        break
    elif not re.search("[-@$]",password):
        flag=-1
        break
    else:
        flag=0
        print("Valid paasword")
        break
if flag==-1:
    print("InValid paasword")
    
