__author__ = 'RetR0'

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

to_do = input ("1 - Encrpytion\n2 - Decryption\n\nPlease enter a number : ")

if to_do == "1":
    text = input ("\nEnter the name of the file to crypt :")
    output = input ("\nEnter the output file name :")
    keyfile = input ("\nImport a key file to use or leave empty to create one :")
    if len(keyfile) > 0:
        try:
            with open (keyfile, 'rb') as f_key:
                key = f_key.read()
        except:
            print ("Error : Key file not found")
            exit (-1)
    if len(keyfile) == 0:
        key = get_random_bytes(32)
        keyfile = input("Enter the name of the key file to create : ")
        try:
            with open (keyfile, 'wb') as f_keyfile:
                f_keyfile.write(key)
        except: 
            print ("Error : I/O")
            exit (-1)
    try:
        with open (text, 'rb') as f_file_to_encrypt:
            text_block = f_file_to_encrypt.read()
    except:
        print("File not found")
        exit(-1)
    cipher = AES.new(key, AES.MODE_CBC)
    data_result = cipher.encrypt(pad(text_block, AES.block_size))
    try:
        with open(output, 'wb') as f_output:
            f_output.write(data_result)
    except:
        print ("Error : I/O")

if to_do == "2":
    text = input ("\nEnter the name of the file to crypt :")
    output = input ("\nEnter the output file name :")
    keyfile = input ("\nImport a key file to use or leave empty to create one :")
    try:
        with open (keyfile, 'rb') as f_key:
            key = f_key.read()
    except:
        print ("Error : Key file not found")
        exit (-1)
    try:
        with open (text, 'rb') as f_file_to_decrypt:
            text_block = f_file_to_decrypt.read()
    except:
        print("File not found")
        exit(-1)
    iv = text_block [:16]
    encrypted_data = text_block [16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    data_result = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    try:
        with open(output, 'wb') as f_output:
            f_output.write(data_result)
    except:
        print ("Error : I/O")
        exit (-1)

#Version 3.5
