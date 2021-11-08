__author__ = 'RetR0'

from Crypto.Cipher import AES
from os import urandom
import os

input_text = input ("text : ")
text = b'input_text' * 2

text_block = input_text
text_block_2 = bytes()
for i in range (len(text_block)):
    c = text_block[i]
    j = i % len(text)
    b = bytes ([c^text[j]])
    text_block_2 = text_block_2 + b

# text = 'hello world 1234'
iv = 16 * b'\x00'
keyfile = 16 * b'\x00'
key = AES.new(keyfile, AES.MODE_CBC, iv)

ciphertext = key.encrypt(text_block_2)

print (ciphertext)

iv = 16 * b'\x00'
keyfile = 16 * b'\x00'
key = AES.new(keyfile, AES.MODE_CBC, iv)

ciphertext2 = key.decrypt(ciphertext)

print (ciphertext2)