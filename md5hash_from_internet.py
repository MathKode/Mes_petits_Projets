"""
Merci à Usmansaadat pour le code classique (sans info)
https://github.com/Usmansaadat/MD5-Algorithm/blob/master/source.py
Ce code reprend toutes les étapes en les expliquant (à ma façon ^^)
Pour le comprendre, veuillez d'abord regarder :
https://www.youtube.com/watch?v=53O9J2J5i14&t=1123s&ab_channel=SundeepSaradhiKanthety
et
https://fr.wikipedia.org/wiki/MD5
"""

import binascii
import sys
import os.path

#En python, lorsqu'une valeur est écrite : \xB2 ou 0xB2 c'est de l'hexadécimal (base 16)
SV = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 
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
 
def leftCircularShift(k,bits):
    bits = bits%32
    print(bits) # Bits = 7
    print('k',k) # 10063647715 en binaire : 1001010111110101110001001111100011 (len = 34) 34 > 32 ERREUR
    k = k%(2**32) #Le ** correspond à 2 puissance 32 
    print('k',k) # 1473713123 en binaire :  1010111110101110001001111100011 (len = 31) 31 <= 32 OK
    upper = (k<<bits)%(2**32)  # Le << Ajoute des 0 bits à la fin
    """
    Sachant que 1473713123 en binaire donne :
    1010111110101110001001111100011
        S ou bits = 7
    10101111101011100010011111000110000000
    Ce qui donne, en décimal : 188635279744
    Puis 188635279744 % (2**32) = 3951686016
    """
    print(upper) # Résult = 3951686016 -> 11101011100010011111000110000000
    print('ç!ç!')
    result = upper | (k>>(32-(bits))) # On fait un Or entre upper et le >> de k de 32-bits
    print(k>>(32-(bits))) # 43 -> 101011
    """
    >> supprime les derniers bits ( si je fait 1100 >> 2 = 11)
    k >> (32-bits)
    1010111110101110001001111100011 >> (32-7)
    1010111110101110001001111100011 >> 25
    1010111 -> 43
    Donc upper OR k :
    3951686016 | 43
    11101011100010011111000110000000 | 101011
    11101011100010011111000110101011
    Ce qui donne en décimal : 3951686059
    """
    print(result) # result = 3951686059
    #CECI REVIENT A FAIRE UNE ROTATION DE 7 BIT VERS LA GAUCHE
    return(result)
 
def blockDivide(block, chunks):
    result = []
    size = len(block)//chunks
    print("Size :",size)
    for i in range(0, chunks):
        print(block[i*size:(i+1)*size])
        result.append( int.from_bytes( block[i*size:(i+1)*size],byteorder="little" ))
    return(result)
 
def F(X,Y,Z):
    print(X) # 4023233417 -> 11101111110011011010101110001001 
    print(Y) # 2562383102 -> 10011000101110101101110011111110
    # Avec and 10001000100010001000100010001000
    # Convertion en decimal : 2290649224
    print((X&Y)) # Resultat : 2290649224 
    print((X&Y)|((~X)&Z)) # Resultat : 2562383102
    """
    Conclusion, quand on fait un (nb1 & nb2), python va transformer les nomber en binaire et les passer dans la porte and.
    Le résultat sera quand à lui, donnné en décimal (convertion auto bin -> decimal)
    """
    return( (X&Y)|((~X)&Z) ) # & = and, ~ = not, | = or, ^ = xor <- porte logique en python
    # (4023233417 & 2562383102) | ((~4023233417) & 271733878 )
    # En binaire :
    # (11101111110011011010101110001001 & 10011000101110101101110011111110) | ((~11101111110011011010101110001001) & 10000001100100101010001110110)
    # 10001000100010001000100010001000 | (00010000001100100101010001110110 & 10000001100100101010001110110)
    # 10001000100010001000100010001000 | 00010000001100100101010001110110 
    # 10011000101110101101110011111110 -> 2562383102 (Comme le print précédent)
    """ Porte logique binaire :
    And :
    b1  b2  result
    0	0	0
    0	1	0
    1	0	0
    1	1	1
    
    Or :
    b1  b2  result
    0	0	0
    0	1	1
    1	0	1
    1	1	1

    XOR :
    b1  b2  result
    0	0	0
    0	1	1
    1	0	1
    1	1	0

    Not :
    b1 result
    0  1
    1  0
    """
def G(X,Y,Z):
    return( (X&Z) | (Y&(~Z)) )
 
def H(X,Y,Z):
    return( X^Y^Z )
 
def I(X,Y,Z):
    return( Y^(X|(~Z)) )
 
def FF(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+F(b,c,d)+M+t), s)
    # F étant égal à 2562383102, on a :
    # 1732584193 + 2562383102 + 2154590060 + 3614090360
    # = 10063647715
    # Il reste le "décalage de s bit vers la gauche" :
    # Le résultat du décalage : 3951686059
    # b valant 4023233417
    # result = 4023233417 + 3951686059
    # result = 7974919476
    print('result',result) # 7974919476
    """
    # Result pour lol premier tour :
    print(a) # Result : 1732584193
    print(b) # Result : 4023233417
    print(c) # Result : 2562383102
    print(d) # Result : 271733878
    print(M) # Message, Result : 2154590060
    print(s) # Tour de rotation (pour la rotation gauche de s bit), result : 7
    print(t) # Constant, result : 3614090360
    print(')))')
    print(result) # Result : 7974919476
    """
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
 
def fmt8(num):
    print("num",num)
    bighex = "{0:08x}".format(num) # TRANSFORMATION EN HEXADICIMAL "non reconnu" (juste une chaine de caractère, sans \x)
    print(bighex) # 39b4df9c <- format txt
    binver = binascii.unhexlify(bighex)# Transformation en hexadecimal "reconnue (avec le \x devant)" # 39B4DF9C -> 111001101101001101111110011100 -> String and hexa (when the data is over ASCII table (127 commence à 0)
    print(binver) # b'9\xb4\xdf\x9c' <- format binaire
    """
    Pour 39B4DF9C -> 39   B4   DF   9C        Exemple supp : 7E    7F
                     57   180  223  156                      126   127
                     9    \xb4 \xdf \x9c                     ~     \x7F
    """
    result = "{0:08x}".format(int.from_bytes(binver,byteorder='little')) # On trransforme le résultat y (en dessous) en hexadecimal
    print(int.from_bytes(binver,byteorder='little')) #resultat y = 2631906361 (justification en dessous)
    """
    9    \xb4 \xdf \x9c    (9 a 57 comme valeur ASCII)
    En Hexa :
    39 B4 DF 9C
    On inverse :
    9C DF B4 39 
    On colle :
    9CDFB439
    On converti : 2631906361
    """
    print('r',result) # 9CDFB439 <- Le code hexa correspondant à  2631906361
    return(result)
 
def bitlen( bitstring ):
    return(len(bitstring)*8) # On demande la taille en bit d'octet, soit, 1 octet = 8 bit, bit total = nb_octet * 8
 
def md5sum(msg):
    #First, we pad the message
    msgLen = bitlen(msg)%(2**64)
    msg = msg + b'\x80'
    """
    Pourquoi ajouter 80 (base 16) au message ?
    Comme vu dans la lecture de l'article wikipédia, le md5 fonctionne de la façon suivante :
        Message + 1 + 0 + 0 ... jusqu'a 448 bit puis + 64bit taille message
    Si on a choisit 80, c'est parceque sa convertion en binaire donne 1000 0000
    Soit le fameux + 1 + 0 + 0 ...
    Mais Pourquoi 1 byte/octet si on doit juste mettre 1 + 0 etc ?
    Car, le message d'avant étant encodé en octet, l'espace qu'il y aura (en bit) sera obligatoirement modulo 8. Exemple :
    Si message = lol
    l = 01101100
    o = 01101111
    l = 01101100
    soit une taille (len) de  8*3 = 24
    448 - 24 = 424 et 424 mod [8] = 0.
    En gros, pour faire simple, si on fait cela c'est parceque le message est codé en octet, l'espace manquant sera toujours lui aussi en octet. 
    Conclusion, on doit ajouter 1 octet avec un 1 devant (1000 0000 \x80) puis des octets de 0 (0000 0000 \x00)
    """
    zeroPad = (448 - (msgLen+8)%512)%512
    zeroPad //= 8
    msg = msg + b'\x00'*zeroPad + msgLen.to_bytes(8,byteorder='little') #Taille compté en bite et non en octet
    msgLen = bitlen(msg)
    iterations = msgLen//512 #Result of the division euclidien -> 13/5 = 2 (car il y a un reste de 3, le reste étant le modulo)
    #chaining variables
    A = 0x67452301 #En decimal (ED) : 1732584193
    B = 0xefcdab89 #ED : 4023233417
    C = 0x98badcfe #ED : 2562383102
    D = 0x10325476 #ED : 271733878
    #main loop
    for i in range(0,iterations):
        a = A
        b = B
        c = C
        d = D
        block = msg[i*64:(i+1)*64]
        M = blockDivide(block,16)
        print(M)
        """
        Pour lol :
        M = [2154590060, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0]
        lol en binaire :
        01101100 01101111 01101100 
        en hexa :
        6C 6F 6C 
        On ajoute le \x80 qui correspond à 128 :
        6C 6F 6C 80
        Ensuite, on inverse l'ordre :
        80 6C 6F 6C
        On les colle
        806C6F6C
        On converti en décimal :
        2154590060 
        Ou en binaire :
        10000000011011000110111101101100

        Rappel convertion binaire to Hexadecimal :
            Ceci ce passe par groupe de 4 bit
        1/2 octet -> On additionne les nombres correpondant au 1 de la liste ( 8 4 2 1 ) -> converti avec la base de donné
        1101 -> 8 4 2 1  -> Dans la base de donnée (1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)
                1 1 0 1                                                    /\
                8 4   1                                                    D est en 13eme p
                -> 13
        Donc 1101 = D

        Rappel convertion Hexa to binaire :
            Ceci ce passe pour 1 lettre :
        D = 13
        (13 - 8) >= 0 -> True -> donc il y a 8
        13 - 8 = 5
        (5 - 4) >= 0 -> True -> donc il y a 4
        5 - 4 = 1
        (1 - 2) >= 0 -> False -> donc il n'y a pas 2
        1 - 0 = 1
        (1 - 1) >= 0 -> True -> donc il y a le 1

        8 4 2 1
        8 4   1
        1 1 0 1    D -> 1101
        """
        #Rounds
        a = FF( a,b,c,d, M[0], 7, SV[0] )
        d = FF( d,a,b,c, M[1], 12, SV[1] )
        print("->>___________________________________________________>> ",d) # 10077931906  1001010110110011001111101111000000
        c = FF( c,d,a,b, M[2], 17, SV[2] )
        b = FF( b,c,d,a, M[3], 22, SV[3] )
        a = FF( a,b,c,d, M[4], 7, SV[4] )
        d = FF( d,a,b,c, M[5], 12, SV[5] )
        c = FF( c,d,a,b, M[6], 17, SV[6] )
        b = FF( b,c,d,a, M[7], 22, SV[7] )
        a = FF( a,b,c,d, M[8], 7, SV[8] )
        d = FF( d,a,b,c, M[9], 12, SV[9] )
        c = FF( c,d,a,b, M[10], 17, SV[10] )
        b = FF( b,c,d,a, M[11], 22, SV[11] )
        a = FF( a,b,c,d, M[12], 7, SV[12] )
        d = FF( d,a,b,c, M[13], 12, SV[13] )
        c = FF( c,d,a,b, M[14], 17, SV[14] )
        print("->>______>> ",c)
        b = FF( b,c,d,a, M[15], 22, SV[15] )
        print("->>______>> ",d)
        a = GG( a,b,c,d, M[1], 5, SV[16] )
        d = GG( d,a,b,c, M[6], 9, SV[17] )
        c = GG( c,d,a,b, M[11], 14, SV[18] )
        b = GG( b,c,d,a, M[0], 20, SV[19] )
        a = GG( a,b,c,d, M[5], 5, SV[20] )
        d = GG( d,a,b,c, M[10], 9, SV[21] )
        c = GG( c,d,a,b, M[15], 14, SV[22] )
        b = GG( b,c,d,a, M[4], 20, SV[23] )
        a = GG( a,b,c,d, M[9], 5, SV[24] )
        d = GG( d,a,b,c, M[14], 9, SV[25] )
        c = GG( c,d,a,b, M[3], 14, SV[26] )
        b = GG( b,c,d,a, M[8], 20, SV[27] )
        a = GG( a,b,c,d, M[13], 5, SV[28] )
        d = GG( d,a,b,c, M[2], 9, SV[29] )
        c = GG( c,d,a,b, M[7], 14, SV[30] )
        b = GG( b,c,d,a, M[12], 20, SV[31] )

        a = HH( a,b,c,d, M[5], 4, SV[32] )
        d = HH( d,a,b,c, M[8], 11, SV[33] )
        c = HH( c,d,a,b, M[11], 16, SV[34] )
        b = HH( b,c,d,a, M[14], 23, SV[35] )
        a = HH( a,b,c,d, M[1], 4, SV[36] )
        d = HH( d,a,b,c, M[4], 11, SV[37] )
        c = HH( c,d,a,b, M[7], 16, SV[38] )
        b = HH( b,c,d,a, M[10], 23, SV[39] )
        a = HH( a,b,c,d, M[13], 4, SV[40] )
        d = HH( d,a,b,c, M[0], 11, SV[41] )
        c = HH( c,d,a,b, M[3], 16, SV[42] )
        b = HH( b,c,d,a, M[6], 23, SV[43] )
        a = HH( a,b,c,d, M[9], 4, SV[44] )
        d = HH( d,a,b,c, M[12], 11, SV[45] )
        c = HH( c,d,a,b, M[15], 16, SV[46] )
        b = HH( b,c,d,a, M[2], 23, SV[47] )
        a = II( a,b,c,d, M[0], 6, SV[48] )
        d = II( d,a,b,c, M[7], 10, SV[49] )
        c = II( c,d,a,b, M[14], 15, SV[50] )
        b = II( b,c,d,a, M[5], 21, SV[51] )
        a = II( a,b,c,d, M[12], 6, SV[52] )
        d = II( d,a,b,c, M[3], 10, SV[53] )
        c = II( c,d,a,b, M[10], 15, SV[54] )
        b = II( b,c,d,a, M[1], 21, SV[55] )
        a = II( a,b,c,d, M[8], 6, SV[56] )
        d = II( d,a,b,c, M[15], 10, SV[57] )
        c = II( c,d,a,b, M[6], 15, SV[58] )
        b = II( b,c,d,a, M[13], 21, SV[59] )
        a = II( a,b,c,d, M[4], 6, SV[60] )
        d = II( d,a,b,c, M[11], 10, SV[61] )
        c = II( c,d,a,b, M[2], 15, SV[62] )
        b = II( b,c,d,a, M[9], 21, SV[63] )
        print('----')
        print(A) # 1732584193
        print(B) # 4023233417
        print(C) # 2562383102
        print(D) # 271733878
        A = (A + a)%(2**32)
        B = (B + b)%(2**32)
        C = (C + c)%(2**32)
        D = (D + d)%(2**32)
        print(A) # 968155036  
        print(B) # 1886291911
        print(C) # 1685598270
        print(D) # 360322761
    result = fmt8(A)+fmt8(B)+fmt8(C)+fmt8(D) # Hexa1 + Hexa2 + Hexa3 + Hexa4 <- Format texte
    return(result) # 9cdfb439c7876e703e307864c9167a15

if __name__ == "__main__":
    data = input('>').encode("UTF-8")
    print("str2hash: ",data)
    print(md5sum(data))