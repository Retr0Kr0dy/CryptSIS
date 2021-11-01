__author__ = 'RetR0'

from hashlib import sha256
from os import urandom
import os
import hashlib
import blowfish

text = input ("text :")
output = input ("output file name :")
key = urandom(56)
iv = urandom(8)
hashnsalt = blowfish.Cipher(key)
with open (text, 'rb') as f_file_to_crypt:
    text_block = f_file_to_crypt.read()
data_encryption = hashnsalt.encrypt_cfb(text_block, iv)

text_to_write = data_encryption.decode()
print (text_to_write)

#version 2.1
