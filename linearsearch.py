listl=[]
n=int(input("Enter an array size:"))
print("Enter Elements one by one")
for i in range(0,n):
    listl.append(input())
print("Created the Linear Search:")
print(listl)
def Linear_Search(listl,n,key):
    for i in range(0,n):
        if(listl[i]==key):
            return i
    return -1
key=input("Element to be Searched:")
n=len(listl)
res=Linear_Search(listl,n,key)
if(res==-1):
    print("Elements Not found")
else:
    print("Element found at index:",res)
