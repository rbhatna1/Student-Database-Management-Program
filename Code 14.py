import mysql.connector

database=mysql.connector.connect(host='localhost',user = 'root',password='tiger')
if database.is_connected()=="False":
    print("Could not connect to the database")
x=database.cursor()
x.execute("use sakila")

def creating_table():
    try:
        x.execute("CREATE TABLE student( No int(2) PRIMARY KEY, Name VARCHAR(10) NOT NULL, STIPEND int(3), Stream VARCHAR(15) NOT NULL, AVGMARKS int(3) NOT NULL,Grade  char(1) NOT NULL, Class int(2) NOT NULL)")
        print("The table has been sucessfully created")
        print()
    except:
        print("Sorry!!, we are unable to create it as it already exists")
        print()

def insert_rows():
    n=int(input("Enter the number of rows to be utilized"))
    for a in range(n):
        No=int(input("Enter the No"))
        Name=str(input("Enter the Name"))
        Stipend=int(input("Enter the Stipend"))
        Stream=str(input("Enter the Stream"))
        Avgmarks=int(input("Enter the Avgmarks"))
        Grade=str(input("Enter the Grade"))
        Class=int(input("Enter the Class"))
        x.execute("Insert into student VALUES({},'{}',{},'{}',{},'{}',{})".format(No,Name,Stipend,Stream,Avgmarks,Grade,Class))
        database.commit()
        print("Entering the data was successful")
        print()
        
def new_row():
    No=int(input("Enter the No"))
    Name=str(input("Enter the Name"))
    Stipend=int(input("Enter the Stipend"))
    Stream=str(input("Enter the Stream"))
    Avgmarks=int(input("Enter the Avgmarks"))
    Grade=str(input("Enter the Grade"))
    Class=int(input("Enter the Class"))
    x.execute("Insert into student VALUES({},'{}',{},'{}',{},'{}',{})".format(No,Name,Stipend,Stream,Avgmarks,Grade,Class))
    database.commit()
    print("Entering the data was successful")
    print()
    
def display_commerce():
    x.execute("Select * from student where Stream='Commerce'")
    a=x.fetchall()
    for i in a:
        print(i)
        print()

def display_entered_stream():
    stream=str(input("Enter the stream"))
    x.execute("Select * from student where Stream='{}'".format(stream))
    a=x.fetchall()
    for i in a:
        print(i)
        print()
        
def All_Students_Increating_table_Class_12():
    x.execute("Select name from student where Class=12")
    a=x.fetchall()
    for i in a:
        print(i)
        print()
        
def Details_All_Students_desc_order():
    x.execute("select * from student order by Avgmarks Desc")
    a=x.fetchall()
    for i in a:
        print(i)
        print()
        
def Stipend_notnull():
    x.execute("select Name,Stream,Stipend*12 from student where Stipend is not null")
    a=x.fetchall()
    for i in a:
        print(i)
        print()
        
def Count_C_Grade():
    x.execute("Select Count(Name) from student where Grade='C'")
    a=x.fetchall()
    for i in a:
        print(i)
        print()
        
def Name_start():
    x.execute("select Name from student where Name like 'V%'")
    a=x.fetchall()
    for i in a:
        print(i)
        print()
        
def update_stipend_300():
    x.execute("Update student set Stipend=Stipend+300 where Stream='Medical'")
    database.commit()
    x.execute("select * from student")
    a=x.fetchall()
    for i in a:
        print(i)
        print()

def Anil():
    x.execute("Delete from student where Name='Anil'")
    database.commit()
    x.execute("select * from student")
    a=x.fetchall()
    for i in a:
        print(i)
        print()
        
choice=0

while choice!=13:
    print("Choose from one of the folowing options")
    print("1)Choose 1 to create the table student")
    print("2)Choose 2 to insert the given rows into the table")
    print("3)Choose 3 to add a new row to the table by accepting values from the user")
    print("4)Choose 4 to display details of all the commerce stream students from the table")
    print("5)Choose 5 to display details of students belonging to user entered Stream")
    print("6)Choose 6 to list name of students who are in grade 12")
    print("7)Choose 7 to list the details of all students sorted by Avgmarks in descending orde")
    print("8)Choose 8 to display a report listing name, stream and stipend received in a year assuming that stipend is paid every month")
    print("9)Choose 9 to count the no of students with grade C")
    print("10)Choose 10 to display details of students whose name starts with ‘V'")
    print("11)Choose 11 to update stipend of Medical students by 300")
    print("12)Choose 12 to delete the details of Student Anil")
    print("13)Choose 13 to exit the program")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        creating_table()
        
    elif choice==2:
        insert_rows()
        
    elif choice==3:
        new_row()
        
    elif choice==4:
        display_commerce()
        
    elif choice==5:
        display_entered_stream()
        
    elif choice==6:
        All_Students_Increating_table_Class_12()
        
    elif choice==7:
        Details_All_Students_desc_order()
        
    elif choice==8:
        Stipend_notnull()
        
    elif choice==9:
        Count_C_Grade()
        
    elif choice==10:
        Name_start()
        
    elif choice==11:
        update_stipend_300()
        
    elif choice==12:
        Anil()

    