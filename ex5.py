# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class CaesarCipher:
    def __init__(self,k):
        self.k=k
    def encrypt(self,str):
        length=(len(str))
        new_str=[]
        for i in range(length):
            if isalpha(str[i]):
                if self.k>=0:
                    new_str.append(str[i]+self.k%26)
                else:
                    temp=(-self.k)%26
                    temp=temp+26
                    new_str.append(str[i]+temp%26);
        return new_str
    def decrypt(self,str):
        self.k=-self.k
        new_str=encrypt(str)
        self.k=-self.k
        return new_str



class CaesarCipher:
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
                counter++;
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
                counter++;
        return new_str
