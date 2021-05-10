# Ma trận hoán vị ban đầu (64bits).
P_i = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#   Bảng này chỉ định hoán vị đầu vào trên khối 64 bit.
'''Ý nghĩa như sau: bit đầu tiên của đầu ra được lấy từ bit thứ 58 của đầu vào; 
bit thứ hai từ bit thứ 50, v.v., với bit cuối cùng của đầu ra được lấy từ 
bit thứ 7 của đầu vào.'''
'''  Thông tin này được trình bày dưới dạng bảng để dễ trình bày; 
nó là một vectơ, không phải là một ma trận.'''

# Ma trận hoán vị cuối cùng (Sau 16 vòng) (64bits).
P_f = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Thuật toán tạo khóa.
# Ma trận PermutedChoice.
# Hoán vị ban đầu được thực hiện trên chìa khóa (56bits).
PC_1 =  [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]


# Hoán vị được Áp dụng trên Phím Đã Dịch chuyển Để nhận K_ (i + 1) (48bits).
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# Ma trận Hàm Mở rộng để Áp dụng XOR với K_i (32bits để mở rộng 48bits).
E =  [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#Substitution Box.
S_box = [
         
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],  

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ], 

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ], 

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]

]

# Hoán vị được thực hiện sau mỗi lần thay thế SBox cho mỗi vòng (28bits).
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Ma trận dịch chuyển cho mỗi vòng phím (16bits).
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

#==============================================================================
#?: Chuyển đổi một chuỗi thành một danh sách các bit.
def str_to_bit_array(text): 
    array = list()
    for char in text:
        #Todo: Nhận giá trị ký tự trên một byte.
        binval = binvalue(char, 8)
        #Todo: Thêm các bit vào danh sách cuối cùng.
        array.extend([int(x) for x in list(binval)])
    return array

#==============================================================================
#?: Tạo lại chuỗi từ mảng bit.
def bit_array_to_str(array):
    res = ''.join([chr(int(y,2)) 
                    for y in [''.join([str(x) for x in _bytes]) 
                        for _bytes in  nsplit(array,8)]])   
    return res

#==============================================================================
#?: Trả về giá trị nhị phân dưới dạng một chuỗi có kích thước đã cho.
def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "Binary value is too large"
    while len(binval) < bitsize:
        #Todo: Thêm nhiều số 0 nếu cần để có được kích thước mong muốn (phần đệm).
        binval = "0"+binval
    return binval

#==============================================================================
#?: Ghép một danh sách vào các danh sách con có kích thước n.
def nsplit(s, n): #Split a list into sublists of size n.
    return [s[k:k+n] for k in range(0, len(s), n)]

#==============================================================================
ENCRYPT=1
DECRYPT=0

#==============================================================================
class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()
#==============================================================================
    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise "Key Should be 8 bytes long !"
        elif len(key) > 8:
            #Todo: Nếu kích thước của khóa trên 8byte, hãy cắt xuống dài 8byte.
            key = key[:8]
        
        self.password = key
        self.text = text
        
        if padding and action==ENCRYPT:
            self.addPadding()
        #Todo: Nếu không, kích thước dữ liệu được chỉ định đệm phải là bội số của 8 byte.
        elif len(self.text) % 8 != 0:
            raise "Data size should be multiple of 8 !"
        
        #Todo: Tạo ra tất cả các phím.
        self.generatekeys()
        #Todo: Chia văn bản thành các khối 8 byte.
        text_blocks = nsplit(self.text, 8)
        result = list()

        #Todo: Vòng lặp trên tất cả các khối dữ liệu.
        for block in text_blocks:
            #Todo: Chuyển đổi khối trong mảng bit.
            block = str_to_bit_array(block)
            #Todo: Áp dụng hoán vị ban đầu.
            block = self.pmt(block,P_i)
            l, r = nsplit(block, 32) # l(LEFT),r(RIGHT).
            tmp = None

            for i in range(16): #16 rounds.
                #Todo: Mở rộng r để phù hợp với kích thước K_i (48bits).
                r_e = self.expand(r, E)
                if action == ENCRYPT:
                    #Todo: Nếu mã hóa, sử dụng K_i.
                    tmp = self.xor(self.keys[i], r_e)
                else:
                    #Todo: Nếu giải mã, hãy bắt đầu bằng phím cuối cùng.
                    tmp = self.xor(self.keys[15-i], r_e)
                
                #Todo: Phương pháp sẽ áp dụng SBOXes
                tmp = self.substitute(tmp)
                tmp = self.pmt(tmp, P)
                tmp = self.xor(l, tmp)
                l = r
                r = tmp
            
            #Todo: Có hoán vị cuối cùng và nối kết quả với kết quả.
            result += self.pmt(r+l, P_f)
        final_res = bit_array_to_str(result)
        if padding and action==DECRYPT:
            #Todo: Loại bỏ phần đệm, nếu giải mã và phần đệm là đúng.
            return self.removePadding(final_res)
        else:
            #Todo: Trả về chuỗi dữ liệu cuối cùng được mã hóa hoặc giải mã.
            return final_res

#==============================================================================
    #?: Thay thế byte bằng cách sử dụng SBOX.
    def substitute(self, r_e):
        #Todo: Tách mảng bit thành danh sách con gồm 6 bit.
        subblocks = nsplit(r_e, 6)
        result = list()

        #Todo: Đối với tất cả các danh sách phụ
        for i in range(len(subblocks)):
            block = subblocks[i]
            
            #Todo: Lấy hàng có bit đầu tiên và cuối cùng
            row = int(str(block[0])+str(block[5]),2)
            #Todo: Cột là các bit thứ 2,3,4,5
            column = int(''.join([str(x) for x in block[1:][:-1]]),2)
            #Todo: Lấy giá trị trong SBOX dành cho vòng (i)
            val = S_box[i][row][column]
            #Todo: Chuyển đổi giá trị thành nhị phân
            bin = binvalue(val, 4)
            #Todo: Và thêm nó vào danh sách kết quả
            result += [int(x) for x in bin]
        return result

#==============================================================================
    def pmt(self, block, table):
        return [block[x-1] for x in table]

#==============================================================================
    #?: Thực hiện điều tương tự hơn so với hoán vị.
    def expand(self, block, table):
        return [block[x-1] for x in table]
    
#==============================================================================
    #?: Áp dụng XOR và trả về danh sách kết quả.
    def xor(self, t1, t2):
        return [x^y for x,y in zip(t1,t2)]

#==============================================================================
    #?: Thuật toán tạo tất cả các khóa.
    def generatekeys(self):
        self.keys = []
        key = str_to_bit_array(self.password)
        #Todo: Áp dụng hoán vị ban đầu trên khóa.
        key = self.pmt(key, PC_1)
        #Todo: Tách nó sang trái (l) và phải (r).
        l, r = nsplit(key, 28)
        #Todo: Áp dụng cho vòng 16.
        for i in range(16):
            #Todo: Áp dụng sự thay đổi theo vòng.
            l, r = self.shift(l, r, SHIFT[i])
            #Todo: Hợp nhất chúng.
            tmp = l + r
            #Todo: Áp dụng hoán vị để lấy K_i.
            self.keys.append(self.pmt(tmp, PC_2))

#==============================================================================
    def shift(self, l, r, n): #Shifts a list of the given value.
        return l[n:] + l[:n], r[n:] + r[:n]

#==============================================================================    
    def addPadding(self): #Adds padding to the datas by using PKCS5.
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

#==============================================================================
    def removePadding(self, data): #Removes the padding of the plain text (If there is padding).
        pad_len = ord(data[-1])
        return data[:-pad_len]
    
#==============================================================================    
    def encrypt(self, key, text, padding=True):
        return self.run(key, text, ENCRYPT, padding)

#==============================================================================
    def decrypt(self, key, text, padding=True):
        return self.run(key, text, DECRYPT, padding)

#==============================================================================
welcome = int(input("Welcome, to continue, Which year 'CryptoQuantus' was established ? :"))
print (welcome)

if welcome != int("2019"):
   print("Actually 2019 :D")
elif __name__ == '__main__':
     key = input ("Enter your 8 Character-Key :")
     text= input ("Plaintext:")
     d = des()
     ciphered = d.encrypt(key,text,padding=True) 
     plain = d.decrypt(key,ciphered,padding=True) 
     print ("Plaintext: ", plain)
     print ("Ciphertext %r" % ciphered)
     print ("by otapsin")