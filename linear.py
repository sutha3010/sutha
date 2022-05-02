def Linear_Search(listl,n,key):
    for i in range(0,n):
        if(listl[i]==key):
            return i
        return -1
    listl=[1,32,5,14,7,9]
    key=input("Element to be Searched:")
    print("Given array is:",list1)
    n=len(listl)
    res=Linear_Search(listl,n,key)
    if(res==-1):
        print("Element Not Found")
    else:
        print("Element Found at index:",res)
