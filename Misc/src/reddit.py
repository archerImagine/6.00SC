head = " o  "
body = "/|\ "
leg =  "/ \ "

heads = ''
bodys = ''
legs = ''

for i in range(20): # Changed as suggested by /u/JWStarfish
    heads += head
    bodys += body
    legs += leg

for i in range(5000): # Changed as suggested by /u/JWStarfish
    print heads
    print bodys
    print legs