import random
s=False
n=False

password=[]

large=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
small=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
special=['!','@','#','$','%','&','*','?','^','(',')','[',']',';',"'",'<','>','?','?','+','=','-']

length=int(input("Wpisz dlugosc hasla: "))
special_c=input("Czy ma zawierac znaki specjalne(T/N): ")
numbers_c=input("Czy ma zawierac liczby(T/N): ")

if special_c=='T':
    s=True

if numbers_c=='T':
    n=True


for x in range(length):
    cat=random.randint(0,3)
    if cat==0:
        password.append(large[random.randint(0,25)])
    elif cat==1:
        password.append(small[random.randint(0,25)])
    elif cat==2:
        if n==True:
            password.append(numbers[random.randint(0,9)])
        else:
            pass
    elif cat==3:
        if s==True:
            password.append(special[random.randint(0,21)])
        else:
            pass

print(password)

