__author__ = 'RetR0'

from hashlib import sha256


i = 0
file_to_crypt = input ("file to crypt :")
output = input ("output file name :")
word_key = ("6F097675C6398E12BAEFC974263901680172324796B189A3568D610E7F84B9BE")
keys = sha256(word_key.encode('utf-8')).digest()


with open (file_to_crypt, 'rb') as f_file_to_crypt:
        with open (output, 'wb') as f_output:
            while f_file_to_crypt.peek():
                c = ord(f_file_to_crypt.read(1))
                j = i % len(keys)
                b = bytes ([c^keys[j]])
                f_output.write(b)
                i= i + 1
                
                
#version 1.2
