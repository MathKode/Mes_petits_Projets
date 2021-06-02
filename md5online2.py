# This module helps us convert bytes to integer
import binascii
import sys
import os.path

# These are 64 additive constant being used in MD5 operations
T = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 
        0x4787c62a, 0xa8304613, 0xfd469501, 0x698098d8, 0x8b44f7af,
        0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 
        0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 
        0xd62f105d, 0x2441453, 0xd8a1e681, 0xe7d3fbc8, 0x21e1cde6, 
        0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 
        0x676f02d9, 0x8d2a4c8a, 0xfffa3942, 0x8771f681, 0x6d9d6122, 
        0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70, 
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05, 0xd9d4d039,
        0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 0xf4292244, 0x432aff97,
        0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 
        0x85845dd1, 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]

# This function performs the circular left operation
def leftCircularShift(k,bits):
    bits = bits%32
    k = k%(2**32)
    upper = (k<<bits)%(2**32)
    result = upper | (k>>(32-(bits)))
    return(result)
    
# This function divides the message block into 16 32-bit blocks    
def blockDivide(block, chunks):
    result = []
    size = len(block)//chunks
    for i in range(0, chunks):
        result.append( int.from_bytes( block[i*size:(i+1)*size],byteorder="little" ))
    return(result)    
 
 
# These are the 4 logical funtions used in MD5 Rounds 
def F(X,Y,Z):
    return( (X&Y)|((~X)&Z) )
 
def G(X,Y,Z):
    return( (X&Z) | (Y&(~Z)) )
 
def H(X,Y,Z):
    return( X^Y^Z )
 
def I(X,Y,Z):
    return( Y^(X|(~Z)) )
    
    
# These functions described here are used as MD5 Rounds where the arguments would be for single operation   
def FF(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+F(b,c,d)+M+t), s)
    return(result)
 
def GG(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+G(b,c,d)+M+t), s)
    return(result)
 
def HH(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+H(b,c,d)+M+t), s)
    return(result)
 
def II(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+I(b,c,d)+M+t), s)
    return(result)

# This function formats the number as a hexadecimal value witht the smallest bytes first.
def fmt8(num):
    bighex = "{0:08x}".format(num)
    binver = binascii.unhexlify(bighex)
    result = "{0:08x}".format(int.from_bytes(binver,byteorder='little'))
    return(result)
 
# Return the length of bitstring 
def bitlen( bitstring ):
    return(len(bitstring)*8)

# Here we perform the main hashing algorithm
def md5sum(msg):
    #First, we pad the message
    msgLen = bitlen(msg)%(2**64)
    msg = msg + b'\x80'
    zeroPad = (448 - (msgLen+8)%512)%512
    zeroPad //= 8
    msg = msg + b'\x00'*zeroPad + msgLen.to_bytes(8,byteorder='little')
    msgLen = bitlen(msg)
    iterations = msgLen//512
    #chaining variables
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476
    #main loop
    for i in range(0,iterations):
        a = A
        b = B
        c = C
        d = D
        block = msg[i*64:(i+1)*64]
        M = blockDivide(block,16)
        #Rounds
        a = FF( a,b,c,d, M[0], 7, T[0] )
        print(a,b,c,d)
        d = FF( d,a,b,c, M[1], 12, T[1] )
        print(a,b,c,d)
        c = FF( c,d,a,b, M[2], 17, T[2] )
        print(a,b,c,d)
        b = FF( b,c,d,a, M[3], 22, T[3] )
        print(a,b,c,d)
        a = FF( a,b,c,d, M[4], 7, T[4] )
        print(a,b,c,d)
        d = FF( d,a,b,c, M[5], 12, T[5] )
        print(a,b,c,d)
        c = FF( c,d,a,b, M[6], 17, T[6] )
        print(a,b,c,d)
        b = FF( b,c,d,a, M[7], 22, T[7] )
        print(a,b,c,d)
        a = FF( a,b,c,d, M[8], 7, T[8] )
        print(a,b,c,d)
        d = FF( d,a,b,c, M[9], 12, T[9] )
        print(a,b,c,d)
        c = FF( c,d,a,b, M[10], 17, T[10] )
        print(a,b,c,d)
        b = FF( b,c,d,a, M[11], 22, T[11] )
        print(a,b,c,d)
        a = FF( a,b,c,d, M[12], 7, T[12] )
        print(a,b,c,d)
        d = FF( d,a,b,c, M[13], 12, T[13] )
        print(a,b,c,d)
        c = FF( c,d,a,b, M[14], 17, T[14] )
        print(a,b,c,d)
        b = FF( b,c,d,a, M[15], 22, T[15] )
        print(a,b,c,d)
        a = GG( a,b,c,d, M[1], 5, T[16] )
        d = GG( d,a,b,c, M[6], 9, T[17] )
        c = GG( c,d,a,b, M[11], 14, T[18] )
        b = GG( b,c,d,a, M[0], 20, T[19] )
        a = GG( a,b,c,d, M[5], 5, T[20] )
        d = GG( d,a,b,c, M[10], 9, T[21] )
        c = GG( c,d,a,b, M[15], 14, T[22] )
        b = GG( b,c,d,a, M[4], 20, T[23] )
        a = GG( a,b,c,d, M[9], 5, T[24] )
        d = GG( d,a,b,c, M[14], 9, T[25] )
        c = GG( c,d,a,b, M[3], 14, T[26] )
        b = GG( b,c,d,a, M[8], 20, T[27] )
        a = GG( a,b,c,d, M[13], 5, T[28] )
        d = GG( d,a,b,c, M[2], 9, T[29] )
        c = GG( c,d,a,b, M[7], 14, T[30] )
        b = GG( b,c,d,a, M[12], 20, T[31] )
        a = HH( a,b,c,d, M[5], 4, T[32] )
        d = HH( d,a,b,c, M[8], 11, T[33] )
        c = HH( c,d,a,b, M[11], 16, T[34] )
        b = HH( b,c,d,a, M[14], 23, T[35] )
        a = HH( a,b,c,d, M[1], 4, T[36] )
        d = HH( d,a,b,c, M[4], 11, T[37] )
        c = HH( c,d,a,b, M[7], 16, T[38] )
        b = HH( b,c,d,a, M[10], 23, T[39] )
        a = HH( a,b,c,d, M[13], 4, T[40] )
        d = HH( d,a,b,c, M[0], 11, T[41] )
        c = HH( c,d,a,b, M[3], 16, T[42] )
        b = HH( b,c,d,a, M[6], 23, T[43] )
        a = HH( a,b,c,d, M[9], 4, T[44] )
        d = HH( d,a,b,c, M[12], 11, T[45] )
        c = HH( c,d,a,b, M[15], 16, T[46] )
        b = HH( b,c,d,a, M[2], 23, T[47] )
        a = II( a,b,c,d, M[0], 6, T[48] )
        d = II( d,a,b,c, M[7], 10, T[49] )
        c = II( c,d,a,b, M[14], 15, T[50] )
        b = II( b,c,d,a, M[5], 21, T[51] )
        a = II( a,b,c,d, M[12], 6, T[52] )
        d = II( d,a,b,c, M[3], 10, T[53] )
        c = II( c,d,a,b, M[10], 15, T[54] )
        b = II( b,c,d,a, M[1], 21, T[55] )
        a = II( a,b,c,d, M[8], 6, T[56] )
        d = II( d,a,b,c, M[15], 10, T[57] )
        c = II( c,d,a,b, M[6], 15, T[58] )
        b = II( b,c,d,a, M[13], 21, T[59] )
        a = II( a,b,c,d, M[4], 6, T[60] )
        d = II( d,a,b,c, M[11], 10, T[61] )
        c = II( c,d,a,b, M[2], 15, T[62] )
        b = II( b,c,d,a, M[9], 21, T[63] )
        A = (A + a)%(2**32)
        B = (B + b)%(2**32)
        C = (C + c)%(2**32)
        D = (D + d)%(2**32)
    result = fmt8(A)+fmt8(B)+fmt8(C)+fmt8(D)
    return(result)
 
 
print(md5sum(input('->').encode('UTF-8')))  

"""






"""