import base64
#imports
text = input('Give me some text to decode!')
print('=========================')
kekd = text.encode('ascii')
text = base64.b64decode(kekd)
final = text.decode('ascii')
print(final)

e = input("""=========================
Press enter to exit!""")

#note: this was extremely easy to make lol.
