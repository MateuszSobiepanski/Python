from types import NoneType
import mysql.connector
import sys

choice=0
leave=False

db = mysql.connector.connect(
    host="localhost",
    user="mateusz",
    password="mateusz",
    database="db_bank"
)

mc=db.cursor()

def login():

    global username

    for i in range(3):

        username=input("Enter username: ")
        password=input("Enter password: ")

        #username='Tadzik12'
        #password='Tadek'

        mc.execute("select username,password,account_id from accounts where username=%s", (username,))
        db_login=mc.fetchone()

        if db_login is None:

            #Incorrect login
            print("Login or Password is incorrect")

        elif username==db_login[0] and password==db_login[1]:

            mc.execute("Insert Into login_try (account_id,date,status) Values (%s,now(),%s)", (db_login[2],"Succeed"))
            db.commit()

            print()
            print("Logged in")
            print()
            print(f"Hello {username}!")
            print()
            break

        else:

            #Incorecct password
            print("Login or Password is incorrect")

    else:

        try:
            mc.execute("Insert Into login_try (account_id,date,status) Values (%s,now(),%s)", (db_login[2],"Fail"))
            db.commit()

        except:
            pass

        sys.exit("Login attempts excceded try again later")

def password_check(password,password_r):

    SpeSym=['$', '@', '#', '%']

    psswd_pass={
    'digit':False,
    'upper':False,
    'lower':False,
    'spec':False,
    'len_min':False,
    'len_max':False,
    'repeat':False
    }

    for char in password:

        if char.isdigit():
            psswd_pass['digit']=True
        
        if char.isupper():
            psswd_pass['upper']=True
        
        if char.islower():
            psswd_pass['lower']=True

        if char in SpeSym:
            psswd_pass['spec']=True
    
    if len(password) > 9:
        psswd_pass['len_min']=True

    if len(password) < 40:
        psswd_pass['len_max']=True

    if password == password_r:
        psswd_pass['repeat']=True

    if all(psswd_pass.values()):
        return True

    if not(all(psswd_pass.values())):
        return False

def register():
    mc.execute("select username from accounts")
    db_users=mc.fetchall()
    #print(db_users)

    attempts=0
    users=[]

    while True:

        username_n=input("Enter your username: ")
        print()

        for user_list in db_users:
            for user in user_list:
                users.append(user)

        if username_n not in users:
            attempts=0
            break
        
        elif username_n in users:
            print("Username already exists\n")
            attempts+=1
    
            if attempts==3:
                print('Try again later\n')
                return 0
            
            continue

    while True:

        password=str(input("Enter password: "))
        password_r=str(input("Repeat password: "))
        print()
        
        if password_check(password,password_r)==True:
            attempts=0
            break
        
        elif password_check(password,password_r)==False:
            attempts+=1
    
            if attempts==3:
                print('Try again later\n')
                return 0
            
            continue


    name=input("Enter your name: ")
    print()
    l_name=input("Enter your surname: ")
    print()

    while True:

        phone=input("Enter your phone: ")
        
        if len(phone) == 9 and phone.isdigit():
            attempts=0
            break

        elif len(phone) != 9 and not(phone.isdigit()):
            print("Phone number must be 9 characters long and containing only digits")
    
            if attempts==3:
                print('Try again later\n')
                return 0

            continue       

    city=input("Enter your city: ")
    print()
    street=input("Enter your street: ")
    print()
    number=str(input("Enter your street number: "))
    print()
    
    try:
        mc.execute("""
        Insert Into address
        (city,street,number)
        Values (%s,%s,%s)""", (city,street,number))

        mc.execute("Select id_address From address Order By id_address Desc Limit 1")
        last_id_address=mc.fetchone()

        # print(last_id_address[0])
        # print(type(last_id_address[0]))

        mc.execute("""
        Insert Into clients
        (id_address,name,s_name,phone)
        Values (%s,%s,%s,%s)""", (last_id_address[0],name,l_name,phone))

        mc.execute("Select id_client From clients Order By id_address Desc Limit 1")
        last_id_clients=mc.fetchone()

        mc.execute("""
        Insert Into accounts
        (id_client,username,password,balance,created_at,delted_at)
        Values (%s,%s,%s,%s,now(),%s)""", (last_id_clients[0],username_n,password,0,'0000-00-00 00:00:00'))

        #'0000-00-00 00:00:00'

        db.commit()

        print("succes")
    
    except:
        db.rollback()
        print("fail")

        pass

def deposit():

    mc.execute("Select balance,account_id from accounts where username=%s", (username,))
    db_balance_id=mc.fetchone()
    # print(db_balance_id[1])
    dep_amount=int(input("Enter amount to deposit: "))

    try:

        mc.execute("Update accounts SET balance = %s where account_id = %s", (db_balance_id[0]+dep_amount, db_balance_id[1]))

        mc.execute("""
        Insert Into transactions
        (from_account_id, to_account_id, date, amount, transaction_status, transaction_type)
        Values (%s, %s, now(), %s, %s, %s)""", (db_balance_id[1], db_balance_id[1], dep_amount, 'Success', 'Deposit'))

        db.commit()
    
        print(f"You have deposited {dep_amount} $\n")
        input("Press Enter to continue...\n")

    except:

        db.rollback()

        mc.execute("""
        Insert Into transactions
        (from_account_id, to_account_id, date, amount, transaction_status, transaction_type)
        Values (%s, %s, now(), %s, %s, %s)""", (db_balance_id[1], db_balance_id[1], dep_amount, 'Failed', 'Deposit'))

        db.commit()

        print("Something went wrong, try again")
        input("Press Enter to continue\n")

def withdraw():

    mc.execute("Select balance,account_id from accounts where username=%s", (username,))
    db_balance_id=mc.fetchone()

    wit_amount=int(input("Enter amount to withdraw: "))

    if wit_amount > db_balance_id[0]:
        print("Not enough funds\n")
        input("Press Enter to continue...\n")

    elif wit_amount <= db_balance_id[0]:

        try:
            mc.execute("Update accounts Set balance = %s Where account_id = %s",(db_balance_id[0]-wit_amount, db_balance_id[1]))

            mc.execute("""
            Insert Into transactions
            (from_account_id, to_account_id, date, amount, transaction_status, transaction_type)
            Values (%s, %s, now(), %s, %s, %s)""", (db_balance_id[1], db_balance_id[1], wit_amount, 'Success', 'Withdraw'))

            db.commit()

            print(f"You have withdrawed {wit_amount} $\n")
            input("Press Enter to continue...")

        except:

            db.rollback()

            mc.execute("""
            Insert Into transactions
            (from_account_id, to_account_id, date, amount, transaction_status, transaction_type)
            Values (%s, %s, now(), %s, %s, %s)""", (db_balance_id[1], db_balance_id[1], wit_amount, 'Failed', 'Withdraw'))
            db.commit()

            print("Something went wrong, try again.")
            input("Press Enter to continue\n")

def balance():

    mc.execute("Select balance from accounts where username=%s", (username,))
    db_balance_id=mc.fetchone()

    print(f"Your balance is {db_balance_id[0]} $")
    input("Press Enter to continue...\n")

def transfer():

    repeat=True

    while True:

        try:

            amount=int(input("Enter amount you want to transfer: "))
            print()

            mc.execute("Select balance,account_id from accounts where username=%s", (username,))
            db_balance_id=mc.fetchone()

            mc.execute("Select account_id from accounts")
            db_usernames=mc.fetchall()
            # print(db_usernames)

            if amount > db_balance_id[0]:
                print("You dont have enough funds\n")
                continue

            elif amount <= db_balance_id[0]:
                break

        except:

            print()
            print("Enter correct value\n")
            continue

    while True:

        if repeat == True:
            trans_user=input("Enter username or id: ")
        
        elif repeat == False:
            trans_user=str(trans_user[0])

        if trans_user.isdigit():

            if int(trans_user) != db_balance_id[1]:

                trans_user=int(trans_user)
                mc.execute("select balance, username from accounts where account_id=%s", (trans_user,))
                balance_t_db=mc.fetchone()

                list=[]

                for x in db_usernames:
                    for y in x:
                        list.append(y)

                if trans_user in list:

                    try:

                        mc.execute("Update accounts Set balance=%s Where username=%s", (db_balance_id[0]-amount, username))
                        mc.execute("Update accounts Set balance=%s Where account_id=%s", (balance_t_db[0]+amount, trans_user))
                        db.commit()

                        mc.execute("""
                        Insert Into transactions
                        (from_account_id, to_account_id, date, amount, transaction_status, transaction_type)
                        Values (%s, %s, now(), %s, %s, %s)""", (db_balance_id[1], trans_user, amount, 'Success', 'Transfer'))
                        db.commit()

                        print()
                        print(f"You have successfully sent {amount}$ to {balance_t_db[1]}\n")
                        input("Press Enter to continue...")
                        print()
                        
                        return 1

                    except:

                        print("Something went wrong")
                        db.rollback()

                        mc.execute("""
                        Insert Into transactions
                        (from_account_id, to_account_id, date, amount, transaction_status, transaction_type)
                        Values (%s, %s, now(), %s, %s, %s)""", (db_balance_id[1], trans_user, amount, 'Failed', 'Transfer'))
                        db.commit()

                        continue

                else:
                    print('User doesnt exists')
                    continue


            else:

                print()
                print("Id need to be differ form yours\n")
                continue
        
        else:

            mc.execute("Select account_id from accounts where username=%s", (trans_user,))
            trans_user=mc.fetchone()

            if type(trans_user) == NoneType:
                print()
                print("User doesnt exist, try again\n")
                repeat=True
                
            else:
                repeat=False

def change_password():
    mc.execute("Select password from accounts where username=%s", (username,))
    db_pass=mc.fetchone()

    for i in range(3):

        password_check=input("Enter current password: ")
        password_check.split()

        if password_check==db_pass[0]:

            n_pass=input("Enter new password: ")
            # password_check()

            mc.execute("Update accounts Set password=%s where username=%s", (n_pass,username))
            db.commit()
            print("Password was changed")
            break
    
        else:
            print("Try again\n")
    
    else:
        print("Attempts exceded\n")

def transaction_history():
    mc.execute("Select account_id from accounts where username=%s", (username,))
    db_id=mc.fetchone()

    mc.execute("Select date, amount, transaction_status, transaction_type, to_account_id From transactions where from_account_id=%s", (db_id[0],))
    db_history=mc.fetchall()

    y=0
    for x in db_history:

        if db_history[y][3] == 'Transfer':
            print(f"Date: {db_history[y][0]} | Amount: {db_history[y][1]} | Transfer Addressee: {db_history[y][4]} | Transaction Status: {db_history[y][2]} | Transaction Type: {db_history[y][3]}\n")

        else:
            print(f"Date: {db_history[y][0]} | Amount: {db_history[y][1]} | Transaction Status: {db_history[y][2]} | Transaction Type: {db_history[y][3]}\n")

        y+=1

    input("Press Enter to continue...\n")

def login_history():
    mc.execute("Select account_id from accounts where username=%s", (username,))
    db_id=mc.fetchone()

    mc.execute("Select date, status from login_try where account_id=%s", (db_id[0],))
    db_login_try=mc.fetchall()

    y=0
    for x in db_login_try:
        print(f"Date: {db_login_try[y][0]} | Status: {db_login_try[y][1]}\n")

        y+=1

    input("Press Enter to continue...")

#####################################################################################

#All the functions are above the hash line

#Before login

while True:

    while True:

        try:
            
            print("Welcome in our Bank!\n")
            print("1. Login")
            print("2. Register")
            print("3. Quit\n")

            choice=int(input("Select one option from list above: "))
            #choice=1

            if choice in range(1,4):

                if  choice==1:
                    login()
                    break

                if choice==2:
                    register()
                    continue

                if choice==3:
                    leave=True
                    break

            elif choice not in range(1,4):
                print("Incorrect value")
                continue

        except:
            print("Incorrect value")

    if leave==1:
        print("Thank you")
        break

    #After login

    while True:

        try:

            print("1. Deposit\n")
            print("2. Withdraw\n")
            print("3. Check Balance\n")
            print("4. Transfer\n")
            print("5. Change password\n")
            print("6. Transaction history\n")
            print("7. Login history\n")
            print("8. Log out\n")

            choice=int(input("Select an option from list above: "))
            print()

            if choice in range(1,9):

                if choice==1:
                    deposit()
                    continue

                if choice==2:
                    withdraw()
                    continue

                if choice==3:
                    balance()
                    continue

                if choice==4:
                    transfer()
                    continue

                if choice==5:
                    change_password()
                    continue

                if choice==6:
                    transaction_history()
                    continue

                if choice==7:
                    login_history()
                    continue

                if choice==8:
                    break
                        
            elif choice not in range(1,9):
                print("Incorrect values\n")
                continue
            

        except:
            print()
            print("Incorrect Valued\n")