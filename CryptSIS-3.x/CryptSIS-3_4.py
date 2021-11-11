__author__ = 'RetR0'

from Crypto.Cipher import AES
from os import terminal_size, urandom
from Crypto.Util.Padding import pad
import os


to_do = input ("What to do, encrypt or decrypt ? e/d :")
to_do_encrypt = to_do == "e" or to_do == "encrypt" or to_do == "-e"
to_do_decrypt = to_do == "d" or to_do == "decrypt" or to_do == "-d"

if to_do_encrypt:
    imput = input ("Enter the name of the file to encrypt :")
    output = input ("Enter the output file name :")
    keyfile = input ("Import a key file to use or leave empty to create one :")
    if len(keyfile) > 0:
        keyfile = keyfile
        try :
            with open (keyfile, 'rb') as f_keyfile:
                rawkey = f_keyfile.read()
            iv = bytes(rawkey[:16])
            key = bytes(rawkey [16:])
            with open (imput, 'rb') as f_file_to_crypt:
                text_block = f_file_to_crypt.read()
                xing = urandom(16)
                text_block = (xing + text_block + xing)
        except EnvironmentError:
                print ("I/O Error")
                exit(-1)
    elif len(keyfile)== 0 :
        iv = os.urandom(16)                
        key = os.urandom(16)
        keyfile = input("Enter the name of the key file to create : ")

        try:
            with open (keyfile, 'wb') as f_keyfile:
                f_keyfile.write(iv + key)
        except EnvironmentError:
            print("Error : key file not found")
            exit(-1)     
        with open (imput, 'rb') as f_file_to_crypt:
            text_block = f_file_to_crypt.read()
            xing = urandom(16)
            xing = xing
            text_block = (xing + text_block + xing)

    cipher = AES.new(key, AES.MODE_CBC)
    data_result = cipher.encrypt(pad(text_block, AES.block_size))

if to_do_decrypt:
    imput = input ("Enter the name of the file to decrypt :")
    output = input ("Enter the output file name :")
    keyfile = input("Enter the name of the key file to use : ")
    try:
        with open (keyfile, 'rb') as f_key:
            rawkey = f_key.read()
            iv = bytes(rawkey[:16])
            key = bytes(rawkey [16:])
    except EnvironmentError:
        print("Error : key file not found")
        exit(-1)
    with open (imput, 'rb') as f_file_to_crypt:
        text_block = f_file_to_crypt.read()

    cipher = AES.new(key, AES.MODE_CBC)
    data_result = cipher.decrypt(pad(text_block, AES.block_size))
    print (data_result)
    text_block_less_char1 = (data_result[:-34])
    text_block_less_char2 = (text_block_less_char1[16:])
    print(text_block_less_char1)
    print(text_block_less_char2)
    data_result = text_block_less_char2
    print (text_block)
    print (data_result)
with open (output, 'wb') as f_output:
    f_output.write(data_result)


#version 3.4
