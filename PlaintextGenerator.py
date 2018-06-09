import random

openedfile = open("plaintexts.txt", "w")

for i in range(0,8000):
    a = ''.join(str(random.randint(0, 1)) for x in range(0,16))
    openedfile.write(a + '\n')

openedfile.close()
