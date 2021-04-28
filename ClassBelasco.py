class  CBelasco:
    def __init__(self,plaintext,key,ciphertext=""):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext
#=============================================================================
    def MaHoa(self):
        self.ciphertext=""
        for i in range(len(self.plaintext)):
            c= self.plaintext[i]
            if c!=' ':
                row = ord(self.key[i%len(self.key)]) - 65
                col = ord(c) - 65
                so  = (row + col) % 26
                self.ciphertext = self.ciphertext + chr(so + 65)
            else:
                self.ciphertext = self.ciphertext + ' '
        return self.ciphertext
#=============================================================================
    def GiaiMa(self):
        self.plaintext=""
        for i in range(len(self.ciphertext)):
            c = self.ciphertext[i]
            if c!= ' ':
                row = ord(self.key[i % len(self.key)]) - 65
                col = ord(c) - 65
                so = (col - row + 26) % 26
                self.plaintext = self.plaintext + chr(so + 65)
            else:
                self.plaintext = self.plaintext + ' '
        return self.plaintext