import random
choice=0
large={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
large_r={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

message=input("Enter message you want to encrpyt/decrypt: ")
choice=int(input("Enter 1 for encryption and 2 for decryption: "))
choice_r=int(input("Enter 1 for manual rotor setup and 2 for automatic rotor setup: \n"))

if choice_r==1:
    r1=r1_o=int(input("Enter positon of the first rotor(1,26): "))
    r2=r2_o=int(input("Enter positon of the second rotor(1,26): "))
    r3=r3_o=int(input("Enter positon of the third rotor(1,26): \n"))
elif choice_r==2:
    r1=r1_o=random.randint(1,26)
    r2=r2_o=random.randint(1,26)
    r3=r3_o=random.randint(1,26)

if choice==1:
    message_enc_r1=[]
    message_enc_r2=[]
    message_enc_r3=[]
    for x in message:
        message_enc_check_r1=large[x]+r1
        if message_enc_check_r1 >= 26:
            message_enc_r1.append((large[x]+r1)-26)
        else:
            message_enc_r1.append(large[x]+r1)
        # print(r1)
        # print(message_enc_r1)
        if r1 >= 26:   
            r1-=26
        else:
            r1+=1
    
    for x in message_enc_r1:
        message_enc_check_r2=x+r2
        if message_enc_check_r2 >= 26:
            message_enc_r2.append((x+r2)-26)
        else:
            message_enc_r2.append(x+r2)
        # print(r2)
        # print(message_enc_r2)
        if r2 >= 26:
            r2-=26
        else:
            r2+=1

    for x in message_enc_r2:
        message_enc_check_r3=x+r3
        if message_enc_check_r3 >= 26:
            message_enc_r3.append((x+r3)-26)
        else:
            message_enc_r3.append(x+r3)
        # print(r3)
        # print(message_enc_r3)
        if r3 >= 26:
            r3-=26
        else:
            r3+=1

    message_enc_fin=[]
    for x in message_enc_r3:
        message_enc_fin.append(large_r[x])
    encrypted=''.join(message_enc_fin)
    print(f"Your encrypted message is: {encrypted}\n")
    print(f"Your first rotor positon is {r1_o}")
    print(f"Your second rotor positon is {r2_o}")
    print(f"Your third rotor positon is {r3_o}")

if choice==2:
    message_dec_r1=[]
    message_dec_r2=[]
    message_dec_r3=[]
    for x in message:
        message_dec_check_r3=large[x]-r3
        if message_dec_check_r3<0:
            message_dec_r3.append((large[x]-r3)+26)
        else:
            message_dec_r3.append(large[x]-r3)
        # print(r3)
        # print(message_dec_r3)
        if r3>=26:
            r3-=26
        else:
            r3+=1
    
    for x in message_dec_r3:
        message_dec_check_r2=x-r2
        if message_dec_check_r2 < 0:
            message_dec_r2.append((x-r2)+26)
        else:
            message_dec_r2.append(x-r2)
        # print(r2)
        # print(message_dec_r2)
        if r2 >= 26:
            r2-=26
        else:
            r2+=1

    for x in message_dec_r2:
        message_dec_check_r1=x-r1
        if message_dec_check_r1 < 0:
            message_dec_r1.append((x-r1)+26)
        else:
            message_dec_r1.append(x-r1)
        # print(r1)
        # print(message_dec_r1)
        if r1 >= 26:
            r1-=26
        else:
            r1+=1

    message_dec_fin=[]
    for x in message_dec_r1:
        message_dec_fin.append(large_r[x])
    decrypted=''.join(message_dec_fin)
    print(f"Your decrypted message is: {decrypted}\n")
    print(f"Your first rotor positon is {r1_o}")
    print(f"Your second rotor positon is {r2_o}")
    print(f"Your third rotor positon is {r3_o}")