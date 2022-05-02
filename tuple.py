input_tuple=final_tuple=()
flag=False
n=int(input("enter The number of students:"))
print("Enter the name,roll_no and Average marks of 5 subjects of",n,"students")
for i in range(0,n):
    name=raw_input("enter the name:")
    roll_no=input("enter the roll_no:")
    marks=input("Enter the Student Average marks:")
    per_marks=(int(marks)*100)/500
    input_tuple=(name,roll_no,marks,per_marks,)
    final_tuple=final_tuple+(input_tuple,)
input_roll=input("please enter the students roll_no for results:")
for x in final_tuple:
    if x[1]==input_roll:
        flag=True
        if int(x[3])in range (0,34):
            print("Name:",x[0],"Roll_number",x[1],"Failed")
        elif int(x[3])in range(35,49):
            print("Name:",x[0],"Roll_number",x[1],"Pass class")
        elif int(x[3])in range(50,59):
            print("Name:",x[0],"Roll_number",x[1],"second class")
        elif int(x[3])in range(60,69):
            print("Name:",x[0],"Roll_number",x[1],"First class")
        elif int(x[3])in range(70,100):
            print("Name:",x[0],"Roll_number",x[1],"First class with Distinction")
if flag==False:
  print("Record Not found")

                                                 
                      
