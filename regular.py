import re
txt="The rain in spain"
x=re.search("^The.*spain$",txt)
if x:
    print("Yes!we have a match!")
else:
    print("No match")
x=re.findall("ai",txt)
print(x)
x=re.search("\s",txt)
print("The First Whitespace character is located in postion:",x.start())
x=re.split("\s",txt)
print(x)                                     
x=re.split("\s",txt,1)
print(x)
x=re.sub("\s","9",txt)
print(x)
x=re.subn("\s","9",txt,2)
print(x)
x=re.search(r"\bs\w+",txt)
print(x.span())
print(x.string)
print(x.group())
                                        
                                       
                                       
