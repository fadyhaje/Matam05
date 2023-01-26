# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import os
import sys
import json

def abc_moving(str,index):
    counter=0
    for i in range(index):
        counter+=1
        if counter==26:
            counter=0
    return counter


class CaesarCipher:
    def __init__(self,k):
        self.k=k
    def encrypt(self,str):
        length=(len(str))
        new_str=""
        for i in range(length):
            if str[i].isalpha():
                if self.k>=0:
                    new_str+=chr(ord(str[i])+abc_moving(str,self.k))
                else:
                    temp=(-self.k)%26
                    temp=temp+26
                    new_str+=chr(ord(str[i])-abc_moving(str,temp))
        return new_str
    def decrypt(self,str):
        self.k=-self.k
        new_str=self.encrypt(str)
        self.k=-self.k
        return new_str

class VigenereCipher:
    def __init__(self,k):
        self.k=[elem for elem in k]
    def encrypt(self,str):
        length=(len(str))
        counter=0
        cesar=CaesarCipher(0)
        new_str=""
        for i in range(length):
            if str[i].isalpha():
                cesar.k=self.k[counter%len(self.k)]
                new_str+=cesar.encrypt(str[i])
                counter+=1;
        return new_str
    def decrypt(self,str):
        temp_k=[-element for element in self.k]
        length=(len(str))
        counter=0
        cesar=CaesarCipher(0)
        new_str=""
        for i in range(length):
            if str[i].isalpha():
                cesar.k=temp_k[counter%len(self.k)]
                new_str+=cesar.decrypt(str[i])
                counter+=1;
        return new_str

def getVigenereFromStr(str):
    temp_k=""
    for elem in str:
        if isalpha(elem):
            number=ord(elem) # char to int
            temp_k+=number
    return VigenereCipher(temp_k)



def processDirectory(str):
    config_path=os.path.join(str,"config.json")
    with open (config_path,'r') as f:
        loaded_config=json.load(f)
    key=loaded_config['key']
    if  loaded_config['type']=='Vigenere':
        obj=VigenereCipher(key)
    else:
        obj=CaesarCipher(key)
    mode=loaded_config['mode']

    for file in os.listdir(str):
        if not file=="config.json" :
            file_path=os.path.join(str,file)
            with open (file_path,'r')  as f:
                temp_str=f.read()
            if mode=="encrypt" and (os.path.splitext(file_path)[1]==".txt"):
                new_f=os.path.splitext(file_path)[0]+".enc"
                with open (new_f, 'w')  as f :
                    f.write(obj.encrypt(temp_str))
            elif mode=="decrypt" and os.path.splitext(file_path)[1]==".enc" :
                new_f=os.path.splitext(file_path)[0]+".txt"
                with open (new_f, 'w')  as f:
                    f.write(obj.decrypt(temp_str))
    return None
