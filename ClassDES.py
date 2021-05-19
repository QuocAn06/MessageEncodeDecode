from pyDes import des, CBC, PAD_PKCS5
import binascii

#=============================================================================
class CDes:
    def __init__(self,plaintext,key,ciphertext=""):
        self.plaintext=plaintext
        self.key=key
        self.ciphertext=ciphertext
#=============================================================================
    def MaHoa(self):
        """
            DES encryption
            :param s: raw string
            :return: Encrypted string, hexadecimal
        """
        secret_key = self.key
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(self.plaintext, padmode=PAD_PKCS5)
        result = binascii.b2a_hex(en)

        self.ciphertext = result

        return self.ciphertext

 #=============================================================================
    def GiaiMa(self):
        """
            DES decryption
            :param s: encrypted string, hexadecimal
            :return: the decrypted string
        """
        secret_key = self.key
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        message = self.ciphertext[2:(len(self.ciphertext)-1)]
        print(type(message))
        print(message)
        self.plaintext = k.decrypt(binascii.a2b_hex(message), padmode=PAD_PKCS5)
        return self.plaintext
        
#=============================================================================
def main():
    s='Have a nice day'
    # Secret key 
    KEY='abcdefgh'
    obj = CDes(s,KEY)
    enc=obj.MaHoa()
    print(enc)
    des=obj.GiaiMa()
    print(des)

#=============================================================================
if __name__ == '__main__':
    main()