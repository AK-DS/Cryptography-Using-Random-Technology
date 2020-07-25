import string
import random
from sympy import *
store1=string.ascii_uppercase
store2=string.ascii_lowercase
store3=store1+store2.replace(" ","")


#Ceaser cipher
def ECeaserCipher():

    text=input("Enter Plain Text\n")
    cipher=""
    for i in range(len(text)):
        if text[i]==" ":
            cipher=cipher+text[i]
        else:
            cipher=cipher+chr(ord(text[i])+6)        
    print(cipher)

def DCeaserCipher():
    #Decipher
    ctext=input("Enter Plain Text\n")
    decipher=""
    for i in range(len(ctext)):
        if ctext[i]==" ":
            decipher=decipher+ctext[i]
        else:
            decipher=decipher+chr(ord(ctext[i])-6)
    print(decipher)
    #text=''




#Vernam Cipher/One Time Pad
def EVernamCipher():
    text=input("Enter Plain Text:  ")
    key=''
    cipher=''
    if text=='':
        print("Empty text field\n")
    else:
        for i in range(len(text)):
            ran=random.choice(store1)
            key=key+ran
            temp=ord(text[i])+ord(ran)-130
            if temp>25:
                cipher=cipher+chr(temp+39)#+65-26
            else:
                cipher=cipher+chr(temp+65)
        print("Cipher Code: ",cipher)
        print("Key: ",key)
        ds.write(cipher)
        ds.write(key)
        key=''

def DVernamCipher():
    #Decipher
    decipher=""
    ctext=input("Enter Cipher Code:  ")
    key=input("Enter You Key:  ")
    if len(key)!=len(ctext):
        print("Key and Cipher Code length do not match\n")
    else:
        for i in range(len(ctext)):
            if((ord(ctext[i])-65) < (ord(key[i])-65)):
                temp=(ord(ctext[i])-39)-(ord(key[i])-65)
                decipher=decipher+chr(temp+65)
            else:
                temp=(ord(ctext[i])-65)-(ord(key[i])-65)
                decipher=decipher+chr(temp+65)
        print("Deciphered Text: ",decipher)




#Diffie-Hellman Key Exchange Algorithm
def DiffieKey():
    #gerenating random prime no.
    n=randprime(10000,100000)
    g=randprime(10000,100000)
    x=randprime(10000,100000)
    y=randprime(10000,100000)

    #generating the values To be exchanged between A and B
    A=(g**x) % n
    B=(g**y) % n

    #generating private keys
    PrKA=(B**x) % n
    PrKB=(A**y) % n

    print("Transfered values :-\nA To B:  ",n,"\nB To A:  ",g)
    print("Private Keys:-\nA:  ",PrKA,"\nB:  ",PrKB)




#Stream Cipher
def EStreamCipher(text):
    bin1=[]
    bin2=[]
    bin3=[]
    bin4=[]
    val=''
    for i in range(0,len(text)):
        if ord(text[i])<97:
            val=val+random.choice(store2)
        else:
            val=val+random.choice(store1)
        bin1.append(''.join(format(ord(text[i]),'b')))
        bin2.append(''.join(format(ord(val[i]),'b')))
        for k in range(len(bin2[i])-len(bin1[i])):
            temp=bin1[i]
            bin1[i]='0'+temp
        for j in range(0,len(bin1[i])):
            bin3.append((int(bin1[i][j])^int(bin2[i][j])))
        s=[str(m) for m in bin3]
        res=int(''.join(s))
        num = int(res)
        dec_value = 0
        base = 1
        temp = num 
        while(temp): 
            last_digit = temp % 10 
            temp = int(temp / 10) 
            dec_value += last_digit * base 
            base = base * 2 
        #print(bin1[i],bin2[i],bin3,dec_value,chr(dec_value),val[i])
        bin3.clear()
        bin4.append(chr(dec_value))
    s=[str(m) for m in bin4]
    res=''.join(s)
    print(res,val,"\n")
    ds.write(res+"\n")
    ukey.write(val+"\n")

#decipher
def DStreamCipher(text,key):
    bin1=[]
    bin2=[]
    bin3=[]
    bin4=[]
    for i in range(0,len(text)):
        bin1.append(''.join(format(ord(text[i]),'b')))
        bin2.append(''.join(format(ord(key[i]),'b')))
        for k in range(len(bin2[i])-len(bin1[i])):
            temp=bin1[i]
            bin1[i]='0'+temp
        for j in range(0,len(bin1[i])):
            bin3.append((int(bin1[i][j])^int(bin2[i][j])))
        s=[str(m) for m in bin3]
        res=''.join(s)
        num = int(res)
        dec_value = 0
        base = 1
        temp = num 
        while(temp): 
            last_digit = temp % 10 
            temp = int(temp / 10) 
            dec_value += last_digit * base 
            base = base * 2 
        #print(bin1[i],bin2[i],bin3,dec_value,chr(dec_value))
        bin3.clear()
        bin4.append(chr(dec_value))
    s=[str(m) for m in bin4]
    res=''.join(s)
    print(res.strip(' '))
    ds.write(res.strip(' '))



def EAES():
    sr=open('Desktop/Encrypted.txt','w')
    text=input("Enter Plain Text:  ")
    round_key=[]
    temp=[]
    value=4
    for i in range(0,value):
        for j in range(0,value):
            temp.append(random.choice(store3))
        round_key.append(temp)
        temp=[]
    print(round_key)
    sr.write(str(round_key))

def DAES():
    text=''


def etechnique(e_choice):
    if e_choice==0:
        random_algo()
    if e_choice==1:
        ECeaserCipher()
    elif e_choice==2:
        EVernamCipher()
    elif e_choice==3:
        DiffieKey()
    elif e_choice==4:
        for i in range(lines):
            EStreamCipher(sr.readline())
    elif e_choice==5:
        EAES()
    else:
        print("Invalid Choice")


def dtechnique(d_choice):
    if d_choice==0:
        random_algo()
    elif d_choice==1:
        DCeaserCipher()
    elif d_choice==2:
        DVernamCipher()
    elif d_choice==3:
        for i in range(lines):
            DStreamCipher(sr.readline(),ukey.readline().replace(" ",""))
    elif d_choice==4:
        DAES()
    else:
        print("Invalid Choice")




def choice(algo):
    if sr.read(1)==None:
        print("Empty File")
    else:
        if algo==1:
            e_choice=int(input("Enter Numeric Value: \n0. Random\n1. Ceaser Cipher\n2. Vernam Cipher\n3. Diffie-Hellman Key\n4. Stream Cipher\n5. AES\n"))
            etechnique(e_choice)
        
        elif algo==2:
            d_choice=int(input("Enter Numeric Value: \n0. Random\n1. Ceaser Cipher\n2. Vernam Cipher\n3. Stream Cipher\n4. AES\n"))
            dtechnique(d_choice)
        else:
            print("Invalid Choice")
    

user_choice=int(input("Enter\n 1 For Encryption\n2 For Decryption"))

fpath=input("Enter Path Of The File  ")
sr=open(fpath,'r')
ds=open("Desktop/ds.txt",'a')
ds.truncate(0)
if user_choice==1:
    ukey=open("Desktop/key.txt",'a')
    ukey.truncate(0)
else:
    kpath=input("Enter Path Of The Key  ")
    ukey=open(kpath,'r')
lines=0
with open(fpath,'r') as f:
    for i in f:
        lines+=1
choice(user_choice)
