# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import os
import sys
import json


def changeStr(str,k):
    twenty6=(ord('Z')-ord('A')+1)
    if(str<='Z' and str>='A'):
        return chr(ord('A')+(ord(str)-ord('A')+k)%twenty6)
    elif (str<='z' and str>='a'):
        return chr(ord('a')+(ord(str)-ord('a')+k)%twenty6)
    else :
        return str

class CaesarCipher:
    def __init__(self,k):
        self.k=k
    def encrypt(self,str):
        length=(len(str))
        new_str=""
        for i in range(length):
            new_str+=changeStr(str[i],self.k)

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
            cesar.k=self.k[counter%len(self.k)]
            new_str+=cesar.encrypt(str[i])
            if(str[i].isalpha()):
                counter+=1
        return new_str
    def decrypt(self,str):
        temp_k=[-element for element in self.k]

        cesar=VigenereCipher([])
        new_str=""
        cesar.k=temp_k
        new_str+=cesar.encrypt(str)
        return new_str

def getVigenereFromStr(str):
    twenty6=(ord('Z')-ord('A')+1)
    temp_k=[]
    for elem in str:
        if elem.isalpha():
            if 'a'<=ord(elem)<='z':
                number=ord(elem)-'a'# char to int
            else:
                number=ord(elem)-'A'+twenty6
            temp_k.append(number)
    return VigenereCipher(temp_k)

def processDirectory(str):
    config_path=os.path.join(str,"config.json")
    with open (config_path,'r') as f:
        loaded_config=json.load(f)
    key=loaded_config['key']
    if  loaded_config['type']=='Vigenere':
        if type(key)==type(''):
            obj=getVigenereFromStr(key)
        else:
            obj=VigenereCipher(key)
    else:
        obj=CaesarCipher(key)
    mode=loaded_config['mode']

    for file in os.listdir(str):
        if not file=="config.json" :
            file_path=os.path.join(str,file)
            with open (file_path,'r',encoding="utf-8")  as f:
                temp_str=f.read()
            if mode=="encrypt" and (os.path.splitext(file_path)[1]=='.txt'):
                new_f=(os.path.splitext(file_path)[0]+'.enc')
                with open (new_f, 'w')  as d :
                    d.write(obj.encrypt(temp_str))
            elif mode=="decrypt" and (os.path.splitext(file_path)[1]=='.enc') :
                new_f=(os.path.splitext(file_path)[0]+'.txt')
                with open (new_f, 'w')  as c:
                    c.write(obj.decrypt(temp_str))
    return None
