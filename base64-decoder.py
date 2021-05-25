import base64

text = 'insert random base64 text'
kekd = text.encode('ascii')
text = base64.b64decode(kekd)
final = text.decode('ascii')