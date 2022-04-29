import sys
rL = ['a',4]
for entry in rL:
    try:
        print("The entry is", entry)
        rL = 10/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "Occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is", rL)
