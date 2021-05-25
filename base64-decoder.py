import base64
#imports
print('========================')
text = 'aW5zZXJ0IHJhbmRvbSBiYXNlNjQgdGV4dA=='
kekd = text.encode('ascii')
text = base64.b64decode(kekd)
final = text.decode('ascii')
print(final)

e = input("""=========================
Press any key to exit!""")

#note: this was extremely easy to make lol.
