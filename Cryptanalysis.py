sbox = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]

sboxinv = [0]*16
for x in sbox:
    sboxinv[x] = sbox.index(x)

randvarx = [list(int(i) for i in bin(x)[2:].zfill(4)) for j in range(0,16)]
randvary = [list(int(i) for i in bin(x)[2:].zfill(4)) for j in sbox]

count = []
for i in range(0,16):
    x = []
    for j in range(0,16):
        x.append(0)
    count.append(x)

plainfile = open("plaintexts.txt", "r")
cipherfile = open("ciphertexts.txt", "r")

print('Please Wait...')

for (x,y) in zip(plainfile.readlines(), cipherfile.readlines()):
    (x,y) = ([int(i) for i in x.strip('\n')], [int(i) for i in y.strip('\n')])
    for l1 in range(0,16):
        for l2 in range(0,16):
            L1 = [int(i) for i in bin(l1)[2:].zfill(4)]
            L2 = [int(i) for i in bin(l2)[2:].zfill(4)]
            v42 = [a ^ b for (a,b) in zip(L1,y[4:8])]
            v44 = [a ^ b for (a,b) in zip(L2,y[12:16])]
#            print('x = ', x)
#            print('y = ', y)
#            print('L1 = ', L1)
#            print('L2 = ', L2)
#            print('v42 = ', v42)
#            print('v44 = ', v44)
            u42 = [int(i) for i in bin(sboxinv[int(''.join(str(h) for h in v42),2)])[2:].zfill(4)]
            u44 = [int(i) for i in bin(sboxinv[int(''.join(str(h) for h in v44),2)])[2:].zfill(4)]
#            print('u42 = ', u42)
#            print('u44 = ', u44)
            z = x[4] ^ x[6] ^ x[7] ^ u42[1] ^ u42[3] ^ u44[1] ^ u44[3]
#            print('count[',l1,'][',l2,'] = ', count[l1][l2])
#            print('z = ', z)
            if z == 0:
                count[l1][l2] += 1
#            print('count[',l1,'][',l2,'] = ', count[l1][l2])

#    print(count)

maxval = -1

for l1 in range(0,16):
    for l2 in range(0,16):
        count[l1][l2] = abs(count[l1][l2] - 4000)
        if count[l1][l2] > maxval:
            maxval = count[l1][l2]
            maxL1 = bin(l1)[2:].zfill(4)
            maxL2 = bin(l2)[2:].zfill(4)

print('The K5<2> is : ', maxL1)
print('The K5<4> is : ', maxL2)
