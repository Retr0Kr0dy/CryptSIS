__author__ = 'RetR0'

from hashlib import sha256

file_to_crypt = input ("file to crypt :")
output = input ("output file name :")
word_key = ("6F097675C6398E12BAEFC974263901680172324796B189A3568D610E7F84B9BE")
keys = sha256(word_key.encode('utf-8')).digest()
with open (file_to_crypt, 'rb') as f_file_to_crypt:
    text_block = f_file_to_crypt.read()
    text_block_2 = bytes()
for i in range (len(text_block)):
    c = text_block[i]
    j = i % len(keys)
    b = bytes ([c^keys[j]])
    text_block_2 = text_block_2 + b
with open (output, 'wb') as f_output:
    f_output.write(text_block_2)
print (text_block)
print (type(text_block_2))

#version 1.3
