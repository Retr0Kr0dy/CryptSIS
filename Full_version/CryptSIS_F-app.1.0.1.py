__author__ = 'RetR0'

from hashlib import sha256
from os import urandom
import hashlib
import os
import blowfish
import sys


print (" ___________________________________________________________\n*************************************************************")
print (""" ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██║██╔════╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ███████╗██║███████╗
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ╚════██║██║╚════██║
╚██████╗██║  ██║   ██║   ██║        ██║   ███████║██║███████║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝╚══════╝""")
print ("*************************************************************\n ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ")
print ("Encrypt/Decrpyt Using different Ciphers, Version F-app.1.0.1")



def main ():
    to_do = input ("\n\n1 - SHA256/utf-8\n2 - Blowfish\n3 - AES (cryptodome)\n\nPlease enter a number : ")
    if to_do == "1":
        verion1cipher()
    
    if to_do == "2":
        version2cipher()

    if to_do == "3":
        version3cipher()
    



def verion1cipher ():

    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**********************SHA256/utf-8***************************")
    print ("*************************************************************")
    print ("\n\n\n╔═══════════════════════════════════════════════════════════╗")
    print ("║ Two way encryption, key isn't save in a file, you got to  ║ \n║ type it in raw text whenever you want to use this cipher. ║")
    print ("╚═══════════════════════════════════════════════════════════╝\n")
    
    i = 0
    file_to_crypt = input ("Enter the name of the file to encrypt/decrypt :")
    output = input ("Enter the output file name :")
    word_key = input ("Enter the key in raw text : ")

    pre_keys = sha256(word_key.encode('utf-8')).digest()
    hash_keys = hashlib.sha512(pre_keys)
    hash_digest = hash_keys.hexdigest()
    keys = sha256(hash_digest.encode('utf-8')).digest()

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

    #version 1.4 (modified)



def version2cipher ():

    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n************************Blowfish*****************************")
    print ("*************************************************************")
    print ("\n\n\n╔═══════════════════════════════════════════════════════════╗")
    print ("║ Two way encryption, multi-usage key (re-use same key).    ║ \n║ No authentification.                                      ║")
    print ("╚═══════════════════════════════════════════════════════════╝\n")

    to_do = input ("1 - Encrpytion\n2 - Decryption\nPlease enter a number : ")
    if to_do == "1":
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
    elif to_do == "2":
        text = input ("Enter the name of the file to crypt :")
        output = input ("Enter the output file name :")
        keyfile = input ("Import a key file to use or leave empty to create one :")
        if len(keyfile) > 0:
            iv = os.urandom(8)                
            key = os.urandom(56)
            keyfile = keyfile
            try :
                with open (keyfile, 'rb') as f_keyfile:
                    rawkey = f_keyfile.read()
                iv = bytes(rawkey[:8])
                key = bytes(rawkey [8:])
            except EnvironmentError:
                print ("I/O Error")
                exit(-1)        
        elif len(keyfile)== 0 :
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
        print ("Error : invalid Option")
    hashnsalt = blowfish.Cipher(key)

    with open (text, 'rb') as f_file_to_crypt:
        text_block = f_file_to_crypt.read()

    match to_do:   
        case "1":
            data_result = b"".join(hashnsalt.encrypt_cfb(text_block, iv))
        case "2":
            data_result = b"".join(hashnsalt.decrypt_cfb(text_block, iv))

    with open (output, 'wb') as f_output:
        f_output.write(data_result)

    #version 2.6 (modified)



def version3cipher ():
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n********************AES (cryptodome)*************************")
    print ("*************************************************************")
    print ("\n\n\n╔═══════════════════════════════════════════════════════════╗")
    print ("║ Two way encryption, multi-usage key (re-use same key).    ║ \n║ No authentification.                                      ║")
    print ("╚═══════════════════════════════════════════════════════════╝\n")



if __name__ == "__main__":
    main()

# Version F-app.1.0.1
