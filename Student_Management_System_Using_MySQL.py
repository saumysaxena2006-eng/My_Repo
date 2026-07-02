import mysql.connector as sql
myCon = sql.connect(host="localhost", passwd="root", user="root", database="College")
if myCon.is_connected():
    cursor = myCon.cursor()
    print("---STUDENT MANAGEMENT SYSTEM---")
    while True:
        print("1-> Show Student List\n2-> Add New Student\n3-> Get A Student's Details\n4-> Update Details")
        print("5-> Delete Student Info\n6-> Exit Program ")
        ch = input("Enter your choice:")
        if ch.isalpha():
            ch.lower()
        if ch == "1" or ch == "show student list":
            print("Details of Students are:")
            cursor.execute("Select * from Student")
            data = cursor.fetchall()
            if data is None:
                print("Empty Set")
            else:
                for detail in data:
                    print(detail)
            continue
        elif ch == "2" or ch == "add new student":
            ID = int(input("Enter New ID:"))
            Name = input("Enter Your Name:")
            Roll_No = int(input("Enter Allotted Roll_No:"))
            Address = input("Enter Your Address:")
            Mobile = int(input("Enter Your Mobile_No:"))
            ABC = int(input("Enter your ABC ID:"))
            cursor.execute(f"insert into Student values({ID},{Name},{Roll_No},{Address},{Mobile}, {ABC})")
            myCon.commit()
            print("Data Inserted Successfully")
            continue
        elif ch == "3" or ch == "get a student's details":
            ID = int(input("Enter Your ID"))
            print("Your Details Are:")
            cursor.execute(f"select * from Student where ID={ID}")
            data = cursor.fetchone()
            if data is None:
                print("Empty Set")
            else:
                print(data)
            continue
        elif ch == "4" or ch == "update details":
            opt = int(input("Enter Your Data which has to be updated:\n1=> Address\n2=> Mobile_No "))
            if opt == 1:
                ID = int(input("Enter Your ID:"))
                add = input("Enter Your New Address:")
                cursor.execute(f"update Student set Address='{add}' where id={ID}")
                myCon.commit()
                print("Data Updated Successfully!")
                continue
            elif opt == 2:
                ID = int(input("Enter Your ID:"))
                mob = input("Enter Your New Mobile No.:")
                cursor.execute(f"update Student set Address='{mob}' where id={ID}")
                myCon.commit()
                print("Data Updated Successfully!")
                continue
            else:
                raise Exception("Invalid Entry")
        elif ch == "5" or ch == "delete student info":
            ID = int(input("Enter your ID:"))
            cursor.execute(f"delete from Student where id={ID}")
            myCon.commit()
            print("Data Deleted Successfully!")
            continue
        else:
            break
else:
    raise Exception("Database Not Found")
