class CVignere:
    def __init__(self, plaintext="",key="",ciphertext=""):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext
#==============================================================================
    def MaHoa(self):
        self.ciphertext = ""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            vt_key = i% len(self.key)
            if c!=' ':
                so = ord(c) -65
                so_key = ord(self.key[vt_key]) -65 +1 
                so = (so + so_key)% 26
                self.ciphertext = self.ciphertext + chr(so+65)
            else:
                self.ciphertext = self.ciphertext + self.key[vt_key]
        return self.ciphertext
#==============================================================================
    def GiaiMa(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            c = self.ciphertext[i]
            vt_key = i% len(self.key)
            if c != self.key[vt_key]:
                so = ord(c) - 65
                so_key = ord(self.key[vt_key]) - 65 + 1
                so = (so - so_key + 26) % 26
                self.plaintext = self.plaintext + chr(so + 65)
            else:
                self.plaintext = self.plaintext + ' '
        return self.plaintext
