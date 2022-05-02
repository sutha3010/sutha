import sys
randomlist=['a',8]
for entry in randomlist:
    try:
        print("The entry is",entry)
        r=10/int(entry)
        break
    except:
        print("OOPS!",sys.exc_info()[0],"occured")
        print("Next Entry")
print("The reciprocal of ",entry,"is",r)
