__author__ = 'RetR0'

from hashlib import sha256
import hashlib


print (" ___________________________________________________________\n*************************************************************")
print (""" ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██║██╔════╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ███████╗██║███████╗
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ╚════██║██║╚════██║
╚██████╗██║  ██║   ██║   ██║        ██║   ███████║██║███████║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝╚══════╝""")
print ("*************************************************************\n ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ")
print ("Encrypt/Decrpyt Using different Ciphers, Version F-exe.1.0.1")

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

def version3cipher ():
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n********************AES (cryptodome)*************************")
    print ("*************************************************************")
    print ("\n\n\n╔═══════════════════════════════════════════════════════════╗")
    print ("║ Two way encryption, multi-usage key (re-use same key).    ║ \n║ No authentification.                                      ║")
    print ("╚═══════════════════════════════════════════════════════════╝\n")

if __name__ == "__main__":
    main()

# Version F-exe.1.0.1
