
user_input=-1
users_accounts={"test":"test","a":"a"}
user_money={"test":25,"a":10}

def pswd_change():
    for i in range(3):
        old_pswd=input("Wpisz stare haslo: ")
        n_pswd=input("Wpisz nowe haslo: ")
        n_pswd_r=input("Wpisz ponownie nowe haslo: ")
        if n_pswd==n_pswd_r:
            if old_pswd==passwd:
                users_accounts.update({login_input:n_pswd})
                print("Twoje haslo zostalo zmienione")
            else:
                print("Niepoprawne haslo")
        else:
            print("Haslo nie sa takie same")
    else:
        print("Przekroczno liczbe prob zmiany hasla")

def transfer():
    while True:
        print(f"Stan twojego konta wynosi: {user_money.get(login_input)}$\n")
        transfer_to=str(input("Wpisz nazwe uzytkownika ktoremu chcesz przeslac srodki: \n"))
        try:
            transfer_amount=int(input("Wpisz kwote do przeslania: \n"))
        except:
            print("Niepoprawna wartosc")
            break
        if transfer_amount<=user_money.get(login_input) and transfer_to in user_money and transfer_to!=login_input:
            user_input_transfer=str(input(f"Czy napewno chcesz przelac {transfer_amount}$ do {transfer_to}  (T/N)? ")).lower()
            if user_input_transfer=="t":
                user_money.update({login_input:user_money.get(login_input)-transfer_amount})
                user_money.update({transfer_to:transfer_amount+user_money.get(transfer_to)})
                print("Srodki zostaly przeslane")
                break
            elif user_input_transfer=="n":
                print("Wroc do wyboru opcji")
                break
            else:
                print("Niepoprawna wartosc")
                break
        else:
            print("Niepoprawna kwota lub nazwa uzytkownika")
            break
         
def balance():
    print(f"Stan twojego konta wynosi: {user_money.get(login_input)}$")

def withdraw():
    while True:
        print(f"Stan twojego konta wynosi: {user_money.get(login_input)}$\n")
        try:
            withdraw_amount_input=int(input("Wybierz kwote jaka chcesz wyplacic: (Aby wrocic wpisz 0)"))
        except:
            print("Niepoprawna wartosc")
            break
        if user_money.get(login_input)>=(withdraw_amount_input):
            user_money.update({login_input:(user_money.get(login_input)-withdraw_amount_input)})
            print(f"Wyplaciles {withdraw_amount_input}$")
            break
        else:
            print("Nie masz tyle pieniedzy")

def deposit():
    while True:
        try:
            deposit_amount_input=int(input("Wpisz kwote jaka chcesz zdeponowac: (Aby wrocic wpisz 0)"))
            break
        except:
            print("Niepoprawna wartosc\n")
    deposit_amount_fin=(user_money.get(login_input))+deposit_amount_input
    user_money.update({login_input:deposit_amount_fin})
    print(f"Wplaciles {deposit_amount_input}$\n")
    print(f"Stan twojego konta po wplacie wynosi {deposit_amount_fin}$")

def login():
    for i in range(3):
        global login_input
        global passwd
        login_input=input("Wpisz nazwe uzytkownika: \n")
        passwd=input("Wpisz haslo: \n")
        if login_input in users_accounts:
            if passwd==users_accounts[login_input]:
                print("Zalogowales sie\n")
                return 0
            else:
                print("Niepoprawny login lub haslo\n")
        else:
            print("Niepoprawny login lub haslo\n")
    else:
        print("Przekroczno liczbe prob zalogowania sie\n")
        exit()

def register():
    new_login=input("Wpisz nazwe uzytkownika: \n")
    new_login_r=input("Wpisz ponownie nazwe uzytkownika: \n")
    new_passwd=input("Wpisz haslo: \n")
    new_passwd_r=input("Wpisz ponownie haslo: \n")
    if new_login not in users_accounts.keys():
        if new_login==new_login_r and new_passwd==new_passwd_r:
            users_accounts.update({new_login_r:new_passwd_r})
            user_money.update({new_login_r:0})
            print("Nowe konto zostało utworzone\n")
        else:
            print("Podane haslo lub login nie sa takie same\n")
    else:
        print("Konto o takim loginie już istnieje\n")

while True:

    while True:
        print("Witaj w naszym Banku!\n")
        print("1. Zaloguj sie\n")
        print("2. Zarejestruj sie\n")
        print("3. Wyjdz\n")
        try:
            user_input=int(input("Wybierz jedna z dostepnych opcji: \n"))
        except:
            print("Niepoprawna wartosc\n")
        if user_input==1:
            login()
            break
        elif user_input==2:
            register()
        elif user_input==3:
            print("Zapraszamy ponownie!")
            quit()

    while True:
        print("1. Wplac srodki\n")
        print("2. Wyplac srodki\n")
        print("3. Sprawdz stan konta\n")
        print("4. Przelej pieniadze\n")
        print("5. Zmien haslo\n")
        print("6. Wyloguj\n")
        try:
            user_input=int(input("Wybierz jedna z opcji: \n"))
        except:
            print("Niepoprawna wartosc\n")
            print("1. Wplac srodki\n")
            print("2. Wyplac srodki\n")
            print("3. Sprawdz stan konta\n")
            print("4. Przelej pieniadze\n")
            print("5. Zmien haslo\n")
            print("6. Wyloguj\n")
        if user_input==1:
            deposit()
        elif user_input==2:
            withdraw()
        elif user_input==3:
            balance()
        elif user_input==4:
            transfer()
        elif user_input==5:
            pswd_change()
        elif user_input==6:
            print("Wylogowales sie\n")
            break