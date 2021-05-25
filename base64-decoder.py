import base64
import os

text = 'insert random base64 text'
kekd = text.encode('ascii')
text = base64.b64decode(kekd)
final = text.decode('ascii')
print(final)
input('Press any key to exit!')
