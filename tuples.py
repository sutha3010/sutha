input_tuple=final_tuple=()
flag=False
n=int(input("Enter the number of students:"))
print("Enter the Name,Roll no and Average marks of 5 subjects of",n,"Students")
for i in range(0,n):
   name=raw_input("Enter the name:")
   roll_no=input("Enter the roll no:")
   marks=input("Enter the student average marks:")
   per_marks=(int(marks)*100)/500
   input_tuple=(name,roll_no,marks,per_marks,)
   final_tuple=final_tuple+(input_tuple,)
input_roll=input("Please enter the students roll no for results:")
for x in final_tuple:
    if x[1] == input_roll:
         flag=True
         if int(x[3]) in range(0,34):
              print("Name:",x[0],"Roll_Number:",x[1],"Failed")
         elif int(x[3]) in range(35,49):
              print("Name:",x[0],"Roll_Number:",x[1],"Pass class")
         elif int(x[3]) in range(50,59):
              print("Name:",x[0],"Roll_Number:",x[1],"Second class")
         elif int(x[3]) in range(60,69):
              print("Name:",x[0],"Roll_Number:",x[1],"First class")
         elif int(x[3]) in range(70,100):
              print("Name:",x[0],"Roll_Number:",x[1],"First class with distinction")
if flag == False:
       print("Record not found")
