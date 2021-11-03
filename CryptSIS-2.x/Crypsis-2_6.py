__author__ = 'RetR0'

from os import urandom
import os
import blowfish
import sys

if len(sys.argv) == 1:
    if len(sys.argv) == 1:
        to_do = input ("What to do, encrypt or decrypt ? e/d :")
        to_do_encrypt = to_do == "e" or to_do == "encrypt" or to_do == "-e"
        to_do_decrypt = to_do == "d" or to_do == "decrypt" or to_do == "-d"
        if to_do_decrypt:
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
        elif to_do_encrypt:
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
            print ("Error : invalid Option for encryption/decryption, please type [e],[encrypt],[-e] (for encrypt) or type [d],[decrypt],[-d] (for decrypt)")
        hashnsalt = blowfish.Cipher(key)
        
        with open (text, 'rb') as f_file_to_crypt:
            text_block = f_file_to_crypt.read()

    elif len(sys.argv) > 1:
        option = sys.argv[2]
        print (option)
        if option == "-d" :
            try:
                with open (sys.argv[5], 'rb') as f_key:
                    rawkey = f_key.read()
                    iv = bytes(rawkey[:8])
                    key = bytes(rawkey [8:])
            except EnvironmentError:
                print("Error : key file not found")
                exit(-1)
        elif option == "-e":
            iv = os.urandom(8)                
            key = os.urandom(56)
            keyfile = sys.argv[5]
            try :
                with open (keyfile, 'wb') as f_keyfile:
                    f_keyfile.write(iv + key)
            except EnvironmentError:
                print ("IO Error")
                exit(-1)
        else:
            print("Error : wrong script argument or options. Usage is : <option> <Input file> <Output File> [Custom key file]\n\nOptions :\n\n-e : Encrypt the input file into the output file\n\n-d : Decrypt the input file into the output file\n\n\nIf no custom key is given, it will generate a random string and ask for a filename \n\n(only work for -e option ; for -d option, you need to specify a key file for the script to work).")
            exit(-1)

        text = sys.argv[3]
        output = sys.argv[4]
        hashnsalt = blowfish.Cipher(key)
        with open (text, 'rb') as f_file_to_crypt:
            text_block = f_file_to_crypt.read()

    elif len(sys.argv) < 4:
        print("Error : wrong script argument or options. Usage is : <option> <Input file> <Output File> [Custom key file]\n\n\nOptions :\n\n-e : Encrypt the input file into the output file\n\n-d : Decrypt the input file into the output file\n\n\nIf no custom key is given, it will generate a random string and ask for a filename \n(only work for -e option ; for -d option, you need to specify a key file for the script to work).")
        exit(-1)        

elif len(sys.argv) > 1:
    if len(sys.argv) > 1:
        to_do = sys.argv[1] 
        to_do_encrypt = to_do == "e" or to_do == "encrypt" or to_do == "-e"
        to_do_decrypt = to_do == "d" or to_do == "decrypt" or to_do == "-d"
        if to_do_decrypt:
            text = sys.argv[2] 
            output = sys.argv[3]
            keyfile = sys.argv[4]
            try:
                with open (keyfile, 'rb') as f_key:
                    rawkey = f_key.read()
                    iv = bytes(rawkey[:8])
                    key = bytes(rawkey [8:])
            except EnvironmentError:
                print("Error : key file not found")
                exit(-1)
        elif to_do_encrypt:
            text = sys.argv[2] 
            output = sys.argv[3]
            keyfile = sys.argv[4]

            if len(keyfile) == "create" :
                iv = os.urandom(8)                
                key = os.urandom(56)
                keyfile = sys.argv[5]

            elif len(keyfile) > 0:
                iv = os.urandom(8)                
                key = os.urandom(56)
                keyfile = keyfile
                try :
                    with open (keyfile, 'rb') as f_keyfile:
                        rawkey = f_keyfile.read()
                    iv = bytes(rawkey[:8])
                    key = bytes(rawkey [8:])
                except EnvironmentError:
                    iv = os.urandom(8)                
                    key = os.urandom(56)
                    keyfile = input ("Enter name for the key file that going to be created : ")       
                try:
                    with open (keyfile, 'wb') as f_keyfile:
                        f_keyfile.write(iv + key)
                except EnvironmentError:
                    iv = os.urandom(8)                
                    key = os.urandom(56)
                    keyfile = input ("Enter name for the key file that going to be created : ")
        else:
            print ("Error : invalid Option for encryption/decryption, please type [e],[encrypt],[-e] (for encrypt) or type [d],[decrypt],[-d] (for decrypt)")
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


#version 2.6
