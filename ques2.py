import pandas as pd 
student_data=[
    {'sname' : 1,'sage' : 1,'sroll': 1,'smarks' :1},
    {'sname' : 1,'sage' : 1,'sroll': 1,'smarks' :1},
    {'sname' : 1,'sage' : 1,'sroll': 1,'smarks' :1},
    {'sname' : 1,'sage' : 1,'sroll': 1,'smarks' :1},
    {'sname' : 1,'sage' : 1,'sroll': 1,'smarks' :1}
]
for i in range(5):
    name=input("enter your name :")
    roll_num=input("enter your roll number :")
    age=input("enter your age :")
    marks=int(input("Enter your marks out of 100 :"))
    while True:
        if marks>100:
            marks=int(input("Please re-enter your marks : "))
        else:
            break
    student_data[i]['sname']=name
    student_data[i]['sage']=roll_num
    student_data[i]['sroll']=age
    student_data[i]['smarks']=marks
student_data

x=pd.DataFrame(student_data, columns = ['sroll','sname','sage','smarks'])
x