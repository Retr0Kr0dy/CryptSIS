__author__ = 'RetR0'

from hashlib import sha256
from os import urandom
import hashlib
import os
import blowfish
import sys

print ("\n")
print ("""             -._.                   .,ad88888ba,.
        _____   '8',             .,ad8888888888888a,
     ,'888,'     '88',          d8P²²²98888P²²²98888b, 
   ,'8888,\       |88|          9b    d8888,    `9888B   
   \8888888\      |88|         ,d88aaa8888888b,,,d888P'  
    \8/^ \88\    ,'8,         d8888888888888888888888b  
          \88\  ,'8,'        d888888P""98888888888888P  
    /88~-._\.8'88,'          88888P'    9888888888888  
   /888_8_8_8~8\             `98P'       9888888888P'     
  /88/'      \88\                         `"9888P"' 
  \8/         \8/'                                  by Krdÿ.  """)

print (" ___________________________________________________________\n*************************************************************")
print (""" ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██║██╔════╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ███████╗██║███████╗
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ╚════██║██║╚════██║
╚██████╗██║  ██║   ██║   ██║        ██║   ███████║██║███████║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝╚══════╝""")
print ("*************************************************************")
print (" Encrypt/Decrpyt Using different Ciphers, Version F-app1.0.1")
print (" -----------------------------------------------------------")


def main ():
    to_do = input ("\nSelect a Cipher.\n\n1 - SHA256/utf-8\n2 - Blowfish\n3 - AES CBC (cryptodome)\n\nPlease enter a number : ")
    if to_do == "1":
        verion1cipher()
    
    if to_do == "2":
        version2cipher()

    if to_do == "3":
        version3cipher()
    


def verion1cipher ():

    print ("\n**********************SHA256/utf-8***************************")
    print ("*************************************************************")
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Two way encryption using simple XOR operation with a      ║
║ raw text key and SHA256/utf-8 encoding.                   ║
║                                                           ║ 
║                                                           ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to enter the key you want to use in raw text ║
║ (you can't save the key).                                 ║
║                                                           ║ 
║                                                           ║ 
║ For decryption, remake the same process, this script is   ║
║ only using XOR opertaion, to make it simple ;             ║
║                                                           ║ 
║      raw_text = 1 0 1 0 0 1 (random binary value)         ║
║           key = 0 1 1 0 1 0 (random binary value)         ║
║  encrypt_text = 0 0 1 1 0 0 (1;1=1 0;0=1 1;0=0 0;1=0)     ║
║           key = 0 1 1 0 1 0 (random binary value)         ║
║  decrypt_text = 1 0 1 0 0 1 (same math)                   ║
║                                                           ║ 
║ As you can see, data came back to it original state by    ║
║ being run through the key a second time.                  ║
╚═══════════════════════════════════════════════════════════╝\n""")
    
    i = 0
    file_to_crypt = input ("Enter the name of the file to encrypt/decrypt :")
    output = input ("\nEnter the output file name :")
    word_key = input ("\nEnter the key in raw text : ")

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

    print ("\n************************Blowfish*****************************")
    print ("*************************************************************")
    print ("\n╔═══════════════════════════════════════════════════════════╗")
    print ("║ Two way encryption, multi-usage key (re-use same key).    ║ \n║ No authentification.                                      ║")
    print ("╚═══════════════════════════════════════════════════════════╝\n")

    to_do = input ("1 - Encrpytion\n2 - Decryption\n\nPlease enter a number : ")
    if to_do == "1":
        text = input ("Enter the name of the file to crypt :")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nImport a key file to use or leave empty to create one :")
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
                print ("\nI/O Error")
                exit(-1)        
        elif len(keyfile) == 0 :
            iv = os.urandom(8)                
            key = os.urandom(56)
            keyfile = input("\nEnter the name of the key file to create : ")
            try:
                with open (keyfile, 'wb') as f_keyfile:
                    f_keyfile.write(iv + key)
            except EnvironmentError:
                print("\nError : key file not found")
                exit(-1)

    elif to_do == "2":
        text = input ("Enter the name of the file to decrypt :")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nEnter the name of the key file to use : ")
        try:
            with open (keyfile, 'rb') as f_key:
                rawkey = f_key.read()
                iv = bytes(rawkey[:8])
                key = bytes(rawkey [8:])
        except EnvironmentError:
            print("\nError : key file not found")
            exit(-1)    
    else:
        print ("\nError : invalid Option")

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
    print ("\n*******************AES CBC (cryptodome)**********************")
    print ("*************************************************************")
    print ("\n╔═══════════════════════════════════════════════════════════╗")
    print ("║ Two way encryption Using AES CBC (cryptodome).            ║ \n║ No authentification, multi-usage key (re-use same key)    ║")
    print ("╚═══════════════════════════════════════════════════════════╝\n")



if __name__ == "__main__":
    main()

# Version F-app.1.0.1

