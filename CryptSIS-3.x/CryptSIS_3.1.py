__author__ = 'RetR0'

from Crypto.Cipher import AES
from os import terminal_size, urandom
import os

#ask for input

text = (input ("text : ").encode()) * 16


#encrypt da string
iv = 16 * b'\x00'
keyfile = 16 * b'\x00'
# iv = urandom(16)
# keyfile = urandom(16)
print (iv)
print (keyfile)
key = AES.new(keyfile, AES.MODE_CBC, iv)

ciphertext = key.encrypt(text)

print (ciphertext)

#decrypt da string
iv = 16 * b'\x00'
keyfile = 16 * b'\x00'
print (iv)
print (keyfile)
key = AES.new(keyfile, AES.MODE_CBC, iv)

ciphertext2 = key.decrypt(ciphertext)
print (ciphertext2)
ciphertext3 = ciphertext2[:int(len(ciphertext2)/16)]
print (ciphertext3)
