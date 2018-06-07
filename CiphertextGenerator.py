sbox = ['E','4','D','1','2','F','B','8','3','A','6','C','5','9','0','7']
pbox = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
key = list('00111010100101001101011000111111')
defaultmsg = list('0010011010110111') #Plaintext from the Book

def substitution(u):
    for i in range(0,16,4):
        a = int(''.join(u[i:i+4]),2)
        u[i:i+4] = list((bin(int(sbox[a], 16))[2:]).zfill(4))
    return u

def permutation(v):
    v = [v[pbox[i]] for i in range(0,16)]
    return v

def keyxor(w, index):
    w = [str(int(w[i]) ^ int(key[i + index])) for i in range(0,16)]
    return w

def main():
    infile = open("plaintexts.txt", "r")
    outfile = open("ciphertexts.txt", "w")
    for line in infile.readlines():
        msg = line
        outfile.write(spn(msg) + '\n')

def spn(msg):

    w = msg
    for i in range(0,9,4):
        u = keyxor(w,i)
        v = substitution(u)
        w = permutation(v)

    u = keyxor(w,12)
    v = substitution(u)
    w = keyxor(v,16)

    return ''.join(w)

if __name__== "__main__":
    main()
