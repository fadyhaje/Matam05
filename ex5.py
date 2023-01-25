# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import os
class CaesarCipher:
    def __init__(self,k):
        self.k=k
    def encrypt(self,str):
        length=(len(str))
        new_str=[]
        for i in range(length):
            if isalpha(str[i]):
                if self.k>=0:
                    new_str.append(str[i]+k%26)
                else:
                    temp=(-k)%26
                    temp=temp+26
                    new_str.append(str[i]+temp%26);
        return new_str
    def decrypt(self,str):
        self.k=-self.k
        new_str=encrypt(str)
        self.k=-self.k
        return new_str

class VigenereCipher:
    def __init__(self,k):
            self.k=[elem for elem in k]
    def encrypt(self,str):
        length=(len(str))
        counter=0
        cesar=CesarCipher(0)
        new_str=[]
        for i in range(length):
            if isalpha(str[i]):
                cesar.k=self.k[counter%len(self.k)]
                new_str.append(cesar.encrypt(str[i]))
                counter+=1;
        return new_str
    def decrypt(self,str):
        temp_k=[-elemnt for element in self.k]
        length=(len(str))
        counter=0
        cesar=CesarCipher(0)
        new_str=[]
        for i in range(length):
            if isalpha(str[i]):
                cesar.k=stemp_k[counter%len(self.k)]
                new_str.append(cesar.decrypt(str[i]))
                counter+=1;
        return new_str
        
def getVigenereFromStr(str):
    temp_k=[]
    for elem in str:
        if isalpha(elem):
            number=ord(elem) # char to int
            temp_k.append(number)
    return VigenereCipher(temp_k)
    
    
    
def turn_ch_to_num(elem)
    if 'a'<=elem<='z' 
        return elem-'a'
    elif  'A'<=elem<='Z'
        return elem-'A'-('z'-'a')+1
            
def processDirectory(dir_path::str)   
    config_path=os.path.join(dir_path,config.json)
    with open (config_path,'r') as f:
        loaded_config=json.load(f)
    key=loaded_config['key']
    if  loaded_config['type']=='Vigenere'
        obj=VigenereCipher(key)
    else  
        obj=Caesar(key)
    mode=loaded_config['mode']
    
    for file in os.listdir(dir_path)    
        if not file==config.json
            with open(file,'r')  as new_f
            temp_str=f.read()
            if mode=="encrypt" and (os.path.splitext(file)[1]==".txt")
                new_f=os.path.join(os.path.split(file)[0],(os.path.split(file)[1]+".enc")
                with open(new_f,'w')  as f 
                f.write(obj.encrypt(temp_str))
            elif mode=="decrypt" and (os.path.splitext(file)[1]==".enc") 
                new_f=os.path.split(file)[1]+".txt"
                with open(new_f,'w')  as f 
                f.write(obj.decrypt(temp_str))
    return None                                   
