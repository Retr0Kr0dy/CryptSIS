__author__ = 'RetR0'

from hashlib import sha256
from os import urandom
import os
import hashlib
import blowfish
import sys

to_do = input ("What to do, encrypt or decrypt ? e/d :")

if to_do == "d":
    text = input ("Enter the name of the file to decrypt :")
    output = input ("Enter the output file name :")
    keyfile = input("Enter the name of the key file to use : ")
    try:
        with open (keyfile, 'rb') as f_key:
            rawkey = f_key.read()
            iv = bytes(rawkey[:8])
            key = bytes(rawkey [8:])
    except EnvironmentError:
        print("Error : key file not found")
        exit(-1)
elif to_do == "e":
    text = input ("Enter the name of the file to crypt :")
    output = input ("Enter the output file name :")
    keytype = input ("Import a key file to use or leave empty to create one :")
    if len(keytype) > 0:
        iv = os.urandom(8)                
        key = os.urandom(56)
        keyfile = keytype
        try :
            with open (keyfile, 'rb') as f_keyfile:
                rawkey = f_keyfile.read()
            iv = bytes(rawkey[:8])
            key = bytes(rawkey [8:])
        except EnvironmentError:
            print ("I/O Error")
            exit(-1)        
    elif len(keytype)== 0 :
        iv = os.urandom(8)                
        key = os.urandom(56)
        keyfile = input("Enter the name of the key file to create : ")

        try:
            with open (keyfile, 'wb') as f_keyfile:
                f_keyfile.write(iv + key)
        except EnvironmentError:
            print("Error : key file not found")
            exit(-1)
else:
    print ("Error : invalid Option for encryption/decryption, please type [e] (for encrypt) or type [d] (for decrypt)")
    exit(-1)

hashnsalt = blowfish.Cipher(key)

with open (text, 'rb') as f_file_to_crypt:
    text_block = f_file_to_crypt.read()

match to_do:   
    case "e":
        data_result = b"".join(hashnsalt.encrypt_cfb(text_block, iv))
    case "d":
        data_result = b"".join(hashnsalt.decrypt_cfb(text_block, iv))

with open (output, 'wb') as f_output:
     f_output.write(data_result)


#version 2.5
