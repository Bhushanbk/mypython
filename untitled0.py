import mysql.connector as sql
import random

mycon= sql.connect(host='localhost',user= 'Gaurav',passwd='root',database= 'bank')
if mycon.is_connected()== False:
    print("Error connecting to MySQL Database")

cursor= mycon.cursor()
    
def createAccount():
    accNo= random.randint(10000000,99999999)
    name = input("\nEnter the Account Holder's name : ")
    acctype = input("Enter the type of Account [C/S] : ")
    acctype = acctype.upper()
    deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for Current:"))
    print("\n\n\nAccount Created")
    print('\n\nAccount Number:',accNo)
    print('\n\n')
    data= "Insert into data values({},'{}','{}',{})".format(accNo,name,acctype,deposit)
    cursor.execute(data)
    mycon.commit()

def acnames():
    allnames= "select Name from data"
    cursor.execute(allnames)
    listofnames= cursor.fetchall()
    if listofnames:
        for i in range(len(listofnames)):
            list_tup= listofnames[i]
            for j in list_tup :
                print(list_tup[0])
            
    else:
        print("No Records to display !")

def displayAll():
    alldet= "select * from data"
    cursor.execute(alldet)
    details= cursor.fetchall()
    if details:
        for i in range(len(details)):
            det_tup = details[i]
            for j in range(len(det_tup)):
                print(det_tup[j], end =' ')
            print(end='\n')    
    else :
        print("No Records to display !")
        

def displayBal(num):
    accbalstr= "select Balance from data where Acc_Num={}".format(num)
    cursor.execute(accbalstr)
    bal= cursor.fetchone()
    if bal:
        balinit= bal[0]
        print("\nYour Current Account Balance is",balinit)
    else:
        print("\nProvided Account Details Incorrect !")


def depositAndWithdraw(accnum,num):
    accbalstr= "select Balance from data where Acc_Num={}".format(accnum)
    cursor.execute(accbalstr)
    bal= cursor.fetchone()
    if bal:
        
        balinit= bal[0]

        if num == 1:
            amount = int(input("Enter the amount to deposit : "))
            depstr= "update data set Balance=Balance + {} where Acc_Num = {}".format(amount,accnum)
            cursor.execute(depstr)
            mycon.commit()
            print("\nYour Account Balance has been updated Successfully !")
            
        elif num == 2:
            amount = int(input("Enter the amount to withdraw : "))
            if amount > balinit :
                print("\nYou don't have enough balance !")
            else:
                withstr= "update data set Balance= Balance - {} where Acc_Num = {}".format(amount,accnum)
                cursor.execute(withstr)
                mycon.commit()
                print("\nAmount has been withdrawn and Balance has been updated Successfully !")
                        
    else:

        print("\nAccount Not Found !!!")
               
def deleteAccount(num):

    accbalstr= "select Balance from data where Acc_Num={}".format(num)
    cursor.execute(accbalstr)
    bal= cursor.fetchone()
    if bal:
        delstr= "delete from data where Acc_Num = {}".format(num)
        cursor.execute(delstr)
        mycon.commit()
        print("\nAccount Closed !!!")
    else :
        print("\nAccount Not Found !!!")
    
     
def modifyAccount(num):
    cha= ''
    accbalstr= "select Balance from data where Acc_Num={}".format(num)
    cursor.execute(accbalstr)
    bal= cursor.fetchone()
    if bal:
        while not (cha == '1' or cha == '2' or cha == '3'):
        
            print("\nTo Modify Your Account Details such as Name, Type, Deposit... Enter the respective number for each option :")
            print("\n1. Name\n2. Account Type [C/S]\n3. Deposit Amount\n")
            cha= input("Enter 1,2 or 3 :")
            if cha == '1' :
                nname= input("\nEnter New Name:")
                nnamestr= "update data set Name = '{}' where Acc_Num={}".format(nname,num)
                cursor.execute(nnamestr)
                mycon.commit()
                print("\nName has been Updated !!")
            elif cha =='2' :
                ntype=''
                while not (ntype== 'S' or ntype == 'C'):
                    
                    print('C - Current\nS - Saving')
                    ntype= input("\nEnter New Type [C or S]:")
                    ntype= ntype.upper()
                    if (ntype == 'S' or ntype == 'C'):
                        ntypestr= "update data set Type='{}' where Acc_Num={}".format(ntype,num)
                        cursor.execute(ntypestr)
                        mycon.commit()
                        print("\nAccount Type has been Updated !!")
                    else:
                        print("Wrong Character !!")
            elif cha == '3':
                ndep= input("\nEnter Deposit Amount:")
                ndepstr= "update data set Balance = {} where Acc_Num = {}".format(ndep,num)
                cursor.execute(ndepstr)
                mycon.commit()
                print("\nDeposit Amount has been Updated !!")
            else:
                print("\n\nInvalid Choice !!!")
    else:
        print("\n\nAccount Not Found !!!")

            

#START of the Main Program
        
        
ch=''
while ch != 9:
    
    print("\n\n\t---MAIN MENU---\n")
    print("1. NEW ACCOUNT")
    print("2. DEPOSIT AMOUNT")
    print("3. WITHDRAW AMOUNT")
    print("4. BALANCE ENQUIRY")
    print("5. ALL ACCOUNT HOLDER LIST")
    print("6. CLOSE AN ACCOUNT")
    print("7. MODIFY AN ACCOUNT")
    print("8. VIEW COMPLETE BANK DETAILS OF ALL ACCOUNT HOLDERS")
    print("9. EXIT\n")
    ch = input("Select Your Option (1-8):")
    
    
    if ch == '1' :
        createAccount()
    elif ch =='2':
        num = int(input("\nEnter the Account Number : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\nEnter the Account Number : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\nEnter the Account Number : "))
        displayBal(num)
    elif ch == '5':
        print('\n')
        acnames()
    elif ch == '6':
        num = int(input("\nEnter the Account Number : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\nEnter the Account Number : "))
        modifyAccount(num)
    elif ch == '8':
        print('\n')
        displayAll()
    elif ch == '9':
        print("\nThanks for using our Bank Management System !!!\n\n")
        break
    else :
        print("\n\nInvalid choice !!!")



#END of the Program
