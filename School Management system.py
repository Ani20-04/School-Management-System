import mysql.connector as sqlcon
conn=sqlcon.connect(host='localhost',user='root',passwd='anirudh09082004',database='project_term_2')
import pandas as pd
import numpy as np

## Enter s and v
print("                          School Management System                    ")
print()
print("[Enter U for Updating the deatils of Students, Teachers & Fees]")
print("===============================================================")
print("[Enter V for Viewing the deatils of Students, Teachers & Fees]")
print("===============================================================")
print()
mode=str(input("Enter (U AND V) here: "))
print()


if mode == 'U':
          print("                         !Welcome to Updating mode!                    ")
          print("                         --------------------------                    ")
          print()
          print("1) To Maintain Students-details")
          print("2) To Maintain Teachers-details")
          print("3) To Maintain Fees of Students")
          print("(To Go Back, Enter 0)")
          print()

          
         
select=int(input("Choose: "))
print()

while select < 4:
           print("1) Add a Student= ")
           print("2) Edit a Student= ")
           print("3) remove a Student= ")
           print("(To Go Back, Enter 0)")
           print()
           csr=conn.cursor()
           main=int(input("Choose: "))
           print()
           while main < 4:
         
              if main == 0:
                    break
              elif main == 1:
                    Rollno=input("Enter the Rollno of the student= ")
                    Name=input("Enter the Name of the student= ")
                    Dateofadmi=input("Enter the Date_of_admission of the student= ")
                    Gender=input("Enter the Gender of the student= ")
                    Grade=input("Enter the Grade of the student= ")
                    Department=input("Enter the Department of the student= ")
                    qry="INSERT INTO STUDENT VALUES('{}','{}','{}','{}','{}','{}');".format(Rollno,Name,Dateofadmi,Gender,Grade,Department)
                    csr.execute(qry)
                    csr=conn.commit()
                    print("Inserted the record Successfully")
                    print()
                    break
              elif main == 2:
                    print("1) Edit the Name ")
                    print("2) Edit the Date_of_admission ")
                    print("3) Edit the Gender ")
                    print("4) Edit the Grade ")
                    print("5) Edit the Department ")
                    print("(To Go Back, Enter 0)")
                    edit=int(input("Select any of the option given above to edit=  "))
                    while edit < 6:
                              if edit == 1:
                                        oldR=input("Enter the Rollno= ")
                                        newn=input("Enter the new name= ")
                                        qry1=("UPDATE STUDENT SET Student_name='{}' WHERE Rollno='{}';").format(newn, oldR)
                                        csr.execute(qry1)
                                        csr=conn.commit()          
                                        print("Edited the record Successfully")
                                        print()
                                        break
                              elif edit == 2:
                                        oldR=input("Enter the Rollno= ")
                                        newd=input("Enter the new Date= ")
                                        qry2="UPDATE STUDENT SET Date_of_admission='{}' WHERE Rollno='{}';".format(newd, oldR)
                                        csr.execute(qry2)
                                        csr=conn.commit()
                                        print("Edited the record Successfully")
                                        print()
                                        break
                              elif edit == 3:
                                        oldR=input("Enter the Rollno= ")
                                        newg=input("Enter the new Gender= ")
                                        qry3="UPDATE STUDENT SET Gender='{}' WHERE Rollno='{}';".format(newg, oldR)
                                        csr.execute(qry3)
                                        csr=conn.commit()
                                        print("Edited the record Successfully")
                                        print()
                                        break
                              elif edit == 4:
                                        oldR=input("Enter the Rollno= ")
                                        newc=input("Enter the new Grade= ")
                                        qry4="UPDATE STUDENT SET Class='{}' WHERE Rollno='{}';".format(newc, oldR)
                                        csr.execute(qry4)
                                        csr=conn.commit()
                                        print("Edited the record Successfully")
                                        print()
                                        break
                              elif edit == 5:
                                        oldR=input("Enter the Rollno= ")
                                        newde=input("Enter the new Department= ")
                                        qry5="UPDATE STUDENT SET Department='{}' WHERE Rollno='{}';".format(newde, oldR)
                                        csr.execute(qry5)
                                        csr=conn.commit()
                                        print("Edited the record Successfully")
                                        print()
                                        break
                              elif edit == 0:
                                        break


              elif main == 3:
                    oldR=input("Enter the Rollno name= ")
                    qry6="DELETE FROM STUDENT WHERE Rollno='{}';".format(oldR)
                    csr.execute(qry6)
                    csr=conn.commit()
                    print("Deleted the record Successfully")
                    print()
                    break

if select == 2:
          print("1) Add a Teacher= ")
          print("2) Edit a Teacher= ")
          print("3) Remove a Teacher= ")
          print("(To Go Back, Enter 0)")
          print()
          csr=conn.cursor()
          tea=int(input("choose= "))
          if tea == 1:
                    ID=input("Enter the ID= ")
                    Teaname=input("Enter the Teacher_Name= ")
                    dateofjoin=input("Enter the Date_of_join= ")
                    Gender=input("Enter the Gender= ")
                    Department=input("Enter the Department= ")
                    Salary=input("Enter the Salary= ")
                    qry="INSERT INTO TEACHERS VALUES('{}','{}','{}','{}','{}','{}');".format(ID,Teaname,dateofjoin,Gender,Department,Salary)
                    csr.execute(qry)
                    csr=conn.commit()
                    print("Inserted the record Successfully")
                    print()
          if tea == 2:
                    print("1) Edit the Teacher_Name= ")
                    print("2) Edit the Date_of_join= ")
                    print("3) Edit the Gender= ")
                    print("4) Edit the Department= ")
                    print("5) Edit the Salary= ")
                    print("(To Go Back, Enter 0)")
                    edit=int(input("Select any of the option given above to edit=  "))
                    if edit == 1:
                              ID=input("Enter the ID= ")
                              newn=input("Enter the new name= ")
                              qry1=("UPDATE TEACHERS SET Teacher_Name='{}' WHERE ID='{}';").format(newn, ID)
                              csr.execute(qry1)
                              csr=conn.commit()          
                              print("Edited the record Successfully")
                              print()
                              
                    elif edit == 2:
                              ID=input("Enter the ID= ")
                              newd=input("Enter the new Date= ")
                              qry2="UPDATE TEACHERS SET Date_of_join='{}' WHERE ID='{}';".format(newd, ID)
                              csr.execute(qry2)
                              csr=conn.commit()
                              print("Edited the record Successfully")
                              print()
                              
                    elif edit == 3:
                              ID=input("Enter the ID= ")
                              newg=input("Enter the new Gender= ")
                              qry3="UPDATE TEACHERS SET Gender='{}' WHERE ID='{}';".format(newg, ID)
                              csr.execute(qry3)
                              csr=conn.commit()
                              print("Edited the record Successfully")
                              print()
                              
                    elif edit == 4:
                              ID=input("Enter the ID= ")
                              newc=input("Enter the new Department= ")
                              qry4="UPDATE TEACHERS SET Department='{}' WHERE ID='{}';".format(newc, ID)
                              csr.execute(qry4)
                              csr=conn.commit()
                              print("Edited the record Successfully")
                              print()
                              
                    elif edit == 5:
                              ID=input("Enter the ID= ")
                              newde=input("Enter the new Salary= ")
                              qry5="UPDATE TEACHERS SET Salary='{}' WHERE ID='{}';".format(newde, ID)
                              csr.execute(qry5)
                              csr=conn.commit()
                              print("Edited the record Successfully")
                              print()
                              
                    
          if tea == 3:
                    ID=input("Enter the ID= ")
                    qry6="DELETE FROM TEACHERS WHERE ID='{}';".format(ID)
                    csr.execute(qry6)
                    csr=conn.commit()
                    print("Deleted the record Successfully")
                    print()
if select == 3:
          print("1) Pay a Fee= ")
          print("2) Edit a Fee= ")
          print("3) Remove a Fee= ")
          print("(To Go Back, Enter 0)")
          print()
          csr=conn.cursor()
          fee=int(input("choose= "))
          if fee == 1:
                    Rollno=input("Enter the Rollno= ")
                    Name=input("Enter the Student_Name= ")
                    dateoffees=input("Enter the Date_of_paying_fees= ")
                    Department=input("Enter the Department= ")
                    Fees=input("Enter the Fees= ")
                    qry="INSERT INTO FEES VALUES('{}','{}','{}','{}','{}');".format(Rollno,Name,dateoffees,Department,Fees)
                    csr.execute(qry)
                    csr=conn.commit()
                    print("Inserted the record Successfully")
                    print()
          elif fee == 2:
                    print("1) Edit the Student_Name ")
                    print("2) Edit the Date_of_paying_fees ")
                    print("3) Edit the Department ")
                    print("4) Edit the Fees ")
                    ed=int(input("Select any of the option given above to edit="))
                    if ed == 1:
                              oldR=input("Enter the Rollno= ")
                              newn=input("Enter the new Student_Name= ")
                              qry1=("UPDATE FEES SET Student_Name='{}' WHERE Rollno='{}';").format(newn, oldR)
                              csr.execute(qry1)
                              csr=conn.commit()          
                              print("Edited the record Successfully")
                              print()
                              
                    elif ed == 2:
                              oldR=input("Enter the Rollno= ")
                              newd=input("Enter the new Date_of_paying_fees= ")
                              qry2="UPDATE FEES SET Date_of_paying_fees='{}' WHERE Rollno='{}';".format(newd, oldR)
                              csr.execute(qry2)
                              csr=conn.commit()
                              print("Edited the record Successfully")
                              print()
                                        
                    elif ed == 3:
                              oldR=input("Enter the Rollno= ")
                              newde=input("Enter the new Department= ")
                              qry3="UPDATE FEES SET Department='{}' WHERE Rollno='{}';".format(newde, oldR)
                              csr.execute(qry3)
                              csr=conn.commit()
                              print("Edited the record Successfully")
                              print()
                                        
                    elif ed == 4:
                              oldR=input("Enter the Rollno= ")
                              newf=input("Enter the new Fees= ")
                              qry4="UPDATE FEES SET Fees='{}' WHERE Rollno='{}';".format(newf, oldR)
                              csr.execute(qry4)
                              csr=conn.commit()
                              print("Edited the record Successfully")
                              print()
          if fee == 3:
                    oldR=input("Enter the Rollno name= ")
                    qry6="DELETE FROM FEES WHERE Rollno='{}';".format(oldR)
                    csr.execute(qry6)
                    csr=conn.commit()
                    print("Deleted the record Successfully")
                    print()


          if view == 1:
                    qry="SELECT *FROM STUDENT;"
                    csr.execute(qry)
                    data=csr.fetchall()
                    for row in data:
                              print(row)
                              print()
          if view == 2:
                    qry="SELECT *FROM TEACHERS;"
                    csr.execute(qry)
                    data=csr.fetchall()
                    for row in data:
                              print(row)
                              print()
          if view == 3:
                    qry="SELECT *FROM FEES;"
                    csr.execute(qry)
                    data=csr.fetchall()
                    for row in data:
                              print(row)
                              print()



         
   
          




