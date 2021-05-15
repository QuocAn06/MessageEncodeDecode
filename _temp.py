
from pyDes import des, CBC, PAD_PKCS5
import binascii
 
# Secret key 
KEY='abcdefgh'
def des_encrypt(s):
    """
         DES encryption
         :param s: raw string
         :return: Encrypted string, hexadecimal
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)
 
 
def des_descrypt(s):
    """
         DES decryption
         :param s: encrypted string, hexadecimal
         :return: the decrypted string
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de
 
s='Have a nice day'
enc=des_encrypt(s)
print(enc)
des=des_descrypt(enc)
print(des)