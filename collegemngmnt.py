import mysql.connector as mysql

db=mysql.connect(host="localhost",user="root",password="",database="collegemanagement")
conn=db.cursor(buffered=True)

def teacher_func():
    while 1:
        print("LOGIN SUCCESS!! WELCOME PROFESSOR")
        print("------------------------------------")
        print("MENU")
        print("------------------------------------")
        print("1.Mark Student Register")
        print("2.View Student Register")
        print("3.Logout")
        print("------------------------------------")
        user_option=input(str("Select an option: "))
        if user_option=="1":
            print("------------------------------------")
            print("Mark Student Register")
            conn.execute("SELECT UserName FROM users WHERE Privilege='Student'")
            records=conn.fetchall()
            date=input(str("Enter Date (DD/MM/YYYY): "))
            for record in records:
                record=str(record).replace("'","")
                record=str(record).replace(",","")
                record=str(record).replace("(","")
                record=str(record).replace(")","")
                status=input(str("Status for "+ str(record)+"  P/A/L: "))
                values=(str(record),date,status)
                conn.execute("INSERT INTO attendance(UserName,Date,Status)VALUES(%s,%s,%s)",values)
                db.commit()
                print(record+" Marked as "+status+" on "+date)
        elif user_option=="2":
            print("------------------------------------")
            print("View Student Register")
            conn.execute("SELECT UserName,Date,Status FROM attendance")
            records=conn.fetchall()
            print("Displaying all records")
            for record in records:
                print(record)
        elif user_option=="3":
            main()
        else:
            print("Please enter a valid option!")

def student_func(username):
    while 1:
        print("LOGIN SUCCESS!! WELCOME")
        print("------------------------------------")
        print("MENU")
        print("------------------------------------")
        print("1.View Register")
        print("2.Download Register")
        print("3.Logout")
        print("------------------------------------")
        user_option=input(str("Select an option: "))
        if user_option=="1":
            print("Displaying Register.....")
            username=(str(username),)
            conn.execute("SELECT Date,UserName,Status FROM attendance WHERE UserName=%s",username)
            records=conn.fetchall()
            for record in records:
                print(record)
        elif user_option=="2":
            print("Downloading Register....")
            username=(str(username),)
            conn.execute("SELECT Date,UserName,Status FROM attendance WHERE UserName=%s",username)
            records=conn.fetchall()
            for record in records:
                with open("C:/Users/admin/Desktop/CollegeManagement/register.txt","w") as reg:
                    reg.write(str(records)+"\n")
                reg.close()
                print("All records saved successfully...")
        elif user_option=="3":
            main()
        else:
            print("Please enter a valid option")

def admin_func():
    while 1:
        print("LOGIN SUCCESS!! WELCOME ADMIN")
        print("------------------------------------")
        print("MENU")
        print("------------------------------------")
        print("1.Register new Student")
        print("2.Register new Teacher")
        print("3.Delete exisiting Student")
        print("4.Delete existing Teacher")
        print("5.Logout")
        print("------------------------------------")
        user_option=input(str("Select an option: "))
        if user_option=="1":
            print("Register new Student")
            print("------------------------------------")
            username=input(str("Enter username:"))
            password=input(str("Enter passowrd: "))
            values=(username,password)
            conn.execute("INSERT into users(UserName,Password,Privilege) VALUES(%s,%s,'Student')",values)
            db.commit()
            print(username+" has been registered as a Student succesfully!!")
            admin_func()
        elif user_option=="2":
            print("Register new Teacher")
            print("------------------------------------")
            username=input(str("Enter username:"))
            password=input(str("Enter passowrd: "))
            values=(username,password)
            conn.execute("INSERT into users(UserName,Password,Privilege) VALUES(%s,%s,'Teacher')",values)
            db.commit()
            print(username+" has been registered as a Teacher succesfully!!")
            admin_func()
        elif user_option=="3":
            print("Delete existing student")
            print("------------------------------------")
            username=input(str("Enter Student's username:"))
            values=(username,"Student")
            conn.execute("DELETE FROM users WHERE UserName= %s AND Privilege=%s",values)
            db.commit()
            if conn.rowcount<1:
                print("User Not Found!!")
            else:
                print("Student "+username+" has been removed from the database successfully")
            admin_func()
        elif user_option=="4":
            print("Delete existing Teacher")
            print("------------------------------------")
            username=input(str("Enter Teacher's username:"))
            values=(username,"Teacher")
            conn.execute("DELETE FROM users WHERE UserName= %s AND Privilege=%s",values)
            db.commit()
            if conn.rowcount<1:
                print("User Not Found!!")
            else:
                print("Teacher "+username+" has been removed from the database successfully")
            admin_func()
        elif user_option=="5":
            break
        else:
            print("Please enter a valid option")

def student():
    print("------------------------------------")
    print("Student's Login")
    print("------------------------------------")
    username=input(str("Enter UserName: "))
    password=input(str("Enter Password: "))
    values=(username,password,'Student')
    conn.execute("SELECT * FROM users WHERE UserName=%s AND Password=%s AND Privilege=%s",values)
    if conn.rowcount<=0:
        print("Failed to login")
    else:
        student_func(username)

def teacher():
    print("------------------------------------")
    print("Teacher's Login")
    print("------------------------------------")
    username=input(str("Enter UserName: "))
    password=input(str("Enter Password: "))
    values=(username,password)
    conn.execute("SELECT * FROM users WHERE UserName=%s AND Password=%s AND Privilege='Teacher'",values)
    if conn.rowcount<=0:
        print("Failed to login")
    else:
        teacher_func()

def admin():
    print("------------------------------------")
    print("Admin Login")
    print("------------------------------------")
    username=input(str("Enter UserName: "))
    password=input(str("Enter Password: "))
    if username=="admin":
        if password=="pass@123":
            admin_func()
        else:
            print("Incorrect Password")
    else:
        print("Invalid credentials!!!")

def main():
    while 1:
        print("Welcome to our management system!!!!")
        print("------------------------------------")
        print("1.Student Login")
        print("------------------------------------")
        print("2.Login as Teacher")
        print("------------------------------------")
        print("3.Admin Login")
        print("------------------------------------")
        user_option=input(str("Please Select an option to continue or press q to quit: "))
        if user_option=="1":
            student()
        elif user_option=="2":
            teacher()
        elif user_option=="3":
            admin()
        elif user_option=='q':
            break
        else:
            print("Please select a valid option")
main()

