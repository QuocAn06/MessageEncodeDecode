class CXOR:
    def __init__(self ,plaintext ,key=3,ciphertext= ""):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext
#====================================================================
    def MaHoa(self):
        for c in self.plaintext:
            if c!= ' ':
                so= ord(c)- 65
                so= so^ self.key
                self.ciphertext+= chr(so+ 65)
            else:
                self.ciphertext+= c
        return self.ciphertext
