a = open('flag.jpg','rb')
b = open('flag.png','wb')
b.write(a.read()[::-1])