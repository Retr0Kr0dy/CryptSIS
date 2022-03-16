from hashlib import sha256
from os import urandom
import ntpath
import hashlib
import os
import blowfish
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives import serialization
from Crypto import Random
import base64

def main ():
  
    print ('\x1b[0;31;40m' + " ___________________________________________________________\n*************************************************************")
    print (""" ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██║██╔════╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ███████╗██║███████╗
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ╚════██║██║╚════██║
╚██████╗██║  ██║   ██║   ██║        ██║   ███████║██║███████║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝╚══════╝""")
    print ("*************************************************************")
    print (" Encrypt/Decrpyt Using different Ciphers, Version F-app1.0.6")
    print (" -----------------------------------------------------------" + '\x1b[0m')
    print ("\n")

    print('\x1b[4;30;43m' + "Select a Cipher." + '\x1b[0m' + "\n\n" + '\x1b[0;32;40m' + '[1]' + '\x1b[0m' + "  SHA256/utf-8" + "\n" + '\x1b[0;32;40m' + '[2]' + '\x1b[0m' + "  Blowfish"  + "\n" + '\x1b[0;32;40m' + '[3]' + '\x1b[0m' + "  AES-256-CBC"  + "\n" + '\x1b[0;32;40m' + '[4]' + '\x1b[0m' + "  RSA"  + "\n" + '\x1b[0;32;40m' + '[5]' + '\x1b[0m' + "  AES-256-CBC + RSA-4096" + "\n\n" + '\x1b[0;35;40m' + '[55]' + '\x1b[0m' + "  Woking with folder" + "\n\n" + '\x1b[0;31;40m' + '[99]' + '\x1b[0m' + "  Exit")
    to_do = input ("\n\nPlease enter a number : ")
    if to_do == "1":
        version1cipher()
    if to_do == "2":
        version2cipher()

    # if to_do == "3":
    #     version3cipher()

    # if to_do == "4":
    #     version4cipher()

    # if to_do == "5":
    #     version5cipher()

    # if to_do == "6":
    #     version6cipher()

    if to_do == "55":
        workingwithfolder()

    if to_do == "99" or to_do == "exit" or to_do == "quit" or to_do == "bye":
        exit(-1)
    else:
        print ("\n")
        input ('\x1b[4;31;40m'+"Error : Invalid Option (press enter to continue)"+'\x1b[0m'+"\n")
        main()

def version1cipher():

    print ('\x1b[4;30;47m' + "\n**********************SHA256/utf-8***************************")
    print ("*************************************************************" + '\x1b[0m')
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Two way encryption using simple XOR operation with a      ║
║ raw text key and SHA256/utf-8 encoding.                   ║
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
║                                                           ║ 
║                                                           ║ 
║ Usage :                                                   ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to enter the key you want to use in raw text ║
║ (you can't save the key).                                 ║
║ [more info in README.md]                                  ║
╚═══════════════════════════════════════════════════════════╝\n""")

    print('\x1b[4;30;43m' + "Select an option." + '\x1b[0m' + "\n\n" + '\x1b[0;32;40m' + '[1]' + '\x1b[0m' + "  Encryption/Decryption" + "\n\n" + '\x1b[0;31;40m' + '[99]' + '\x1b[0m' + "  Go to main menu")
    to_do = input ("\n\nPlease enter a number : ")
    if to_do == "1":
        i = 0
        file_to_crypt = input ("\n\nEnter the name of the file to encrypt/decrypt :")
        try:                
            with open (file_to_crypt, 'rb') as f_file_to_crypt:
                text_block = f_file_to_crypt.read()
                text_block_2 = bytes()
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  Target Locked !!!")
        except:
            input ("\n" +'\x1b[4;31;40m'+f"Error : {file_to_crypt} File not Found (press enter to continue)"+'\x1b[0m'+"\n")
            version1cipher()       
        output = input ("\nEnter the output file name :")
        word_key = input ("\nEnter the key in raw text : ")
        try:
            print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Setting up encoder ...")
            pre_keys = sha256(word_key.encode('utf-8')).digest()
            hash_keys = hashlib.sha512(pre_keys)
            hash_digest = hash_keys.hexdigest()
            keys = sha256(hash_digest.encode('utf-8')).digest()
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ('\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        try:
            print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Encrypting ...")
            for i in range (len(text_block)):
                c = text_block[i]
                j = i % len(keys)
                b = bytes ([c^keys[j]])
                text_block_2 = text_block_2 + b
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ('\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        try:
            print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Writting Data ...")
            with open (output, 'wb') as f_output:
                f_output.write(text_block_2)
                print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
                print ("\n" + '\x1b[0;30;42m' + '[-]' + '\x1b[0m' + "  COMPLETED")
                input("\n\npress enter to continue")
                main()
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
    if to_do == "99":
       main()
    else:
        print ("\n")
        input ('\x1b[4;31;40m'+"Error : Invalid Option (press enter to continue)"+'\x1b[0m'+"\n")
        version1cipher()

def version2cipher():
    print ('\x1b[4;30;47m' + "\n************************Blowfish*****************************")
    print ("*************************************************************" + '\x1b[0m')
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Encryption/Decryption using the Blowfish Cipher.          ║
║ (no Authentification).                                    ║
║                                                           ║ 
║ Blowfish a block cipher, meaning that it divides a        ║
║ message up into fixed length blocks during encryption     ║
║ and decryption.                                           ║
║                                                           ║ 
║ Usage :                                                   ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to create a key file or use an existant key  ║
║ file.                                                     ║
║ [more info in README.md]                                  ║
╚═══════════════════════════════════════════════════════════╝\n""")

    print('\x1b[4;30;43m' + "Select an option." + '\x1b[0m' + "\n\n" + '\x1b[0;32;40m' + '[1]' + '\x1b[0m' + "  Encryption" + "\n"  + '\x1b[0;32;40m' + '[2]' + '\x1b[0m' + "  Decryption" + "\n\n" + '\x1b[0;31;40m' + '[99]' + '\x1b[0m' + "  Go to main menu")
    to_do = input ("\n\nPlease enter a number : ")
    if to_do == "1":
        file_to_crypt = input ("\n\nEnter the name of the file to crypt :")
        try:
            with open (file_to_crypt, 'rb') as f_file_to_crypt:
                text_block = f_file_to_crypt.read()
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  Target Locked !!!")
        except:
            input ("\n" +'\x1b[4;31;40m'+f"Error : {file_to_crypt} File not Found (press enter to continue)"+'\x1b[0m'+"\n")
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
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  Keyfile Locked !!!")
            except EnvironmentError:
                input ("\n" +'\x1b[4;31;40m'+f"Error : Key file not found (press enter to continue)"+'\x1b[0m'+"\n")
                version2cipher()    
        elif len(keyfile) == 0 :
            iv = os.urandom(8)                
            key = os.urandom(56)
            keyfile = input("\nEnter the name of the key file to create : ")
            try:
                with open (keyfile, 'wb') as f_keyfile:
                    f_keyfile.write(iv + key)
                print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Keyfile generated")
            except EnvironmentError:
                input ("\n" +'\x1b[4;31;40m'+f"Error : Keyfile generation failed (press enter to continue)"+'\x1b[0m'+"\n")
                version2cipher() 
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Setting up encoder ...")
        try: 
            hashnsalt = blowfish.Cipher(key)
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Encrypting ...")
        try:
            data_result = b"".join(hashnsalt.encrypt_cfb(text_block, iv))
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Writting Data ...")
        try:
            with open (output, 'wb') as f_output:
                f_output.write(data_result)
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;30;42m' + '[-]' + '\x1b[0m' + "  COMPLETED")
        input("\n\npress enter to continue")
        main()
    if to_do == "2":
        file_to_crypt = input ("\n\nEnter the name of the file to decrypt :")
        try:
            with open (file_to_crypt, 'rb') as f_file_to_crypt:
                text_block = f_file_to_crypt.read()
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  Target Locked !!!")
        except:
            input ("\n" +'\x1b[4;31;40m'+f"Error : {file_to_crypt} File not Found (press enter to continue)"+'\x1b[0m'+"\n")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nEnter the name of the key file to use : ")
        try:
            with open (keyfile, 'rb') as f_key:
                rawkey = f_key.read()
                iv = bytes(rawkey[:8])
                key = bytes(rawkey [8:])
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  Keyfile Locked !!!")
        except EnvironmentError:
            input ("\n" +'\x1b[4;31;40m'+f"Error : Key file not found (press enter to continue)"+'\x1b[0m'+"\n")
            version2cipher()  
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Setting up encoder ...")
        try: 
            hashnsalt = blowfish.Cipher(key)
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Decrypting ...")
        try:
            data_result = b"".join(hashnsalt.decrypt_cfb(text_block, iv))
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Writting Data ...")
        try:
            with open (output, 'wb') as f_output:
                f_output.write(data_result)
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;30;42m' + '[-]' + '\x1b[0m' + "  COMPLETED")
        input("\n\npress enter to continue")
        main()
    if to_do == "99":
        main()









def workingwithfolder():
    print('\x1b[4;30;43m' + "Select a Cipher." + '\x1b[0m' + "\n\n" + '\x1b[0;32;40m' + '[1]' + '\x1b[0m' + "  Blowfish"  + "\n" + '\x1b[0;32;40m' + '[3]' + '\x1b[0m' + "  AES-256-CBC"  + "\n" + '\x1b[0;32;40m' + '[4]' + '\x1b[0m' + "  RSA"  + "\n\n" + '\x1b[0;31;40m' + '[99]' + '\x1b[0m' + "  Exit")
    to_do2 = input ("\n\nPlease enter a number : ")
    if to_do2 == '1':
        folder1cipher()

def folder1cipher():
    print ('\x1b[4;30;47m' + "\n************************Blowfish*****************************")
    print ("*************************************************************" + '\x1b[0m')
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Encryption/Decryption using the Blowfish Cipher.          ║
║ (no Authentification).                                    ║
║                                                           ║ 
║ Blowfish a block cipher, meaning that it divides a        ║
║ message up into fixed length blocks during encryption     ║
║ and decryption.                                           ║
║                                                           ║ 
║ Usage :                                                   ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to create a key file or use an existant key  ║
║ file.                                                     ║
║ [more info in README.md]                                  ║
╚═══════════════════════════════════════════════════════════╝\n""")

    print('\x1b[4;30;43m' + "Select an option." + '\x1b[0m' + "\n\n" + '\x1b[0;32;40m' + '[1]' + '\x1b[0m' + "  Encryption" + "\n"  + '\x1b[0;32;40m' + '[2]' + '\x1b[0m' + "  Decryption" + "\n\n" + '\x1b[0;31;40m' + '[99]' + '\x1b[0m' + "  Go to main menu")
    to_do = input ("\n\nPlease enter a number : ")
    files = []
    if to_do == "1":
        folder_to_crypt = input ("\n\nEnter the name of the folder to crypt :")
        try:
            for r, d, f in os.walk(folder_to_crypt):
                for file in f:
                    if '.' in file:
                        files.append(os.path.join(r, file))
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  File list Locked !!!")
        except:
            input ("\n" +'\x1b[4;31;40m'+f"Error : {folder_to_crypt} Folder not Found (press enter to continue)"+'\x1b[0m'+"\n")
        output = input ("\nEnter the output folder name :")
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
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  Keyfile Locked !!!")
            except EnvironmentError:
                input ("\n" +'\x1b[4;31;40m'+f"Error : Key file not found (press enter to continue)"+'\x1b[0m'+"\n")
                folder1cipher()    
        elif len(keyfile) == 0 :
            iv = os.urandom(8)                
            key = os.urandom(56)
            keyfile = input("\nEnter the name of the key file to create : ")
            try:
                with open (keyfile, 'wb') as f_keyfile:
                    f_keyfile.write(iv + key)
                print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Keyfile generated")
            except EnvironmentError:
                input ("\n" +'\x1b[4;31;40m'+f"Error : Keyfile generation failed (press enter to continue)"+'\x1b[0m'+"\n")
                folder1cipher() 
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Setting up encoder ...")
        try: 
            hashnsalt = blowfish.Cipher(key)
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Encrypting ...")
        try:
            for f in files:
                with open (f, 'rb') as f_file_to_encrypt:
                    text_block = f_file_to_encrypt.read()
                data_result = b"".join(hashnsalt.encrypt_cfb(text_block, iv))
                try:
                    fn = ntpath.basename(f)
                    o_output = output + "\\" + fn
                    with open (o_output, 'wb') as f_output:
                        f_output.write(data_result)
                    print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + f"  Succeed with : {f}")
                except:
                    print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + f"  Error with : {f}")
                    continue
            print ("\n" + '\x1b[0;30;42m' + '[-]' + '\x1b[0m' + "  COMPLETED")
            input("\n\npress enter to continue")
            main()
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error : Encryption failed")
    if to_do == "2":
        folder_to_crypt = input ("\n\nEnter the name of the folder to decrypt :")
        try:
            for r, d, f in os.walk(folder_to_crypt):
                for file in f:
                    if '.' in file:
                        files.append(os.path.join(r, file))
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  File list Locked !!!")
        except:
            input ("\n" +'\x1b[4;31;40m'+f"Error : {folder_to_crypt} Folder not Found (press enter to continue)"+'\x1b[0m'+"\n")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nEnter the name of the key file to use : ")
        try:
            with open (keyfile, 'rb') as f_key:
                rawkey = f_key.read()
                iv = bytes(rawkey[:8])
                key = bytes(rawkey [8:])
                print ("\n" + '\x1b[0;34;40m' + '[-]' + '\x1b[0m' + "  Keyfile Locked !!!")
        except EnvironmentError:
            input ("\n" +'\x1b[4;31;40m'+f"Error : Key file not found (press enter to continue)"+'\x1b[0m'+"\n")
            version2cipher()  
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Setting up encoder ...")
        try: 
            hashnsalt = blowfish.Cipher(key)
            print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + "  Succeed")
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error")
        print ("\n" + '\x1b[0;36;40m' + '[-]' + '\x1b[0m' + "  Decrypting ...")
        try:
            for f in files:
                with open (f, 'rb') as f_file_to_encrypt:
                    text_block = f_file_to_encrypt.read()
                data_result = b"".join(hashnsalt.encrypt_cfb(text_block, iv))
                try:
                    fn = ntpath.basename(f)
                    o_output = output + "\\" + fn
                    with open (o_output, 'wb') as f_output:
                        f_output.write(data_result)
                    print ('\x1b[0;32;40m' + '[-]' + '\x1b[0m' + f"  Succeed with : {f}")
                except:
                    print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + f"  Error with : {f}")
                    continue
            print ("\n" + '\x1b[0;30;42m' + '[-]' + '\x1b[0m' + "  COMPLETED")
            input("\n\npress enter to continue")
            main()
        except:
            print ("\n" + '\x1b[0;31;40m' + '[-]' + '\x1b[0m' + "  Error : Decryption failed")
    if to_do == "99":
        main()



if __name__ == "__main__":
    main()

# Version_AZURA-app.0.0.1
